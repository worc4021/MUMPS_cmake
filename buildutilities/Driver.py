import os
import sys
from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
from makeLexer import makeLexer as Lexer
from makeParser import makeParser as Parser
from DependencyListener import DependencyListener as Listener
from DependencyGraph import DependencyGraph
from Templater import Templater

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
    
    recipes = listener.graph
    variables = listener.variables

    basedir = os.path.dirname(argv[1])
    keytargets = ['$(libdir)/lib$(ARITH)mumps$(PLAT)$(LIBEXT)','$(libdir)/libmumps_common$(PLAT)$(LIBEXT)']
    
    dg = DependencyGraph(basedir)

    for key in keytargets:
        objlist = []
        for var in recipes.edges[key]:
            for deps in variables.edges[var]:
                
                dg.add_object(deps)

                if  recipes.has_node(deps):
                    for dep in recipes.edges[deps]:
                        dg.add_dependency(deps, dep)

            objlist += variables.edges[var]
        recipes.edges[key] = unique(objlist)
        libname = key.replace('$(libdir)/lib','').replace('$(PLAT)$(LIBEXT)','.lib').replace('$(ARITH)','${ARITH}')
        dg.add_object(libname)
        for deps in unique(objlist):
            dg.add_dependency(libname, deps)

    # This one somehow is implicit
    dg.add_dependency('${ARITH}mumps.lib', 'mumps_common.lib')

    templater = Templater(dg)

    with open("CMakeLists.txt", "w+") as f:
        f.write(templater.flat_libraries('${ARITH}mumps.lib'))
   

if __name__ == '__main__':
    main(sys.argv)