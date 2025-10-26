import os
import sys
from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
from makeLexer import makeLexer as Lexer
from makeParser import makeParser as Parser
from DependencyListener import DependencyListener as Listener
from DependencyGraph import DependencyGraph
from Templater import Templater
from FortranModuleTree import getDependencyGraph
import logging

def downloadsource(version: str, destdir: str) -> None:

    url=f"https://mumps-solver.org/MUMPS_{version}.tar.gz"
    import urllib.request
    import tarfile
    logging.info(f"Downloading MUMPS version {version} to {destdir}")
    with urllib.request.urlopen(url) as response:
        with open(os.path.join(destdir, f"MUMPS_{version}.tar.gz"), "wb") as out_file:
            out_file.write(response.read())

    with tarfile.open(os.path.join(destdir, f"MUMPS_{version}.tar.gz"), "r:gz") as tar:
        tar.extractall(path=destdir,filter='data')

def unique(lst : list[str]) -> list[str]:
    retval = []
    for l in lst:
        if l not in retval:
            retval.append(l)
    return retval

def main():
    from argparse import ArgumentParser
    from os.path import join
    from os import getcwd
    inputParser = ArgumentParser(   prog = 'mumps-cmake',
                                    description = 'Generate cmake build scripts for mumps solver',
                                    epilog = 'M. Schaich - @worc4021' )
    inputParser.add_argument('mumpsversion', help=r'MUMPS version to download (e.g. 5.8.1)')
    inputParser.add_argument('-o','--output', help='Output directory', required=False, default=join(getcwd(),'output'))
    inputParser.add_argument('-l','--loglevel', help='Set log level', required=False, default='INFO', choices=['DEBUG','INFO','WARNING','ERROR','CRITICAL'])
    
    args = inputParser.parse_args() 

    logging.basicConfig(format='%(asctime)s - %(levelname)s -- %(name)s - %(message)s', 
                        datefmt='%d-%b-%y %H:%M:%S',
                        level=args.loglevel,
                        stream=sys.stdout)
    logging.captureWarnings(True)

    destdir = args.output
    if not os.path.exists(destdir):
        os.makedirs(destdir)
    else:
        logging.warning(f"Output directory {destdir} already exists, files might be overwritten")
    downloadsource(args.mumpsversion, destdir)
    
    input_stream = FileStream(join(destdir, f'MUMPS_{args.mumpsversion}','src', 'Makefile'))
    lexer = Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = Parser(stream)
    tree = parser.file_()
    if parser.getNumberOfSyntaxErrors() > 0:
        logging.error("syntax errors")
    else:
        listener = Listener()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
    
    # # listener.graph.merge(listener.variables)
    # # with open("output.dot", "w+") as f:
    # #     f.write(listener.graph.toDOT())
    # # print("output written to output.dot")

    recipes = listener.graph
    variables = listener.variables

    basedir = join(destdir, f'MUMPS_{args.mumpsversion}','src')
    keytargets = ['$(libdir)/lib$(ARITH)mumps$(PLAT)$(LIBEXT)','$(libdir)/libmumps_common$(PLAT)$(LIBEXT)']
    
    dg = DependencyGraph(basedir)
    dgFromSource = getDependencyGraph(basedir)

    for key in keytargets:
        objlist = []
        for var in recipes.edges[key]:
            for deps in variables.edges[var]:
                
                dg.add_object(deps)

                depedencies = dgFromSource.get_dependencies(deps)

                if  recipes.has_node(deps):
                    for dep in recipes.edges[deps]:
                        dg.add_dependency(deps, dep)
                if len(depedencies) > 1:
                    for dep in depedencies:
                        dg.add_dependency(deps, dep)

            objlist += variables.edges[var]
        recipes.edges[key] = unique(objlist)
        libname = key.replace('$(libdir)/lib','').replace('$(PLAT)$(LIBEXT)','.lib').replace('$(ARITH)','${ARITH}')
        dg.add_object(libname)
        for deps in unique(objlist):
            dg.add_dependency(libname, deps)

    
    for obj in ['${ARITH}mumps_f77.o','${ARITH}fac_mem_dynamic.o']:
        dg.add_dependency(obj,'${ARITH}mumps_c.o')

    # # This one somehow is implicit
    for lib in ['mumps_common.lib','mumps::pord','metis','mumps::mpiseq','BLAS::BLAS']:
        dg.add_dependency('${ARITH}mumps.lib', lib)
        dg.add_dependency('mumps_common.lib', lib)
    
    templater = Templater(dg)
    from pathlib import Path
    targetfile = Path(__file__).resolve().parent.parent / "src" / "CMakeLists.txt"

    with open(targetfile, "w+") as f:
        f.write(templater.many_objects())
        

if __name__ == '__main__':
    main()