add_library(pord 
    ${MUMPS_ROOT}/PORD/lib/graph.c 
    ${MUMPS_ROOT}/PORD/lib/gbipart.c 
    ${MUMPS_ROOT}/PORD/lib/gbisect.c 
    ${MUMPS_ROOT}/PORD/lib/ddcreate.c 
    ${MUMPS_ROOT}/PORD/lib/ddbisect.c 
    ${MUMPS_ROOT}/PORD/lib/nestdiss.c
    ${MUMPS_ROOT}/PORD/lib/multisector.c 
    ${MUMPS_ROOT}/PORD/lib/gelim.c 
    ${MUMPS_ROOT}/PORD/lib/bucket.c 
    ${MUMPS_ROOT}/PORD/lib/tree.c 
    ${MUMPS_ROOT}/PORD/lib/symbfac.c 
    ${MUMPS_ROOT}/PORD/lib/interface.c 
    ${MUMPS_ROOT}/PORD/lib/sort.c 
    ${MUMPS_ROOT}/PORD/lib/minpriority.c)
add_library(mumps::pord ALIAS pord)

file(GLOB HEADER_FILES "${MUMPS_ROOT}/PORD/include/*.h")

target_sources(pord PUBLIC
                  FILE_SET HEADERS
                  BASE_DIRS ${MUMPS_ROOT}/PORD/include
                  FILES ${HEADER_FILES})

target_compile_definitions(pord PUBLIC PORD_INTSIZE64)
