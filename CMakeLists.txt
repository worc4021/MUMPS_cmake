cmake_minimum_required(VERSION 3.15)
project(MUMPS Fortran C CXX)

# Obtain latest source by pulling the tar.gz from https://mumps-solver.org/MUMPS_{MUMPS VERSION currently 5.7.3}.tar.gz

include(SetupMumps.cmake)

include(GNUInstallDirs)
option(USE_INT64 "Use 64-bit integers" OFF)
option(BUILD_MEX "Build MATLAB interface" ON)

include(FetchContent)
FetchContent_Declare(
  metisdep
  GIT_REPOSITORY https://github.com/worc4021/METIS.git
  GIT_TAG        master
  EXCLUDE_FROM_ALL
)
FetchContent_MakeAvailable(metisdep)

set(CMAKE_POSITION_INDEPENDENT_CODE ON)
set(CMAKE_MSVC_RUNTIME_LIBRARY "MultiThreaded$<$<CONFIG:Debug>:Debug>")

# As specified in INSTALL file, all external dependencies should use 64 bit integers. The mkl provides interfaces with 64 ilp64 and 32 lp64
set(MKL_LINK static)
set(MKL_THREADING sequential)
set(MKL_INTERFACE lp64)
find_package(MKL REQUIRED)

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

execute_process(COMMAND patch --no-backup-if-mismatch --input=src/mumps_c.c.patch src/mumps_c.c WORKING_DIRECTORY ${MUMPS_ROOT})
execute_process(COMMAND patch --no-backup-if-mismatch --input=src/mumps_common.h.patch src/mumps_common.h WORKING_DIRECTORY ${MUMPS_ROOT})
execute_process(COMMAND patch --no-backup-if-mismatch --input=libseq/elapse.h.patch libseq/elapse.h WORKING_DIRECTORY ${MUMPS_ROOT})

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

enable_testing()

add_subdirectory(PORD)
add_subdirectory(libseq)
add_subdirectory(src)
add_subdirectory(examples)
# # if (BUILD_MEX)
# #     add_subdirectory(MATLAB)
# # endif()

install(TARGETS libdmumps libcmumps libsmumps libzmumps pord mpiseq libmumps_common
      EXPORT mumpsTargets
      LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}/${CMAKE_BUILD_TYPE}
      ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}/${CMAKE_BUILD_TYPE}
      RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}/${CMAKE_BUILD_TYPE}
      FILE_SET HEADERS)

# file(GLOB HEADER_FILES "${MUMPS_ROOT}/include/*.h")
# install(FILES ${HEADER_FILES} DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}/mumps)
install(EXPORT mumpsTargets
      FILE mumpsTargets.cmake
      NAMESPACE mumps::
      DESTINATION cmake)