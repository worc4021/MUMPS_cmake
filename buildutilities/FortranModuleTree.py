import os
import sys
import re

from DependencyGraph import DependencyGraph

def modulesDeclared(text : str) -> dict:
    retval = {
        'uses': [],
        'provides': [],
    }
    m = re.findall(r'MODULE\s+(\w+)', text)
    if m:
        for match in m:
            if match not in retval['provides']:
                retval['provides'].append(match)
        
    m = re.findall(r'USE\s+([DSCZ]?MUMPS\w+)', text)
    if m:
        for match in m:
            if match not in retval['uses']:
                retval['uses'].append(match)
    return retval

def getDependencyGraph(basedir:str) -> DependencyGraph:
    
    files = [f for f in os.listdir(basedir) if f.endswith('F')]
    
    aliases = {}
    dependencies = {}

    for file in files:
        with open(os.path.join(basedir,file)) as f:
            text = f.read()
            modules = modulesDeclared(text)
            aliases[file] = modules['provides']
            dependencies[file] = []
            for dep in modules['uses']:
                if dep not in aliases[file]:
                    dependencies[file].append(dep)
                        
    g = DependencyGraph(basedir=basedir)
    aliasmap = {}
    for a in aliases:
        if aliases[a]:
            for alias in aliases[a]:
                aliasmap[alias] = a


    for d in dependencies:
        g.add_object(d)
        for dep in dependencies[d]:
            if dep in aliasmap:
                g.add_dependency(d,aliasmap[dep])
            else:
                raise Exception(f"Module {dep} not found in any file")

    dg = DependencyGraph(basedir)

    for file in g.dependencies:
        deps = g.dependencies[file]
        if file.startswith('c') and 'd'+file[1:] in g.dependencies:
            file = '${ARITH}'+file[1:]
            obj = file.replace('.F','.o')
        elif (file.startswith('d') and 'c'+file[1:] in g.dependencies) or (file.startswith('s') and 'c'+file[1:] in g.dependencies) or (file.startswith('z') and 'c'+file[1:] in g.dependencies):
            continue
        else:
            obj = file.replace('.F','.o')
        
        dg.add_object(obj)
        dg.add_dependency(obj, file)

        for dep in deps:
            if dep.startswith('c') and 'd'+dep[1:] in g.dependencies:
                dep = '${ARITH}'+dep[1:]
            elif (dep.startswith('d') and 'c'+dep[1:] in g.dependencies) or (dep.startswith('s') and 'c'+dep[1:] in g.dependencies) or (dep.startswith('z') and 'c'+file[1:] in g.dependencies):
                continue
            dg.add_dependency(obj, dep.replace('.F','.o'))
    return dg



def main(argv):
    if len(argv) < 2:
        print("Usage: Driver.py <input make file>")
        return

    basedir = os.path.dirname(argv[1])
    dg = getDependencyGraph(basedir)    

    print(dg)

    # with open("modules.dot", "w+") as f:
    #     f.write(g.toDOT())



if __name__ == '__main__':
    main(sys.argv)