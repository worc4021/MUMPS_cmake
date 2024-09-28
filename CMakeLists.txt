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


if (USE_INT64)
    configure_file(${CMAKE_CURRENT_SOURCE_DIR}/src/mumps_int_def64_h.in ${CMAKE_CURRENT_SOURCE_DIR}/include/mumps_int_def.h COPYONLY)
else()
    configure_file(${CMAKE_CURRENT_SOURCE_DIR}/src/mumps_int_def32_h.in ${CMAKE_CURRENT_SOURCE_DIR}/include/mumps_int_def.h COPYONLY)
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
if (BUILD_MEX)
    add_subdirectory(MATLAB)
endif()


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