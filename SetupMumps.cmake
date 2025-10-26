if (NOT DEFINED MUMPS_VERSION)
set(MUMPS_VERSION "5.8.1")
endif()

if(WIN32)
set(VENV_PYTHONDIR "Scripts")
else()
set(VENV_PYTHONDIR "bin")
endif()

if (NOT IS_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}/.venv")
    find_package(Python3 REQUIRED COMPONENTS Interpreter)
    message(STATUS "Using local virtual environment")
    execute_process(
        COMMAND ${Python3_EXECUTABLE} -m venv ${CMAKE_CURRENT_SOURCE_DIR}/.venv
        COMMAND_ECHO STDOUT)
    
    execute_process(
        COMMAND ${CMAKE_CURRENT_SOURCE_DIR}/.venv/${VENV_PYTHONDIR}/python -m pip install -r ${CMAKE_CURRENT_SOURCE_DIR}/buildutilities/requirements.txt
        COMMAND_ECHO STDOUT)
endif()

message(STATUS "Configuring MUMPS version ${MUMPS_VERSION}")
set(PYTHONEXE "${CMAKE_CURRENT_SOURCE_DIR}/.venv/${VENV_PYTHONDIR}/python")
execute_process(COMMAND ${PYTHONEXE} ${CMAKE_CURRENT_SOURCE_DIR}/buildutilities/Driver.py ${MUMPS_VERSION} --output ${CMAKE_CURRENT_BINARY_DIR}
        COMMAND_ECHO STDOUT
        ERROR_VARIABLE error_output
        RESULT_VARIABLE res)

if (NOT res EQUAL 0)
    message(FATAL_ERROR "Error configuring MUMPS: ${error_output}") 
endif()    

set(MUMPS_ROOT "${CMAKE_CURRENT_BINARY_DIR}/MUMPS_${MUMPS_VERSION}")