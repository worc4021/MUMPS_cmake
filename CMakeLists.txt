cmake_minimum_required(VERSION 3.15)
project(MUMPS Fortran C CXX)

# Obtain latest source by pulling the tar.gz from https://mumps-solver.org/MUMPS_{MUMPS VERSION currently 5.9.0}.tar.gz

include(SetupMumps.cmake)

include(GNUInstallDirs)
include(CMakePackageConfigHelpers)

option(USE_INT64 "Use 64-bit integers" OFF)
option(BUILD_MEX "Build MATLAB interface" ON)
option(MUMPS_BUILD_TESTS "Build tests" ON)

message(STATUS "CMAKE_PREFIX_PATH=${CMAKE_PREFIX_PATH}")
find_package(OpenBLAS REQUIRED)
find_package(METIS REQUIRED)
find_package(GKlib REQUIRED)
find_package(OpenMP REQUIRED)

set(CMAKE_POSITION_INDEPENDENT_CODE ON)
set(CMAKE_MSVC_RUNTIME_LIBRARY "MultiThreaded$<$<CONFIG:Debug>:Debug>")


include(FortranCInterface)
FortranCInterface_VERIFY()
if (FortranCInterface_GLOBAL_CASE STREQUAL "UPPER")
    set(F_SYMBOL "MUMPS_##upper_case")
    set(F_SYM_ARITH_S "SMUMPS_##upper_case")
    set(F_SYM_ARITH_D "DMUMPS_##upper_case")
    set(F_SYM_ARITH_Z "ZMUMPS_##upper_case")
    set(F_SYM_ARITH_C "CMUMPS_##upper_case")
else()
    set(F_SYMBOL "mumps_##lower_case")
    set(F_SYM_ARITH_D "dmumps_##lower_case")
    set(F_SYM_ARITH_S "smumps_##lower_case")
    set(F_SYM_ARITH_C "cmumps_##lower_case")
    set(F_SYM_ARITH_Z "zmumps_##lower_case")
endif(FortranCInterface_GLOBAL_CASE STREQUAL "UPPER")

if (NOT FortranCInterface_GLOBAL_SUFFIX STREQUAL "")
    set(F_SYMBOL "mumps_##lower_case##${FortranCInterface_GLOBAL_SUFFIX}")
    set(F_SYM_ARITH_S "smumps_##lower_case##${FortranCInterface_GLOBAL_SUFFIX}")
    set(F_SYM_ARITH_D "dmumps_##lower_case##${FortranCInterface_GLOBAL_SUFFIX}")
    set(F_SYM_ARITH_Z "zmumps_##lower_case##${FortranCInterface_GLOBAL_SUFFIX}")
    set(F_SYM_ARITH_C "cmumps_##lower_case##${FortranCInterface_GLOBAL_SUFFIX}")
endif()

if (NOT FortranCInterface_GLOBAL_PREFIX STREQUAL "")
    set(F_SYMBOL "#define F_SYMBOL(lower_case,upper_case) ${FortranCInterface_GLOBAL_PREFIX}##${F_SYMBOL}")
    set(F_SYM_ARITH_S "#define F_SYM_ARITH(lower_case,upper_case) ${FortranCInterface_GLOBAL_PREFIX}##${F_SYM_ARITH_S}")
    set(F_SYM_ARITH_D "#define F_SYM_ARITH(lower_case,upper_case) ${FortranCInterface_GLOBAL_PREFIX}##${F_SYM_ARITH_D}")
    set(F_SYM_ARITH_Z "#define F_SYM_ARITH(lower_case,upper_case) ${FortranCInterface_GLOBAL_PREFIX}##${F_SYM_ARITH_Z}")
    set(F_SYM_ARITH_C "#define F_SYM_ARITH(lower_case,upper_case) ${FortranCInterface_GLOBAL_PREFIX}##${F_SYM_ARITH_C}")
else()
    set(F_SYMBOL "#define F_SYMBOL(lower_case,upper_case) ${F_SYMBOL}")
    set(F_SYM_ARITH_S "#define F_SYM_ARITH(lower_case,upper_case) ${F_SYM_ARITH_S}")
    set(F_SYM_ARITH_D "#define F_SYM_ARITH(lower_case,upper_case) ${F_SYM_ARITH_D}")
    set(F_SYM_ARITH_Z "#define F_SYM_ARITH(lower_case,upper_case) ${F_SYM_ARITH_Z}")
    set(F_SYM_ARITH_C "#define F_SYM_ARITH(lower_case,upper_case) ${F_SYM_ARITH_C}")
endif()

configure_file(${CMAKE_CURRENT_SOURCE_DIR}/src/mumps_c.c.patch.in ${MUMPS_ROOT}/src/mumps_c.c.patch)
configure_file(${CMAKE_CURRENT_SOURCE_DIR}/src/mumps_common.h.patch.in ${MUMPS_ROOT}/src/mumps_common.h.patch)
configure_file(${CMAKE_CURRENT_SOURCE_DIR}/libseq/elapse.h.patch.in ${MUMPS_ROOT}/libseq/elapse.h.patch)

execute_process(COMMAND patch --no-backup-if-mismatch --input=${MUMPS_ROOT}/src/mumps_c.c.patch src/mumps_c.c WORKING_DIRECTORY ${MUMPS_ROOT})
execute_process(COMMAND patch --no-backup-if-mismatch --input=${MUMPS_ROOT}/src/mumps_common.h.patch src/mumps_common.h WORKING_DIRECTORY ${MUMPS_ROOT})
execute_process(COMMAND patch --no-backup-if-mismatch --input=${MUMPS_ROOT}/libseq/elapse.h.patch libseq/elapse.h WORKING_DIRECTORY ${MUMPS_ROOT})

if (USE_INT64)
    configure_file(${MUMPS_ROOT}/src/mumps_int_def64_h.in ${MUMPS_ROOT}/include/mumps_int_def.h COPYONLY)
else()
    configure_file(${MUMPS_ROOT}/src/mumps_int_def32_h.in ${MUMPS_ROOT}/include/mumps_int_def.h COPYONLY)
endif()

if (CMAKE_Fortran_COMPILER_ID MATCHES "GNU")
    set(CMAKE_Fortran_FLAGS "${CMAKE_Fortran_FLAGS} -fallow-argument-mismatch")
endif()

set(MUMPS_INCLUDEDIR ${MUMPS_ROOT}/include)

set(ARCHS)
list(APPEND ARCHS "d" "s" "c" "z")


add_subdirectory(PORD)
add_subdirectory(libseq)
add_subdirectory(src)
if (MUMPS_BUILD_TESTS)
    enable_testing()
    include(CTest)
    add_subdirectory(examples)
endif()


foreach(ARITH ${ARCHS})
    target_sources(lib${ARITH}mumps PUBLIC 
        FILE_SET HEADERS
        BASE_DIRS ${MUMPS_INCLUDEDIR}
        FILES
            ${MUMPS_INCLUDEDIR}/${ARITH}mumps_c.h
            ${MUMPS_INCLUDEDIR}/${ARITH}mumps_struc.h
            ${MUMPS_INCLUDEDIR}/mumps_compat.h
            ${MUMPS_INCLUDEDIR}/mumps_int_def.h
    )
endforeach(ARITH ${ARCHS})


configure_package_config_file(mumpsConfig.cmake.in
  ${CMAKE_CURRENT_BINARY_DIR}/mumpsConfig.cmake
  INSTALL_DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/mumps)

install(TARGETS libdmumps libcmumps libsmumps libzmumps pord mpiseq libmumps_common
      EXPORT mumpsTargets
      LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
      ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
      RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
      FILE_SET HEADERS)

install(EXPORT mumpsTargets
      FILE mumpsTargets.cmake
      NAMESPACE mumps::
      DESTINATION  ${CMAKE_INSTALL_LIBDIR}/cmake/mumps)

install(FILES ${CMAKE_CURRENT_BINARY_DIR}/mumpsConfig.cmake
      DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/mumps )