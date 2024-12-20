
add_library(mpiseq 
    elapse.c
    mpi.f
    mpic.c)
add_library(mumps::mpiseq ALIAS mpiseq)
file(GLOB HEADER_FILES "*.h")
target_sources(mpiseq PUBLIC
                  FILE_SET HEADERS
                  FILES ${HEADER_FILES})

set_target_properties(pord PROPERTIES 
        POSITION_INDEPENDENT_CODE ON
        MSVC_RUNTIME_LIBRARY "MultiThreaded$<$<CONFIG:Debug>:Debug>")
