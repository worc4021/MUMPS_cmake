add_library(pord 
    lib/graph.c 
    lib/gbipart.c 
    lib/gbisect.c 
    lib/ddcreate.c 
    lib/ddbisect.c 
    lib/nestdiss.c
    lib/multisector.c 
    lib/gelim.c 
    lib/bucket.c 
    lib/tree.c 
    lib/symbfac.c 
    lib/interface.c 
    lib/sort.c 
    lib/minpriority.c)
add_library(mumps::pord ALIAS pord)
target_include_directories(pord PUBLIC 
                            $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
                            $<INSTALL_INTERFACE:${HEADER_INSTALL_DIR}/pord>)

set_target_properties(pord PROPERTIES 
        POSITION_INDEPENDENT_CODE ON
        MSVC_RUNTIME_LIBRARY "MultiThreaded$<$<CONFIG:Debug>:Debug>")
target_compile_definitions(pord PUBLIC PORD_INTSIZE64)

file(GLOB HEADER_FILES "include/*.h")
install(FILES ${HEADER_FILES} DESTINATION ${HEADER_INSTALL_DIR}/pord)