
add_library(mpiseq 
    elapse.c
    mpi.f
    mpic.c)
add_library(mumps::mpiseq ALIAS mpiseq)
target_include_directories(mpiseq PUBLIC 
                $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}>
                $<INSTALL_INTERFACE:${HEADER_INSTALL_DIR}/libseq>)
set_target_properties(pord PROPERTIES 
        POSITION_INDEPENDENT_CODE ON
        MSVC_RUNTIME_LIBRARY "MultiThreaded$<$<CONFIG:Debug>:Debug>")

file(GLOB HEADER_FILES "*.h")
install(FILES ${HEADER_FILES} DESTINATION ${HEADER_INSTALL_DIR}/libseq)