cmake_minimum_required(VERSION 3.5)
project(MUMPS Fortran C CXX)

# Obtain latest source by pulling the tar.gz from https://mumps-solver.org/MUMPS_{MUMPS VERSION currently 5.7.3}.tar.gz

include(GNUInstallDirs)
option(USE_INT64 "Use 64-bit integers" OFF)
option(BUILD_MEX "Build MATLAB interface" ON)

include($ENV{CMAKE_INSTALL_PREFIX}/cmake/GKlibTargets.cmake)
include($ENV{CMAKE_INSTALL_PREFIX}/cmake/metisTargets.cmake)

# As specified in INSTALL file, all external dependencies should use 64 bit integers. The mkl provides interfaces with 64 ilp64 and 32 lp64
set(MKL_LINK static)
set(MKL_THREADING intel_thread)
set(MKL_INTERFACE lp64)
find_package(MKL REQUIRED)

include(FortranCInterface)
FortranCInterface_VERIFY()
if (FortranCInterface_GLOBAL_CASE STREQUAL "UPPER")
    set(F_SYMBOL "#define F_SYMBOL(lower_case,upper_case) ${FortranCInterface_GLOBAL_PREFIX}##MUMPS_##upper_case##${FortranCInterface_GLOBAL_SUFFIX}")
    set(F_SYM_ARITH_D "#define F_SYM_ARITH(lower_case,upper_case) ${FortranCInterface_GLOBAL_PREFIX}##DMUMPS_##upper_case##${FortranCInterface_GLOBAL_SUFFIX}")
    set(F_SYM_ARITH_S "#define F_SYM_ARITH(lower_case,upper_case) ${FortranCInterface_GLOBAL_PREFIX}##SMUMPS_##upper_case##${FortranCInterface_GLOBAL_SUFFIX}")
    set(F_SYM_ARITH_C "#define F_SYM_ARITH(lower_case,upper_case) ${FortranCInterface_GLOBAL_PREFIX}##CMUMPS_##upper_case##${FortranCInterface_GLOBAL_SUFFIX}")
    set(F_SYM_ARITH_Z "#define F_SYM_ARITH(lower_case,upper_case) ${FortranCInterface_GLOBAL_PREFIX}##ZMUMPS_##upper_case##${FortranCInterface_GLOBAL_SUFFIX}")
else()
    set(F_SYMBOL "#define F_SYMBOL(lower_case,upper_case) ${FortranCInterface_GLOBAL_PREFIX}##mumps_##lower_case##${FortranCInterface_GLOBAL_SUFFIX}")
    set(F_SYM_ARITH_D "#define F_SYM_ARITH(lower_case,upper_case) ${FortranCInterface_GLOBAL_PREFIX}##dmumps_##lower_case##${FortranCInterface_GLOBAL_SUFFIX}")
    set(F_SYM_ARITH_S "#define F_SYM_ARITH(lower_case,upper_case) ${FortranCInterface_GLOBAL_PREFIX}##smumps_##lower_case##${FortranCInterface_GLOBAL_SUFFIX}")
    set(F_SYM_ARITH_C "#define F_SYM_ARITH(lower_case,upper_case) ${FortranCInterface_GLOBAL_PREFIX}##cmumps_##lower_case##${FortranCInterface_GLOBAL_SUFFIX}")
    set(F_SYM_ARITH_Z "#define F_SYM_ARITH(lower_case,upper_case) ${FortranCInterface_GLOBAL_PREFIX}##zmumps_##lower_case##${FortranCInterface_GLOBAL_SUFFIX}")
endif(FortranCInterface_GLOBAL_CASE STREQUAL "UPPER")

message(STATUS "Add to src/mumps_common.h: ")
message(STATUS "${F_SYMBOL}")
message(STATUS "Add to src/mumps_c.c: ")
message(STATUS "${F_SYM_ARITH_D}")
message(STATUS "${F_SYM_ARITH_S}")
message(STATUS "${F_SYM_ARITH_C}")
message(STATUS "${F_SYM_ARITH_Z}")

if (USE_INT64)
    configure_file(${CMAKE_CURRENT_SOURCE_DIR}/src/mumps_int_def64_h.in ${CMAKE_CURRENT_SOURCE_DIR}/include/mumps_int_def.h COPYONLY)
else()
    configure_file(${CMAKE_CURRENT_SOURCE_DIR}/src/mumps_int_def32_h.in ${CMAKE_CURRENT_SOURCE_DIR}/include/mumps_int_def.h COPYONLY)
endif()

if (CMAKE_Fortran_COMPILER_ID MATCHES "GNU")
    set(CMAKE_Fortran_FLAGS "${CMAKE_Fortran_FLAGS} -fallow-argument-mismatch")
endif()

set(MUMPS_INCLUDEDIR ${CMAKE_CURRENT_SOURCE_DIR}/include)

set(ARCHS)
list(APPEND ARCHS "d" "s" "c" "z")

set(HEADER_INSTALL_DIR ${CMAKE_INSTALL_INCLUDEDIR}/mumps)

enable_testing()

add_subdirectory(PORD)
add_subdirectory(libseq)
add_subdirectory(src)
add_subdirectory(examples)
# if (BUILD_MEX)
#     add_subdirectory(MATLAB)
# endif()


install(TARGETS libdmumps libcmumps libsmumps libzmumps pord mpiseq libmumps_common
      EXPORT mumpsTargets
      LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
      ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
      RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR})
file(GLOB HEADER_FILES "include/*.h")
install(FILES ${HEADER_FILES} DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}/mumps)
install(EXPORT mumpsTargets
      FILE mumpsTargets.cmake
      NAMESPACE mumps::
      DESTINATION cmake)