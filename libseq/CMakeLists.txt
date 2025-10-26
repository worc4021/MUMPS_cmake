
add_library(mpiseq 
    ${MUMPS_ROOT}/libseq/elapse.c
    ${MUMPS_ROOT}/libseq/mpi.f
    ${MUMPS_ROOT}/libseq/mpic.c)
add_library(mumps::mpiseq ALIAS mpiseq)
file(GLOB HEADER_FILES "${MUMPS_ROOT}/libseq/*.h")
target_sources(mpiseq PUBLIC
                    FILE_SET HEADERS
                    BASE_DIRS ${MUMPS_ROOT}/libseq
                    FILES ${HEADER_FILES})
