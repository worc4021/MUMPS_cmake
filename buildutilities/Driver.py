import os
import sys
from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
from makeLexer import makeLexer as Lexer
from makeParser import makeParser as Parser
from DependencyListener import DependencyListener as Listener
from DependencyGraph import DependencyGraph
from Templater import Templater
from FortranModuleTree import getDependencyGraph

def unique(lst : list[str]) -> list[str]:
    retval = []
    for l in lst:
        if l not in retval:
            retval.append(l)
    return retval

def main(argv):
    if len(argv) < 2:
        print("Usage: Driver.py <input file>")
        return

    input_stream = FileStream(argv[1])
    lexer = Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = Parser(stream)
    tree = parser.file_()
    if parser.getNumberOfSyntaxErrors() > 0:
        print("syntax errors")
    else:
        listener = Listener()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
    
    # listener.graph.merge(listener.variables)
    # with open("output.dot", "w+") as f:
    #     f.write(listener.graph.toDOT())
    # print("output written to output.dot")

    recipes = listener.graph
    variables = listener.variables

    basedir = os.path.dirname(argv[1])
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

    
    dg.add_dependency('${ARITH}mumps_f77.o','${ARITH}mumps_c.o')

    # This one somehow is implicit
    for lib in ['mumps_common.lib','mumps::pord','metis::metis','mumps::mpiseq','MKL::MKL']:
        dg.add_dependency('${ARITH}mumps.lib', lib)
        dg.add_dependency('mumps_common.lib', lib)
    
    templater = Templater(dg)

    with open("CMakeLists.txt", "w+") as f:
        f.write(templater.many_objects())

    

if __name__ == '__main__':
    main(sys.argv)