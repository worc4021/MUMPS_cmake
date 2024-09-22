foreach(ARITH ${ARCHS})
    add_executable(${ARITH}simpletest ${ARITH}simpletest.f)
    target_link_libraries(${ARITH}simpletest PRIVATE ${ARITH}mumps)
    target_include_directories(${ARITH}simpletest PRIVATE ${MUMPS_INCLUDEDIR})

    add_executable(${ARITH}simpletest_save_restore ${ARITH}simpletest_save_restore.f)
    target_link_libraries(${ARITH}simpletest_save_restore PRIVATE ${ARITH}mumps)
    target_include_directories(${ARITH}simpletest_save_restore PRIVATE ${MUMPS_INCLUDEDIR})
endforeach()


add_executable(c_example_save_restore c_example_save_restore.c)
target_link_libraries(c_example_save_restore PRIVATE dmumps)
target_include_directories(c_example_save_restore PRIVATE ${MUMPS_INCLUDEDIR})

add_executable(multiple_arithmetics_example multiple_arithmetics_example.f)
target_link_libraries(multiple_arithmetics_example PRIVATE dmumps cmumps smumps zmumps)
target_include_directories(multiple_arithmetics_example PRIVATE ${MUMPS_INCLUDEDIR})

add_executable(c_example c_example.c)
target_link_libraries(c_example PRIVATE dmumps)
target_include_directories(c_example PRIVATE ${MUMPS_INCLUDEDIR})