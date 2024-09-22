import os
from stringtemplate3.groups import StringTemplateGroup as STG
from stringtemplate3.templates import StringTemplate as ST
from DependencyGraph import DependencyGraph
from textwrap import dedent

class Templater:
    def __init__(self, dg : DependencyGraph):
        self.dg = dg
        with open(os.path.join(os.path.dirname(__file__), "cmake.stg"), "r") as f:
            self.group = STG(file=f, lexer="angle-bracket", lineSeparator="\n")
        # self.group = STG(name='cmake', lexer='angle-bracket', lineSeparator='\n')
        
        # self.group.defineTemplate(name='target_object',template=r'$\<TARGET_OBJECTS:<x>\>')
        # self.group.defineTemplate(name='object_include',template=r'${CMAKE_CURRENT_BINARY_DIR}/<object>')

        template = dedent("""\
        add_library(<name> OBJECT <sources; separator=" ">)
        set_target_properties(<name> PROPERTIES Fortran_MODULE_DIRECTORY <name:object_include()>)
        target_include_directories(<name> PUBLIC <name:object_include()> <module_includes:object_include(); separator=" "> ${MUMPS_INCLUDEDIR})
        <if(objects)>target_link_libraries(<name> PUBLIC <objects:target_object(); separator=" ">)<endif>
        """)
        self.group.defineTemplate(name='add_obj_library',template=template)

        template = dedent("""\
        add_library(<name> STATIC <sources; separator=" ">)
        set_target_properties(<name> PROPERTIES Fortran_MODULE_DIRECTORY <name:object_include()>)
        target_include_directories(<name> PUBLIC <name:object_include()> <module_includes:object_include(); separator=" "> ${MUMPS_INCLUDEDIR})
        <if(objects)>target_link_libraries(<name> PUBLIC <objects:target_object(); separator=" "> <libs; separator=" ">)<endif>
        """)
        self.group.defineTemplate(name='add_library',template=template)

        template = dedent("""\
        foreach(ARITH ${ARCHS})
            <libraries; separator="\n">
            target_compile_definitions(${ARITH}mumps_c PRIVATE MUMPS_ARITH=MUMPS_ARITH_${ARITH})
        endforeach(ARITH ${ARCHS})
        """)
        self.group.defineTemplate(name='foreach',template=template)

        template = dedent("""\
        foreach(ARITH ${ARCHS})
            <libraries; separator="\n">
        endforeach(ARITH ${ARCHS})
        """)
        self.group.defineTemplate(name='foreach_flat',template=template)

        template = dedent("""\
        add_library(<name> STATIC <sources; separator=" ">)
        set_target_properties(<name> PROPERTIES Fortran_MODULE_DIRECTORY <name:object_include()>)
        target_include_directories(<name> PUBLIC $\\<BUILD_INTERFACE:${MUMPS_INCLUDEDIR}\\> $\\<INSTALL_INTERFACE:${HEADER_INSTALL_DIR}\\>)
        target_compile_definitions(<name> PRIVATE metis pord GEMMT_AVAILABLE)
        target_link_libraries(<name> PUBLIC pord metis::metis mpiseq MKL::MKL <objects:target_object(); separator=" "> <libs; separator=" ">)
        """)
        self.group.defineTemplate(name='add_flat_library',template=template)

    def object_library(self, object) -> str:
        st = self.group.getInstanceOf("add_obj_library")
        all_deps = self.dg.all_dependencies(object)
        filesources = []
        objectsources = []
        for deps in all_deps:
            if deps.endswith('.o') or deps.endswith('.lib'):
                if self.dg.should_become_library(deps):
                    objectsources.append(deps.replace('.o',''))
                else:
                    filesources.append(self.dg.all_dependencies(deps)[0])
            else:
                filesources.append(deps)
        st["name"] = object.replace('.o','').replace('.lib','')
        st["sources"] = filesources
        if len(objectsources) > 0:
            st["objects"] = objectsources
            st["module_includes"] = [x.replace('.o','') for x in  self.dg.all_modules(object)]
        return st.toString()
    
    def static_library(self, object) -> str:
        st = self.group.getInstanceOf("add_library")
        all_deps = self.dg.all_dependencies(object)
        filesources = []
        objectsources = []
        libs = []
        for deps in all_deps:
            if deps.endswith('.o') or deps.endswith('.lib'):
                if deps.endswith('.lib'):
                    libs.append('lib' + deps.replace('.lib',''))
                elif self.dg.should_become_library(deps):
                    objectsources.append(deps.replace('.o',''))
                else:
                    filesources.append(self.dg.all_dependencies(deps)[0])
            else:
                filesources.append(deps)
        st["name"] = 'lib'+object.replace('.o','').replace('.lib','')
        st["sources"] = filesources
        if len(objectsources) > 0:
            st["objects"] = objectsources
            st["module_includes"] = [x.replace('.o','') for x in  self.dg.all_modules(object)]
        if len(libs) > 0:
            st["libs"] = libs
        return st.toString()
    
    def process_all(self) -> str:
        (rl,rla) = self.dg.get_recursive_list()
        res = ""

        for obj in rl:
            if self.dg.should_become_library(obj):
                if obj.endswith('.o'):
                    res += self.object_library(obj) + "\n"
                else:
                    res += self.static_library(obj) + "\n"

        arith_list = []
        for obj in rla:
            if 'mumps_c' in obj or self.dg.should_become_library(obj):
                if obj.endswith('.o'):
                    arith_list.append(self.object_library(obj))
                else:
                    arith_list.append(self.static_library(obj))                    
        st = self.group.getInstanceOf("foreach")
        st["libraries"] = arith_list

        res += st.toString()

        return res
    

    def flat_libraries(self, lib :str) -> str:
        
        special = dedent("""\
        add_library(${ARITH}mumps_c OBJECT mumps_c.c)
        target_include_directories(${ARITH}mumps_c PUBLIC ${MUMPS_INCLUDEDIR})
        target_compile_definitions(${ARITH}mumps_c PRIVATE MUMPS_ARITH=MUMPS_ARITH_${ARITH})
        """)
        
        
        st = self.group.getInstanceOf("add_flat_library")
        st["name"] = lib.replace('.lib','')
        st["sources"] = self.dg.all_file_dependencies(lib)
        st["objects"] = ['${ARITH}mumps_c']
    
        
        stfe = self.group.getInstanceOf("foreach_flat")
        stfe["libraries"] = [special, st.toString() + "\n"]
        
        return stfe.toString()