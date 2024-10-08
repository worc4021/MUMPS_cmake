import os
from graphlib import TopologicalSorter


class DependencyGraph:
    def __init__(self, basedir : str):
        self.objects = list()
        self.dependencies = {}
        self.basedir = basedir
    
    def add_object(self, object : str):
        object = object.replace('$(ARITH)','${ARITH}')
        if object not in self.objects:
            self.objects.append(object)
        if object not in self.dependencies:
            self.dependencies[object] = list()
            filename = self.isfile(object)
            if filename is not None:
                self.add_dependency(object, filename)

    def add_dependency(self, object1 : str, object2 : str):
        object1 = object1.replace('$(ARITH)','${ARITH}')
        object2 = object2.replace('$(ARITH)','${ARITH}')
        self.add_object(object1)
        self.add_object(object2)
        if object1 == object2:
            return
        if object2 not in self.dependencies[object1]:
            self.dependencies[object1].append(object2)

    def isfile(self, name : str):
        if os.path.isfile(os.path.join(self.basedir, name.replace('${ARITH}','d'))):
            return  None
        if os.path.isfile(os.path.join(self.basedir, name.replace('${ARITH}','d').replace('.o','.c'))):
            return  name.replace('.o','.c')
        if os.path.isfile(os.path.join(self.basedir, name.replace('${ARITH}','d').replace('.o','.F'))):
            return  name.replace('.o','.F')
        return None
    
    def get_dependencies(self, object : str):
        obj = object.replace('$(ARITH)','${ARITH}')
        if obj not in self.dependencies:
            return []
        return self.dependencies[object.replace('$(ARITH)','${ARITH}')]

    def has_dependencies(self, object : str):
        return object in self.dependencies and len(self.dependencies[object]) > 0
    
    def has_dependencies_from_list(self, object: str, existing_objects : list[str], second_list : list[str] = []):
        for dep in self.dependencies[object]:
            if (dep.endswith('.o') or dep.endswith('.lib')) and dep not in existing_objects and dep not in second_list:
                return False
        return True
    
    def all_dependencies(self, object : str):
        return self.dependencies[object]
    
    def all_modules(self, object : str):
        retval = []
        for dep in self.dependencies[object]:
            if self.should_become_library(dep):
                retval.append(dep)
                tmp = self.all_modules(dep)
                for t in tmp:
                    if t not in retval:
                        retval.append(t)
        return retval

    def get_recursive_list(self) -> tuple[list[str], list[str]]:
        retval = []
        arch_list = []
        list_of_arch_independent_objects = []
        for object in self.objects:
            if '${ARITH}' not in object and self.has_dependencies(object):
                list_of_arch_independent_objects.append(object)
                
        while len(list_of_arch_independent_objects) > 0:
            obj = list_of_arch_independent_objects.pop()
            if self.has_dependencies_from_list(obj, retval):
                retval.append(obj)
            else:
                list_of_arch_independent_objects.insert(0, obj)
            
        list_of_objects = []
        for object in self.objects:
            if '${ARITH}' in object and self.has_dependencies(object):
                list_of_objects.append(object)

        while len(list_of_objects) > 0:
            obj = list_of_objects.pop()
            if self.has_dependencies_from_list(obj, arch_list, retval):
                arch_list.append(obj)
            else:
                list_of_objects.insert(0, obj)

        return (retval, arch_list)
    
    def sorted_objects(self):
        g_arith = {}
        g_common = {}
        for object in self.objects:
            if '${ARITH}' not in object and object not in g_common:
                g_common[object] = self.dependencies[object]
            elif '${ARITH}' in object and object not in g_arith:
                g_arith[object] = self.dependencies[object]
        tsc = TopologicalSorter(g_common)
        tsa = TopologicalSorter(g_arith)

        oc = tuple(tsc.static_order())
        oa = tuple(tsa.static_order())
        return (oc, oa)

    def should_become_library(self, object : str):
        return ('mumps_c.c' in self.dependencies[object]) or ((object.endswith('.o') or object.endswith('.lib')) and len(self.dependencies[object]) > 1)
    
    def all_file_dependencies(self, libname: str) -> list[str]:
        retval = []
        for dep in self.dependencies[libname]:
            if ('mumps_c.c' not in dep) and dep.endswith('.c') or dep.endswith('.F'):
                retval.append(dep)
            else:
                tmp = self.all_file_dependencies(dep)
                for t in tmp:
                    if t not in retval:
                        retval.append(t)
        return retval
    
    def has_dependents(self, object : str, discard_entries = None):
        for key in self.dependencies:
            if discard_entries is not None and discard_entries(key):
                continue
            if object in self.dependencies[key]:
                return True
        return False
    
    def is_fortran(self, object : str):
        isfortran = [f.endswith('.F') for f in self.dependencies[object]]
        return all(isfortran)