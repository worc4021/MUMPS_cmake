foreach(ARITH ${ARCHS})
    add_executable(${ARITH}simpletest ${ARITH}simpletest.F)
    target_link_libraries(${ARITH}simpletest PRIVATE lib${ARITH}mumps)

    add_executable(${ARITH}simpletest_save_restore ${ARITH}simpletest_save_restore.F)
    target_link_libraries(${ARITH}simpletest_save_restore PRIVATE lib${ARITH}mumps)
endforeach()


add_executable(c_example_save_restore c_example_save_restore.c)
target_link_libraries(c_example_save_restore PRIVATE libdmumps)


add_executable(multiple_arithmetics_example multiple_arithmetics_example.F)
target_link_libraries(multiple_arithmetics_example PRIVATE libdmumps libcmumps libsmumps libzmumps)


add_executable(c_example c_example.c)
target_link_libraries(c_example PRIVATE libdmumps)


include(FortranCInterface)
FortranCInterface_HEADER(${CMAKE_CURRENT_SOURCE_DIR}/FCMangle.h
                            MACRO_NAMESPACE "FC_"
                            SYMBOL_NAMESPACE "FC_")

include(CTest)
# include(FetchContent)
# FetchContent_Declare(
#   googletest
#   URL https://github.com/google/googletest/archive/03597a01ee50ed33e9dfd640b249b4be3799d395.zip
# )
# # For Windows: Prevent overriding the parent project's compiler/linker settings
# set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
# FetchContent_MakeAvailable(googletest)
# include(GoogleTest)
# add_executable(cpp_example cpp_example.cpp)
# target_link_libraries(cpp_example PRIVATE libdmumps GTest::gtest)
# target_include_directories(cpp_example PRIVATE ${MUMPS_INCLUDEDIR})
# gtest_add_tests(cpp_example "" AUTO)


add_test(NAME c_example_save_restore_exe COMMAND c_example_save_restore)
add_test(NAME c_example_exe COMMAND c_example)
add_test(NAME multiple_arithmetics_example_exe COMMAND multiple_arithmetics_example)