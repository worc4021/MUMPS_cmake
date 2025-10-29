foreach(ARITH ${ARCHS})
    add_executable(${ARITH}simpletest ${MUMPS_ROOT}/examples/${ARITH}simpletest.F)
    target_link_libraries(${ARITH}simpletest PRIVATE lib${ARITH}mumps)

    add_executable(${ARITH}simpletest_save_restore ${MUMPS_ROOT}/examples/${ARITH}simpletest_save_restore.F)
    target_link_libraries(${ARITH}simpletest_save_restore PRIVATE lib${ARITH}mumps)
endforeach()


add_executable(c_example_save_restore ${MUMPS_ROOT}/examples/c_example_save_restore.c)
target_link_libraries(c_example_save_restore PRIVATE libdmumps)


add_executable(multiple_arithmetics_example ${MUMPS_ROOT}/examples/multiple_arithmetics_example.F)
target_link_libraries(multiple_arithmetics_example PRIVATE libdmumps libcmumps libsmumps libzmumps)


add_executable(c_example ${MUMPS_ROOT}/examples/c_example.c)
target_link_libraries(c_example PRIVATE libdmumps)


include(FortranCInterface)
FortranCInterface_HEADER(${MUMPS_ROOT}/examples/FCMangle.h
                            MACRO_NAMESPACE "FC_"
                            SYMBOL_NAMESPACE "FC_")

enable_testing()
include(CTest)

add_test(NAME c_example_save_restore_exe COMMAND $<TARGET_FILE:c_example_save_restore>)
add_test(NAME c_example_exe COMMAND $<TARGET_FILE:c_example>)
add_test(NAME multiple_arithmetics_example_exe COMMAND $<TARGET_FILE:multiple_arithmetics_example>)