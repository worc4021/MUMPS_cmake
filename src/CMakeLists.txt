file(GLOB HEADER_FILES "${MUMPS_INCLUDEDIR}/*.h")
add_library(ana_orderings_wrappers_m OBJECT ${MUMPS_ROOT}/src/ana_orderings_wrappers_m.F)
target_sources(ana_orderings_wrappers_m PUBLIC
          FILE_SET HEADERS
          BASE_DIRS ${MUMPS_INCLUDEDIR}
          FILES ${HEADER_FILES})
target_include_directories(ana_orderings_wrappers_m PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
set_target_properties(ana_orderings_wrappers_m PROPERTIES 
    Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
    LINKER_LANGUAGE C)
target_link_libraries(ana_orderings_wrappers_m PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     

add_library(ana_blk_m OBJECT ${MUMPS_ROOT}/src/ana_blk_m.F)
target_sources(ana_blk_m PUBLIC
          FILE_SET HEADERS
          BASE_DIRS ${MUMPS_INCLUDEDIR}
          FILES ${HEADER_FILES})
target_include_directories(ana_blk_m PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
set_target_properties(ana_blk_m PROPERTIES 
    Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
    LINKER_LANGUAGE C)
target_link_libraries(ana_blk_m PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     

add_library(mumps_memory_mod OBJECT ${MUMPS_ROOT}/src/mumps_memory_mod.F)
target_sources(mumps_memory_mod PUBLIC
          FILE_SET HEADERS
          BASE_DIRS ${MUMPS_INCLUDEDIR}
          FILES ${HEADER_FILES})
target_include_directories(mumps_memory_mod PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
set_target_properties(mumps_memory_mod PROPERTIES 
    Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
    LINKER_LANGUAGE C)
target_link_libraries(mumps_memory_mod PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     

add_library(tools_common_m OBJECT ${MUMPS_ROOT}/src/tools_common_m.F)
target_sources(tools_common_m PUBLIC
          FILE_SET HEADERS
          BASE_DIRS ${MUMPS_INCLUDEDIR}
          FILES ${HEADER_FILES})
target_include_directories(tools_common_m PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
set_target_properties(tools_common_m PROPERTIES 
    Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
    LINKER_LANGUAGE C)
target_link_libraries(tools_common_m PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     

add_library(lr_common OBJECT ${MUMPS_ROOT}/src/lr_common.F)
target_sources(lr_common PUBLIC
          FILE_SET HEADERS
          BASE_DIRS ${MUMPS_INCLUDEDIR}
          FILES ${HEADER_FILES})
target_include_directories(lr_common PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
set_target_properties(lr_common PROPERTIES 
    Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
    LINKER_LANGUAGE C)
target_link_libraries(lr_common PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     

add_library(omp_tps_common_m OBJECT ${MUMPS_ROOT}/src/omp_tps_common_m.F)
target_sources(omp_tps_common_m PUBLIC
          FILE_SET HEADERS
          BASE_DIRS ${MUMPS_INCLUDEDIR}
          FILES ${HEADER_FILES})
target_include_directories(omp_tps_common_m PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
set_target_properties(omp_tps_common_m PROPERTIES 
    Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
    LINKER_LANGUAGE C)
target_link_libraries(omp_tps_common_m PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     

add_library(mumps_comm_buffer_common OBJECT ${MUMPS_ROOT}/src/mumps_comm_buffer_common.F)
target_sources(mumps_comm_buffer_common PUBLIC
          FILE_SET HEADERS
          BASE_DIRS ${MUMPS_INCLUDEDIR}
          FILES ${HEADER_FILES})
target_include_directories(mumps_comm_buffer_common PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
set_target_properties(mumps_comm_buffer_common PROPERTIES 
    Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
    LINKER_LANGUAGE C)
target_link_libraries(mumps_comm_buffer_common PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     

add_library(mumps_intr_types_common OBJECT ${MUMPS_ROOT}/src/mumps_intr_types_common.F)
target_sources(mumps_intr_types_common PUBLIC
          FILE_SET HEADERS
          BASE_DIRS ${MUMPS_INCLUDEDIR}
          FILES ${HEADER_FILES})
target_include_directories(mumps_intr_types_common PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
set_target_properties(mumps_intr_types_common PROPERTIES 
    Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
    LINKER_LANGUAGE C)
target_link_libraries(mumps_intr_types_common PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     

add_library(mumps_ooc_common OBJECT ${MUMPS_ROOT}/src/mumps_ooc_common.F)
target_sources(mumps_ooc_common PUBLIC
          FILE_SET HEADERS
          BASE_DIRS ${MUMPS_INCLUDEDIR}
          FILES ${HEADER_FILES})
target_include_directories(mumps_ooc_common PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
set_target_properties(mumps_ooc_common PROPERTIES 
    Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
    LINKER_LANGUAGE C)
target_link_libraries(mumps_ooc_common PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     

add_library(mumps_l0_omp_m OBJECT ${MUMPS_ROOT}/src/mumps_l0_omp_m.F)
target_sources(mumps_l0_omp_m PUBLIC
          FILE_SET HEADERS
          BASE_DIRS ${MUMPS_INCLUDEDIR}
          FILES ${HEADER_FILES})
target_include_directories(mumps_l0_omp_m PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
set_target_properties(mumps_l0_omp_m PROPERTIES 
    Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
    LINKER_LANGUAGE C)
target_link_libraries(mumps_l0_omp_m PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     

add_library(mumps_pivnul_mod OBJECT ${MUMPS_ROOT}/src/mumps_pivnul_mod.F)
target_sources(mumps_pivnul_mod PUBLIC
          FILE_SET HEADERS
          BASE_DIRS ${MUMPS_INCLUDEDIR}
          FILES ${HEADER_FILES})
target_include_directories(mumps_pivnul_mod PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
set_target_properties(mumps_pivnul_mod PROPERTIES 
    Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
    LINKER_LANGUAGE C)
target_link_libraries(mumps_pivnul_mod PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     

add_library(front_data_mgt_m OBJECT ${MUMPS_ROOT}/src/front_data_mgt_m.F)
target_sources(front_data_mgt_m PUBLIC
          FILE_SET HEADERS
          BASE_DIRS ${MUMPS_INCLUDEDIR}
          FILES ${HEADER_FILES})
target_include_directories(front_data_mgt_m PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
set_target_properties(front_data_mgt_m PROPERTIES 
    Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
    LINKER_LANGUAGE C)
target_link_libraries(front_data_mgt_m PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     

add_library(mumps_mpitoomp_m OBJECT ${MUMPS_ROOT}/src/mumps_mpitoomp_m.F)
target_sources(mumps_mpitoomp_m PUBLIC
          FILE_SET HEADERS
          BASE_DIRS ${MUMPS_INCLUDEDIR}
          FILES ${HEADER_FILES})
target_include_directories(mumps_mpitoomp_m PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
set_target_properties(mumps_mpitoomp_m PROPERTIES 
    Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
    LINKER_LANGUAGE C)
target_link_libraries(mumps_mpitoomp_m PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     

add_library(sol_omp_common_m OBJECT ${MUMPS_ROOT}/src/sol_omp_common_m.F)
target_sources(sol_omp_common_m PUBLIC
          FILE_SET HEADERS
          BASE_DIRS ${MUMPS_INCLUDEDIR}
          FILES ${HEADER_FILES})
target_include_directories(sol_omp_common_m PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
set_target_properties(sol_omp_common_m PROPERTIES 
    Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
    LINKER_LANGUAGE C)
target_link_libraries(sol_omp_common_m PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     

add_library(double_linked_list OBJECT ${MUMPS_ROOT}/src/double_linked_list.F)
target_sources(double_linked_list PUBLIC
          FILE_SET HEADERS
          BASE_DIRS ${MUMPS_INCLUDEDIR}
          FILES ${HEADER_FILES})
target_include_directories(double_linked_list PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
set_target_properties(double_linked_list PROPERTIES 
    Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
    LINKER_LANGUAGE C)
target_link_libraries(double_linked_list PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     

add_library(fac_future_niv2_mod OBJECT ${MUMPS_ROOT}/src/fac_future_niv2_mod.F)
target_sources(fac_future_niv2_mod PUBLIC
          FILE_SET HEADERS
          BASE_DIRS ${MUMPS_INCLUDEDIR}
          FILES ${HEADER_FILES})
target_include_directories(fac_future_niv2_mod PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
set_target_properties(fac_future_niv2_mod PROPERTIES 
    Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
    LINKER_LANGUAGE C)
target_link_libraries(fac_future_niv2_mod PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     

add_library(mumps_addr OBJECT ${MUMPS_ROOT}/src/mumps_addr.c)
target_sources(mumps_addr PUBLIC
          FILE_SET HEADERS
          BASE_DIRS ${MUMPS_INCLUDEDIR}
          FILES ${HEADER_FILES})
target_include_directories(mumps_addr PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
set_target_properties(mumps_addr PROPERTIES 
    Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
    LINKER_LANGUAGE C)
target_link_libraries(mumps_addr PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     

add_library(mumps_common OBJECT ${MUMPS_ROOT}/src/mumps_common.c)
target_sources(mumps_common PUBLIC
          FILE_SET HEADERS
          BASE_DIRS ${MUMPS_INCLUDEDIR}
          FILES ${HEADER_FILES})
target_include_directories(mumps_common PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
set_target_properties(mumps_common PROPERTIES 
    Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
    LINKER_LANGUAGE C)
target_link_libraries(mumps_common PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     

add_library(mumps_config_file_C OBJECT ${MUMPS_ROOT}/src/mumps_config_file_C.c)
target_sources(mumps_config_file_C PUBLIC
          FILE_SET HEADERS
          BASE_DIRS ${MUMPS_INCLUDEDIR}
          FILES ${HEADER_FILES})
target_include_directories(mumps_config_file_C PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
set_target_properties(mumps_config_file_C PROPERTIES 
    Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
    LINKER_LANGUAGE C)
target_link_libraries(mumps_config_file_C PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     

add_library(mumps_io OBJECT ${MUMPS_ROOT}/src/mumps_io.c)
target_sources(mumps_io PUBLIC
          FILE_SET HEADERS
          BASE_DIRS ${MUMPS_INCLUDEDIR}
          FILES ${HEADER_FILES})
target_include_directories(mumps_io PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
set_target_properties(mumps_io PROPERTIES 
    Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
    LINKER_LANGUAGE C)
target_link_libraries(mumps_io PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     

add_library(mumps_io_basic OBJECT ${MUMPS_ROOT}/src/mumps_io_basic.c)
target_sources(mumps_io_basic PUBLIC
          FILE_SET HEADERS
          BASE_DIRS ${MUMPS_INCLUDEDIR}
          FILES ${HEADER_FILES})
target_include_directories(mumps_io_basic PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
set_target_properties(mumps_io_basic PROPERTIES 
    Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
    LINKER_LANGUAGE C)
target_link_libraries(mumps_io_basic PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     

add_library(mumps_io_err OBJECT ${MUMPS_ROOT}/src/mumps_io_err.c)
target_sources(mumps_io_err PUBLIC
          FILE_SET HEADERS
          BASE_DIRS ${MUMPS_INCLUDEDIR}
          FILES ${HEADER_FILES})
target_include_directories(mumps_io_err PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
set_target_properties(mumps_io_err PROPERTIES 
    Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
    LINKER_LANGUAGE C)
target_link_libraries(mumps_io_err PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     

add_library(mumps_numa OBJECT ${MUMPS_ROOT}/src/mumps_numa.c)
target_sources(mumps_numa PUBLIC
          FILE_SET HEADERS
          BASE_DIRS ${MUMPS_INCLUDEDIR}
          FILES ${HEADER_FILES})
target_include_directories(mumps_numa PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
set_target_properties(mumps_numa PROPERTIES 
    Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
    LINKER_LANGUAGE C)
target_link_libraries(mumps_numa PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     

add_library(mumps_io_thread OBJECT ${MUMPS_ROOT}/src/mumps_io_thread.c)
target_sources(mumps_io_thread PUBLIC
          FILE_SET HEADERS
          BASE_DIRS ${MUMPS_INCLUDEDIR}
          FILES ${HEADER_FILES})
target_include_directories(mumps_io_thread PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
set_target_properties(mumps_io_thread PROPERTIES 
    Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
    LINKER_LANGUAGE C)
target_link_libraries(mumps_io_thread PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     

add_library(mumps_pord OBJECT ${MUMPS_ROOT}/src/mumps_pord.c)
target_sources(mumps_pord PUBLIC
          FILE_SET HEADERS
          BASE_DIRS ${MUMPS_INCLUDEDIR}
          FILES ${HEADER_FILES})
target_include_directories(mumps_pord PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
set_target_properties(mumps_pord PROPERTIES 
    Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
    LINKER_LANGUAGE C)
target_link_libraries(mumps_pord PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     

add_library(mumps_metis OBJECT ${MUMPS_ROOT}/src/mumps_metis.c)
target_sources(mumps_metis PUBLIC
          FILE_SET HEADERS
          BASE_DIRS ${MUMPS_INCLUDEDIR}
          FILES ${HEADER_FILES})
target_include_directories(mumps_metis PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
set_target_properties(mumps_metis PROPERTIES 
    Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
    LINKER_LANGUAGE C)
target_link_libraries(mumps_metis PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     

add_library(mumps_metis64 OBJECT ${MUMPS_ROOT}/src/mumps_metis64.c)
target_sources(mumps_metis64 PUBLIC
          FILE_SET HEADERS
          BASE_DIRS ${MUMPS_INCLUDEDIR}
          FILES ${HEADER_FILES})
target_include_directories(mumps_metis64 PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
set_target_properties(mumps_metis64 PROPERTIES 
    Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
    LINKER_LANGUAGE C)
target_link_libraries(mumps_metis64 PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     

add_library(mumps_metis_int OBJECT ${MUMPS_ROOT}/src/mumps_metis_int.c)
target_sources(mumps_metis_int PUBLIC
          FILE_SET HEADERS
          BASE_DIRS ${MUMPS_INCLUDEDIR}
          FILES ${HEADER_FILES})
target_include_directories(mumps_metis_int PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
set_target_properties(mumps_metis_int PROPERTIES 
    Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
    LINKER_LANGUAGE C)
target_link_libraries(mumps_metis_int PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     

add_library(mumps_scotch OBJECT ${MUMPS_ROOT}/src/mumps_scotch.c)
target_sources(mumps_scotch PUBLIC
          FILE_SET HEADERS
          BASE_DIRS ${MUMPS_INCLUDEDIR}
          FILES ${HEADER_FILES})
target_include_directories(mumps_scotch PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
set_target_properties(mumps_scotch PROPERTIES 
    Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
    LINKER_LANGUAGE C)
target_link_libraries(mumps_scotch PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     

add_library(mumps_scotch64 OBJECT ${MUMPS_ROOT}/src/mumps_scotch64.c)
target_sources(mumps_scotch64 PUBLIC
          FILE_SET HEADERS
          BASE_DIRS ${MUMPS_INCLUDEDIR}
          FILES ${HEADER_FILES})
target_include_directories(mumps_scotch64 PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
set_target_properties(mumps_scotch64 PROPERTIES 
    Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
    LINKER_LANGUAGE C)
target_link_libraries(mumps_scotch64 PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     

add_library(mumps_scotch_int OBJECT ${MUMPS_ROOT}/src/mumps_scotch_int.c)
target_sources(mumps_scotch_int PUBLIC
          FILE_SET HEADERS
          BASE_DIRS ${MUMPS_INCLUDEDIR}
          FILES ${HEADER_FILES})
target_include_directories(mumps_scotch_int PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
set_target_properties(mumps_scotch_int PROPERTIES 
    Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
    LINKER_LANGUAGE C)
target_link_libraries(mumps_scotch_int PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     

add_library(mumps_register_thread OBJECT ${MUMPS_ROOT}/src/mumps_register_thread.c)
target_sources(mumps_register_thread PUBLIC
          FILE_SET HEADERS
          BASE_DIRS ${MUMPS_INCLUDEDIR}
          FILES ${HEADER_FILES})
target_include_directories(mumps_register_thread PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
set_target_properties(mumps_register_thread PROPERTIES 
    Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
    LINKER_LANGUAGE C)
target_link_libraries(mumps_register_thread PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     

add_library(mumps_thread OBJECT ${MUMPS_ROOT}/src/mumps_thread.c)
target_sources(mumps_thread PUBLIC
          FILE_SET HEADERS
          BASE_DIRS ${MUMPS_INCLUDEDIR}
          FILES ${HEADER_FILES})
target_include_directories(mumps_thread PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
set_target_properties(mumps_thread PROPERTIES 
    Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
    LINKER_LANGUAGE C)
target_link_libraries(mumps_thread PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     

add_library(mumps_thread_affinity OBJECT ${MUMPS_ROOT}/src/mumps_thread_affinity.c)
target_sources(mumps_thread_affinity PUBLIC
          FILE_SET HEADERS
          BASE_DIRS ${MUMPS_INCLUDEDIR}
          FILES ${HEADER_FILES})
target_include_directories(mumps_thread_affinity PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
set_target_properties(mumps_thread_affinity PROPERTIES 
    Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
    LINKER_LANGUAGE C)
target_link_libraries(mumps_thread_affinity PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     

add_library(mumps_flytes OBJECT ${MUMPS_ROOT}/src/mumps_flytes.c)
target_sources(mumps_flytes PUBLIC
          FILE_SET HEADERS
          BASE_DIRS ${MUMPS_INCLUDEDIR}
          FILES ${HEADER_FILES})
target_include_directories(mumps_flytes PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
set_target_properties(mumps_flytes PROPERTIES 
    Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
    LINKER_LANGUAGE C)
target_link_libraries(mumps_flytes PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     

add_library(mumps_sol_omp_memory_manager OBJECT ${MUMPS_ROOT}/src/mumps_sol_omp_memory_manager.c)
target_sources(mumps_sol_omp_memory_manager PUBLIC
          FILE_SET HEADERS
          BASE_DIRS ${MUMPS_INCLUDEDIR}
          FILES ${HEADER_FILES})
target_include_directories(mumps_sol_omp_memory_manager PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
set_target_properties(mumps_sol_omp_memory_manager PROPERTIES 
    Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
    LINKER_LANGUAGE C)
target_link_libraries(mumps_sol_omp_memory_manager PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     

add_library(mumps_save_restore_C OBJECT ${MUMPS_ROOT}/src/mumps_save_restore_C.c)
target_sources(mumps_save_restore_C PUBLIC
          FILE_SET HEADERS
          BASE_DIRS ${MUMPS_INCLUDEDIR}
          FILES ${HEADER_FILES})
target_include_directories(mumps_save_restore_C PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
set_target_properties(mumps_save_restore_C PROPERTIES 
    Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
    LINKER_LANGUAGE C)
target_link_libraries(mumps_save_restore_C PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     

add_library(ana_blk OBJECT ${MUMPS_ROOT}/src/ana_blk.F)
target_sources(ana_blk PUBLIC
          FILE_SET HEADERS
          BASE_DIRS ${MUMPS_INCLUDEDIR}
          FILES ${HEADER_FILES})
target_include_directories(ana_blk PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
set_target_properties(ana_blk PROPERTIES 
    Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
    LINKER_LANGUAGE C)
target_link_libraries(ana_blk PUBLIC $<TARGET_OBJECTS:ana_blk_m> $<TARGET_OBJECTS:tools_common_m>)
target_link_libraries(ana_blk PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     

add_library(mumps_static_mapping OBJECT ${MUMPS_ROOT}/src/mumps_static_mapping.F)
target_sources(mumps_static_mapping PUBLIC
          FILE_SET HEADERS
          BASE_DIRS ${MUMPS_INCLUDEDIR}
          FILES ${HEADER_FILES})
target_include_directories(mumps_static_mapping PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
set_target_properties(mumps_static_mapping PROPERTIES 
    Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
    LINKER_LANGUAGE C)
target_link_libraries(mumps_static_mapping PUBLIC $<TARGET_OBJECTS:lr_common>)
target_link_libraries(mumps_static_mapping PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     

add_library(lr_stats OBJECT ${MUMPS_ROOT}/src/lr_stats.F)
target_sources(lr_stats PUBLIC
          FILE_SET HEADERS
          BASE_DIRS ${MUMPS_INCLUDEDIR}
          FILES ${HEADER_FILES})
target_include_directories(lr_stats PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
set_target_properties(lr_stats PROPERTIES 
    Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
    LINKER_LANGUAGE C)
target_link_libraries(lr_stats PUBLIC $<TARGET_OBJECTS:lr_common>)
target_link_libraries(lr_stats PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     

add_library(fac_asm_build_sort_index_ELT_m OBJECT ${MUMPS_ROOT}/src/fac_asm_build_sort_index_ELT_m.F)
target_sources(fac_asm_build_sort_index_ELT_m PUBLIC
          FILE_SET HEADERS
          BASE_DIRS ${MUMPS_INCLUDEDIR}
          FILES ${HEADER_FILES})
target_include_directories(fac_asm_build_sort_index_ELT_m PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
set_target_properties(fac_asm_build_sort_index_ELT_m PROPERTIES 
    Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
    LINKER_LANGUAGE C)
target_link_libraries(fac_asm_build_sort_index_ELT_m PUBLIC $<TARGET_OBJECTS:omp_tps_common_m>)
target_link_libraries(fac_asm_build_sort_index_ELT_m PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     

add_library(fac_asm_build_sort_index_m OBJECT ${MUMPS_ROOT}/src/fac_asm_build_sort_index_m.F)
target_sources(fac_asm_build_sort_index_m PUBLIC
          FILE_SET HEADERS
          BASE_DIRS ${MUMPS_INCLUDEDIR}
          FILES ${HEADER_FILES})
target_include_directories(fac_asm_build_sort_index_m PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
set_target_properties(fac_asm_build_sort_index_m PROPERTIES 
    Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
    LINKER_LANGUAGE C)
target_link_libraries(fac_asm_build_sort_index_m PUBLIC $<TARGET_OBJECTS:omp_tps_common_m>)
target_link_libraries(fac_asm_build_sort_index_m PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     

add_library(tools_common OBJECT ${MUMPS_ROOT}/src/tools_common.F)
target_sources(tools_common PUBLIC
          FILE_SET HEADERS
          BASE_DIRS ${MUMPS_INCLUDEDIR}
          FILES ${HEADER_FILES})
target_include_directories(tools_common PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
set_target_properties(tools_common PROPERTIES 
    Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
    LINKER_LANGUAGE C)
target_link_libraries(tools_common PUBLIC $<TARGET_OBJECTS:lr_common> $<TARGET_OBJECTS:mumps_comm_buffer_common>)
target_link_libraries(tools_common PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     

add_library(fac_descband_data_m OBJECT ${MUMPS_ROOT}/src/fac_descband_data_m.F)
target_sources(fac_descband_data_m PUBLIC
          FILE_SET HEADERS
          BASE_DIRS ${MUMPS_INCLUDEDIR}
          FILES ${HEADER_FILES})
target_include_directories(fac_descband_data_m PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
set_target_properties(fac_descband_data_m PROPERTIES 
    Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
    LINKER_LANGUAGE C)
target_link_libraries(fac_descband_data_m PUBLIC $<TARGET_OBJECTS:front_data_mgt_m>)
target_link_libraries(fac_descband_data_m PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     

add_library(fac_maprow_data_m OBJECT ${MUMPS_ROOT}/src/fac_maprow_data_m.F)
target_sources(fac_maprow_data_m PUBLIC
          FILE_SET HEADERS
          BASE_DIRS ${MUMPS_INCLUDEDIR}
          FILES ${HEADER_FILES})
target_include_directories(fac_maprow_data_m PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
set_target_properties(fac_maprow_data_m PROPERTIES 
    Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
    LINKER_LANGUAGE C)
target_link_libraries(fac_maprow_data_m PUBLIC $<TARGET_OBJECTS:front_data_mgt_m>)
target_link_libraries(fac_maprow_data_m PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     

add_library(ana_omp_m OBJECT ${MUMPS_ROOT}/src/ana_omp_m.F)
target_sources(ana_omp_m PUBLIC
          FILE_SET HEADERS
          BASE_DIRS ${MUMPS_INCLUDEDIR}
          FILES ${HEADER_FILES})
target_include_directories(ana_omp_m PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
set_target_properties(ana_omp_m PROPERTIES 
    Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
    LINKER_LANGUAGE C)
target_link_libraries(ana_omp_m PUBLIC $<TARGET_OBJECTS:double_linked_list>)
target_link_libraries(ana_omp_m PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     

add_library(mumps_load OBJECT ${MUMPS_ROOT}/src/mumps_load.F)
target_sources(mumps_load PUBLIC
          FILE_SET HEADERS
          BASE_DIRS ${MUMPS_INCLUDEDIR}
          FILES ${HEADER_FILES})
target_include_directories(mumps_load PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
set_target_properties(mumps_load PROPERTIES 
    Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
    LINKER_LANGUAGE C)
target_link_libraries(mumps_load PUBLIC $<TARGET_OBJECTS:mumps_comm_buffer_common> $<TARGET_OBJECTS:fac_future_niv2_mod>)
target_link_libraries(mumps_load PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     

add_library(libmumps_common STATIC ${MUMPS_ROOT}/src/sol_ds_common_m.F ${MUMPS_ROOT}/src/ana_orderings.F ${MUMPS_ROOT}/src/ana_set_ordering.F ${MUMPS_ROOT}/src/ana_AMDMF.F ${MUMPS_ROOT}/src/bcast_errors.F ${MUMPS_ROOT}/src/estim_flops.F ${MUMPS_ROOT}/src/mumps_type2_blocking.F ${MUMPS_ROOT}/src/mumps_version.F ${MUMPS_ROOT}/src/mumps_print_defined.F ${MUMPS_ROOT}/src/sol_common.F $<TARGET_OBJECTS:ana_blk_m> $<TARGET_OBJECTS:ana_omp_m> $<TARGET_OBJECTS:ana_orderings_wrappers_m> $<TARGET_OBJECTS:double_linked_list> $<TARGET_OBJECTS:fac_asm_build_sort_index_ELT_m> $<TARGET_OBJECTS:fac_asm_build_sort_index_m> $<TARGET_OBJECTS:fac_descband_data_m> $<TARGET_OBJECTS:fac_future_niv2_mod> $<TARGET_OBJECTS:fac_maprow_data_m> $<TARGET_OBJECTS:front_data_mgt_m> $<TARGET_OBJECTS:lr_common> $<TARGET_OBJECTS:lr_stats> $<TARGET_OBJECTS:mumps_comm_buffer_common> $<TARGET_OBJECTS:mumps_intr_types_common> $<TARGET_OBJECTS:mumps_l0_omp_m> $<TARGET_OBJECTS:mumps_load> $<TARGET_OBJECTS:mumps_memory_mod> $<TARGET_OBJECTS:mumps_mpitoomp_m> $<TARGET_OBJECTS:mumps_ooc_common> $<TARGET_OBJECTS:mumps_pivnul_mod> $<TARGET_OBJECTS:mumps_static_mapping> $<TARGET_OBJECTS:omp_tps_common_m> $<TARGET_OBJECTS:sol_omp_common_m> $<TARGET_OBJECTS:tools_common_m> $<TARGET_OBJECTS:ana_blk> $<TARGET_OBJECTS:tools_common> $<TARGET_OBJECTS:mumps_addr> $<TARGET_OBJECTS:mumps_common> $<TARGET_OBJECTS:mumps_config_file_C> $<TARGET_OBJECTS:mumps_io> $<TARGET_OBJECTS:mumps_io_basic> $<TARGET_OBJECTS:mumps_io_err> $<TARGET_OBJECTS:mumps_numa> $<TARGET_OBJECTS:mumps_io_thread> $<TARGET_OBJECTS:mumps_pord> $<TARGET_OBJECTS:mumps_metis> $<TARGET_OBJECTS:mumps_metis64> $<TARGET_OBJECTS:mumps_metis_int> $<TARGET_OBJECTS:mumps_scotch> $<TARGET_OBJECTS:mumps_scotch64> $<TARGET_OBJECTS:mumps_scotch_int> $<TARGET_OBJECTS:mumps_register_thread> $<TARGET_OBJECTS:mumps_thread> $<TARGET_OBJECTS:mumps_thread_affinity> $<TARGET_OBJECTS:mumps_flytes> $<TARGET_OBJECTS:mumps_sol_omp_memory_manager> $<TARGET_OBJECTS:mumps_save_restore_C>)
target_sources(libmumps_common PUBLIC
          FILE_SET HEADERS
          BASE_DIRS ${MUMPS_INCLUDEDIR}
          FILES ${HEADER_FILES})
target_include_directories(libmumps_common PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
set_target_properties(libmumps_common PROPERTIES
                  Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                  LINKER_LANGUAGE C)

target_link_libraries(libmumps_common PUBLIC mumps::pord METIS::metis mumps::mpiseq OpenBLAS::OpenBLAS)
        foreach(ARITH ${ARCHS})
            add_library(${ARITH}mumps_struc_def OBJECT ${MUMPS_ROOT}/src/${ARITH}mumps_struc_def.F)
            target_sources(${ARITH}mumps_struc_def PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}mumps_struc_def PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}mumps_struc_def PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}mumps_struc_def PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}mumps_intr_types OBJECT ${MUMPS_ROOT}/src/${ARITH}mumps_intr_types.F)
            target_sources(${ARITH}mumps_intr_types PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}mumps_intr_types PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}mumps_intr_types PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}mumps_intr_types PUBLIC $<TARGET_OBJECTS:mumps_intr_types_common>)
            target_link_libraries(${ARITH}mumps_intr_types PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}omp_tps_m OBJECT ${MUMPS_ROOT}/src/${ARITH}omp_tps_m.F)
            target_sources(${ARITH}omp_tps_m PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}omp_tps_m PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}omp_tps_m PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}omp_tps_m PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}lr_type OBJECT ${MUMPS_ROOT}/src/${ARITH}lr_type.F)
            target_sources(${ARITH}lr_type PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}lr_type PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}lr_type PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}lr_type PUBLIC $<TARGET_OBJECTS:lr_common>)
            target_link_libraries(${ARITH}lr_type PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}fac_sispointers_m OBJECT ${MUMPS_ROOT}/src/${ARITH}fac_sispointers_m.F)
            target_sources(${ARITH}fac_sispointers_m PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}fac_sispointers_m PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}fac_sispointers_m PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_sispointers_m PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}static_ptr_m OBJECT ${MUMPS_ROOT}/src/${ARITH}static_ptr_m.F)
            target_sources(${ARITH}static_ptr_m PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}static_ptr_m PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}static_ptr_m PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}static_ptr_m PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}mumps_mpi3_mod OBJECT ${MUMPS_ROOT}/src/${ARITH}mumps_mpi3_mod.F)
            target_sources(${ARITH}mumps_mpi3_mod PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}mumps_mpi3_mod PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}mumps_mpi3_mod PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}mumps_mpi3_mod PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}mumps_ooc_buffer OBJECT ${MUMPS_ROOT}/src/${ARITH}mumps_ooc_buffer.F)
            target_sources(${ARITH}mumps_ooc_buffer PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}mumps_ooc_buffer PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}mumps_ooc_buffer PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}mumps_ooc_buffer PUBLIC $<TARGET_OBJECTS:mumps_ooc_common>)
            target_link_libraries(${ARITH}mumps_ooc_buffer PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}ana_aux_ELT OBJECT ${MUMPS_ROOT}/src/${ARITH}ana_aux_ELT.F)
            target_sources(${ARITH}ana_aux_ELT PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}ana_aux_ELT PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}ana_aux_ELT PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}ana_aux_ELT PUBLIC $<TARGET_OBJECTS:ana_orderings_wrappers_m>)
            target_link_libraries(${ARITH}ana_aux_ELT PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}bcast_int OBJECT ${MUMPS_ROOT}/src/${ARITH}bcast_int.F)
            target_sources(${ARITH}bcast_int PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}bcast_int PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}bcast_int PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}bcast_int PUBLIC $<TARGET_OBJECTS:mumps_comm_buffer_common>)
            target_link_libraries(${ARITH}bcast_int PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}fac_mem_alloc_cb OBJECT ${MUMPS_ROOT}/src/${ARITH}fac_mem_alloc_cb.F)
            target_sources(${ARITH}fac_mem_alloc_cb PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}fac_mem_alloc_cb PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}fac_mem_alloc_cb PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_mem_alloc_cb PUBLIC $<TARGET_OBJECTS:mumps_load>)
            target_link_libraries(${ARITH}fac_mem_alloc_cb PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}fac_mem_free_block_cb OBJECT ${MUMPS_ROOT}/src/${ARITH}fac_mem_free_block_cb.F)
            target_sources(${ARITH}fac_mem_free_block_cb PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}fac_mem_free_block_cb PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}fac_mem_free_block_cb PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_mem_free_block_cb PUBLIC $<TARGET_OBJECTS:mumps_load>)
            target_link_libraries(${ARITH}fac_mem_free_block_cb PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}fac_sol_pool OBJECT ${MUMPS_ROOT}/src/${ARITH}fac_sol_pool.F)
            target_sources(${ARITH}fac_sol_pool PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}fac_sol_pool PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}fac_sol_pool PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_sol_pool PUBLIC $<TARGET_OBJECTS:mumps_load>)
            target_link_libraries(${ARITH}fac_sol_pool PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}mumps_c OBJECT ${MUMPS_ROOT}/src/mumps_c.c)
            target_sources(${ARITH}mumps_c PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}mumps_c PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}mumps_c PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}mumps_c PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}mumps_gpu OBJECT ${MUMPS_ROOT}/src/${ARITH}mumps_gpu.c)
            target_sources(${ARITH}mumps_gpu PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}mumps_gpu PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}mumps_gpu PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}mumps_gpu PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}ana_aux OBJECT ${MUMPS_ROOT}/src/${ARITH}ana_aux.F)
            target_sources(${ARITH}ana_aux PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}ana_aux PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}ana_aux PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}ana_aux PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_struc_def> $<TARGET_OBJECTS:mumps_static_mapping> $<TARGET_OBJECTS:ana_orderings_wrappers_m> $<TARGET_OBJECTS:ana_blk_m>)
            target_link_libraries(${ARITH}ana_aux PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}ana_aux_par OBJECT ${MUMPS_ROOT}/src/${ARITH}ana_aux_par.F)
            target_sources(${ARITH}ana_aux_par PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}ana_aux_par PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}ana_aux_par PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}ana_aux_par PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_struc_def> $<TARGET_OBJECTS:mumps_memory_mod> $<TARGET_OBJECTS:ana_orderings_wrappers_m> $<TARGET_OBJECTS:tools_common_m> $<TARGET_OBJECTS:ana_blk_m>)
            target_link_libraries(${ARITH}ana_aux_par PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}mumps_config_file OBJECT ${MUMPS_ROOT}/src/${ARITH}mumps_config_file.F)
            target_sources(${ARITH}mumps_config_file PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}mumps_config_file PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}mumps_config_file PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}mumps_config_file PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_struc_def>)
            target_link_libraries(${ARITH}mumps_config_file PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}mumps_save_restore_files OBJECT ${MUMPS_ROOT}/src/${ARITH}mumps_save_restore_files.F)
            target_sources(${ARITH}mumps_save_restore_files PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}mumps_save_restore_files PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}mumps_save_restore_files PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}mumps_save_restore_files PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_struc_def>)
            target_link_libraries(${ARITH}mumps_save_restore_files PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}ana_LDLT_preprocess OBJECT ${MUMPS_ROOT}/src/${ARITH}ana_LDLT_preprocess.F)
            target_sources(${ARITH}ana_LDLT_preprocess PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}ana_LDLT_preprocess PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}ana_LDLT_preprocess PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}ana_LDLT_preprocess PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_struc_def>)
            target_link_libraries(${ARITH}ana_LDLT_preprocess PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}fac_scalings OBJECT ${MUMPS_ROOT}/src/${ARITH}fac_scalings.F)
            target_sources(${ARITH}fac_scalings PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}fac_scalings PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}fac_scalings PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_scalings PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_struc_def>)
            target_link_libraries(${ARITH}fac_scalings PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}ini_defaults OBJECT ${MUMPS_ROOT}/src/${ARITH}ini_defaults.F)
            target_sources(${ARITH}ini_defaults PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}ini_defaults PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}ini_defaults PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}ini_defaults PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_struc_def>)
            target_link_libraries(${ARITH}ini_defaults PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}sol_distrhs OBJECT ${MUMPS_ROOT}/src/${ARITH}sol_distrhs.F)
            target_sources(${ARITH}sol_distrhs PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}sol_distrhs PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}sol_distrhs PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}sol_distrhs PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_struc_def>)
            target_link_libraries(${ARITH}sol_distrhs PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}fac_sol_l0omp_m OBJECT ${MUMPS_ROOT}/src/${ARITH}fac_sol_l0omp_m.F)
            target_sources(${ARITH}fac_sol_l0omp_m PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}fac_sol_l0omp_m PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}fac_sol_l0omp_m PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_sol_l0omp_m PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_intr_types>)
            target_link_libraries(${ARITH}fac_sol_l0omp_m PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}sol_omp_m OBJECT ${MUMPS_ROOT}/src/${ARITH}sol_omp_m.F)
            target_sources(${ARITH}sol_omp_m PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}sol_omp_m PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}sol_omp_m PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}sol_omp_m PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_intr_types> $<TARGET_OBJECTS:mumps_l0_omp_m>)
            target_link_libraries(${ARITH}sol_omp_m PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}fac_distrib_distentry OBJECT ${MUMPS_ROOT}/src/${ARITH}fac_distrib_distentry.F)
            target_sources(${ARITH}fac_distrib_distentry PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}fac_distrib_distentry PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}fac_distrib_distentry PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_distrib_distentry PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_struc_def> $<TARGET_OBJECTS:mumps_intr_types_common> $<TARGET_OBJECTS:${ARITH}mumps_intr_types>)
            target_link_libraries(${ARITH}fac_distrib_distentry PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}fac_dist_arrowheads_omp OBJECT ${MUMPS_ROOT}/src/${ARITH}fac_dist_arrowheads_omp.F)
            target_sources(${ARITH}fac_dist_arrowheads_omp PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}fac_dist_arrowheads_omp PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}fac_dist_arrowheads_omp PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_dist_arrowheads_omp PUBLIC $<TARGET_OBJECTS:mumps_intr_types_common> $<TARGET_OBJECTS:${ARITH}mumps_intr_types>)
            target_link_libraries(${ARITH}fac_dist_arrowheads_omp PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}fac_distrib_ELT OBJECT ${MUMPS_ROOT}/src/${ARITH}fac_distrib_ELT.F)
            target_sources(${ARITH}fac_distrib_ELT PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}fac_distrib_ELT PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}fac_distrib_ELT PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_distrib_ELT PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_struc_def> $<TARGET_OBJECTS:mumps_intr_types_common> $<TARGET_OBJECTS:${ARITH}mumps_intr_types>)
            target_link_libraries(${ARITH}fac_distrib_ELT PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}fac_lastrtnelind OBJECT ${MUMPS_ROOT}/src/${ARITH}fac_lastrtnelind.F)
            target_sources(${ARITH}fac_lastrtnelind PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}fac_lastrtnelind PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}fac_lastrtnelind PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_lastrtnelind PUBLIC $<TARGET_OBJECTS:mumps_comm_buffer_common> $<TARGET_OBJECTS:mumps_intr_types_common> $<TARGET_OBJECTS:${ARITH}mumps_intr_types>)
            target_link_libraries(${ARITH}fac_lastrtnelind PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}fac_process_message OBJECT ${MUMPS_ROOT}/src/${ARITH}fac_process_message.F)
            target_sources(${ARITH}fac_process_message PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}fac_process_message PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}fac_process_message PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_process_message PUBLIC $<TARGET_OBJECTS:mumps_load> $<TARGET_OBJECTS:mumps_intr_types_common> $<TARGET_OBJECTS:${ARITH}mumps_intr_types> $<TARGET_OBJECTS:mumps_comm_buffer_common>)
            target_link_libraries(${ARITH}fac_process_message PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}fac_process_root2son OBJECT ${MUMPS_ROOT}/src/${ARITH}fac_process_root2son.F)
            target_sources(${ARITH}fac_process_root2son PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}fac_process_root2son PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}fac_process_root2son PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_process_root2son PUBLIC $<TARGET_OBJECTS:mumps_intr_types_common> $<TARGET_OBJECTS:${ARITH}mumps_intr_types>)
            target_link_libraries(${ARITH}fac_process_root2son PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}fac_process_rtnelind OBJECT ${MUMPS_ROOT}/src/${ARITH}fac_process_rtnelind.F)
            target_sources(${ARITH}fac_process_rtnelind PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}fac_process_rtnelind PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}fac_process_rtnelind PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_process_rtnelind PUBLIC $<TARGET_OBJECTS:mumps_load> $<TARGET_OBJECTS:mumps_intr_types_common> $<TARGET_OBJECTS:${ARITH}mumps_intr_types>)
            target_link_libraries(${ARITH}fac_process_rtnelind PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}fac_root_parallel OBJECT ${MUMPS_ROOT}/src/${ARITH}fac_root_parallel.F)
            target_sources(${ARITH}fac_root_parallel PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}fac_root_parallel PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}fac_root_parallel PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_root_parallel PUBLIC $<TARGET_OBJECTS:lr_stats> $<TARGET_OBJECTS:mumps_intr_types_common> $<TARGET_OBJECTS:${ARITH}mumps_intr_types>)
            target_link_libraries(${ARITH}fac_root_parallel PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}ini_driver OBJECT ${MUMPS_ROOT}/src/${ARITH}ini_driver.F)
            target_sources(${ARITH}ini_driver PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}ini_driver PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}ini_driver PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}ini_driver PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_struc_def> $<TARGET_OBJECTS:${ARITH}mumps_intr_types>)
            target_link_libraries(${ARITH}ini_driver PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}rank_revealing OBJECT ${MUMPS_ROOT}/src/${ARITH}rank_revealing.F)
            target_sources(${ARITH}rank_revealing PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}rank_revealing PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}rank_revealing PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}rank_revealing PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_intr_types> $<TARGET_OBJECTS:mumps_intr_types_common>)
            target_link_libraries(${ARITH}rank_revealing PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}mumps_lr_data_m OBJECT ${MUMPS_ROOT}/src/${ARITH}mumps_lr_data_m.F)
            target_sources(${ARITH}mumps_lr_data_m PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}mumps_lr_data_m PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}mumps_lr_data_m PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}mumps_lr_data_m PUBLIC $<TARGET_OBJECTS:${ARITH}lr_type> $<TARGET_OBJECTS:front_data_mgt_m>)
            target_link_libraries(${ARITH}mumps_lr_data_m PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}sol_bwd OBJECT ${MUMPS_ROOT}/src/${ARITH}sol_bwd.F)
            target_sources(${ARITH}sol_bwd PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}sol_bwd PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}sol_bwd PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}sol_bwd PUBLIC $<TARGET_OBJECTS:${ARITH}static_ptr_m> $<TARGET_OBJECTS:${ARITH}mumps_intr_types>)
            target_link_libraries(${ARITH}sol_bwd PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}sol_fwd OBJECT ${MUMPS_ROOT}/src/${ARITH}sol_fwd.F)
            target_sources(${ARITH}sol_fwd PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}sol_fwd PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}sol_fwd PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}sol_fwd PUBLIC $<TARGET_OBJECTS:${ARITH}static_ptr_m> $<TARGET_OBJECTS:${ARITH}mumps_intr_types>)
            target_link_libraries(${ARITH}sol_fwd PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}mumps_ooc OBJECT ${MUMPS_ROOT}/src/${ARITH}mumps_ooc.F)
            target_sources(${ARITH}mumps_ooc PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}mumps_ooc PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}mumps_ooc PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}mumps_ooc PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_ooc_buffer> $<TARGET_OBJECTS:mumps_ooc_common> $<TARGET_OBJECTS:${ARITH}mumps_struc_def>)
            target_link_libraries(${ARITH}mumps_ooc PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}fac_mem_dynamic OBJECT ${MUMPS_ROOT}/src/${ARITH}fac_mem_dynamic.F)
            target_sources(${ARITH}fac_mem_dynamic PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}fac_mem_dynamic PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}fac_mem_dynamic PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_mem_dynamic PUBLIC $<TARGET_OBJECTS:mumps_load> $<TARGET_OBJECTS:${ARITH}static_ptr_m> $<TARGET_OBJECTS:${ARITH}mumps_c>)
            target_link_libraries(${ARITH}fac_mem_dynamic PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}mumps_f77 OBJECT ${MUMPS_ROOT}/src/${ARITH}mumps_f77.F)
            target_sources(${ARITH}mumps_f77 PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}mumps_f77 PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}mumps_f77 PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}mumps_f77 PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_struc_def> $<TARGET_OBJECTS:${ARITH}mumps_c>)
            target_link_libraries(${ARITH}mumps_f77 PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}arrowheads OBJECT ${MUMPS_ROOT}/src/${ARITH}arrowheads.F)
            target_sources(${ARITH}arrowheads PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}arrowheads PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}arrowheads PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}arrowheads PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_struc_def> $<TARGET_OBJECTS:${ARITH}ana_aux> $<TARGET_OBJECTS:mumps_intr_types_common> $<TARGET_OBJECTS:${ARITH}mumps_intr_types>)
            target_link_libraries(${ARITH}arrowheads PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}lr_core OBJECT ${MUMPS_ROOT}/src/${ARITH}lr_core.F)
            target_sources(${ARITH}lr_core PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}lr_core PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}lr_core PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}lr_core PUBLIC $<TARGET_OBJECTS:${ARITH}lr_type> $<TARGET_OBJECTS:${ARITH}mumps_lr_data_m> $<TARGET_OBJECTS:lr_stats> $<TARGET_OBJECTS:lr_common>)
            target_link_libraries(${ARITH}lr_core PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}mumps_sol_es OBJECT ${MUMPS_ROOT}/src/${ARITH}mumps_sol_es.F)
            target_sources(${ARITH}mumps_sol_es PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}mumps_sol_es PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}mumps_sol_es PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}mumps_sol_es PUBLIC $<TARGET_OBJECTS:${ARITH}lr_type> $<TARGET_OBJECTS:${ARITH}mumps_lr_data_m>)
            target_link_libraries(${ARITH}mumps_sol_es PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}fac_process_band OBJECT ${MUMPS_ROOT}/src/${ARITH}fac_process_band.F)
            target_sources(${ARITH}fac_process_band PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}fac_process_band PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}fac_process_band PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_process_band PUBLIC $<TARGET_OBJECTS:mumps_load> $<TARGET_OBJECTS:tools_common_m> $<TARGET_OBJECTS:${ARITH}mumps_lr_data_m> $<TARGET_OBJECTS:fac_descband_data_m> $<TARGET_OBJECTS:mumps_intr_types_common> $<TARGET_OBJECTS:${ARITH}mumps_intr_types>)
            target_link_libraries(${ARITH}fac_process_band PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}fac_front_aux OBJECT ${MUMPS_ROOT}/src/${ARITH}fac_front_aux.F)
            target_sources(${ARITH}fac_front_aux PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}fac_front_aux PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}fac_front_aux PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_front_aux PUBLIC $<TARGET_OBJECTS:${ARITH}lr_type> $<TARGET_OBJECTS:lr_stats> $<TARGET_OBJECTS:mumps_comm_buffer_common> $<TARGET_OBJECTS:mumps_load> $<TARGET_OBJECTS:${ARITH}mumps_ooc> $<TARGET_OBJECTS:mumps_ooc_common> $<TARGET_OBJECTS:mumps_l0_omp_m> $<TARGET_OBJECTS:mumps_pivnul_mod>)
            target_link_libraries(${ARITH}fac_front_aux PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}mumps_save_restore OBJECT ${MUMPS_ROOT}/src/${ARITH}mumps_save_restore.F)
            target_sources(${ARITH}mumps_save_restore PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}mumps_save_restore PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}mumps_save_restore PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}mumps_save_restore PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_struc_def> $<TARGET_OBJECTS:${ARITH}mumps_save_restore_files> $<TARGET_OBJECTS:${ARITH}mumps_lr_data_m> $<TARGET_OBJECTS:${ARITH}mumps_ooc> $<TARGET_OBJECTS:${ARITH}fac_sol_l0omp_m> $<TARGET_OBJECTS:${ARITH}mumps_mpi3_mod> $<TARGET_OBJECTS:front_data_mgt_m> $<TARGET_OBJECTS:${ARITH}mumps_intr_types>)
            target_link_libraries(${ARITH}mumps_save_restore PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}fac_process_contrib_type3 OBJECT ${MUMPS_ROOT}/src/${ARITH}fac_process_contrib_type3.F)
            target_sources(${ARITH}fac_process_contrib_type3 PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}fac_process_contrib_type3 PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}fac_process_contrib_type3 PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_process_contrib_type3 PUBLIC $<TARGET_OBJECTS:mumps_load> $<TARGET_OBJECTS:${ARITH}mumps_ooc> $<TARGET_OBJECTS:mumps_intr_types_common> $<TARGET_OBJECTS:${ARITH}mumps_intr_types>)
            target_link_libraries(${ARITH}fac_process_contrib_type3 PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}fac_process_root2slave OBJECT ${MUMPS_ROOT}/src/${ARITH}fac_process_root2slave.F)
            target_sources(${ARITH}fac_process_root2slave PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}fac_process_root2slave PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}fac_process_root2slave PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_process_root2slave PUBLIC $<TARGET_OBJECTS:mumps_load> $<TARGET_OBJECTS:${ARITH}mumps_ooc> $<TARGET_OBJECTS:mumps_intr_types_common> $<TARGET_OBJECTS:${ARITH}mumps_intr_types>)
            target_link_libraries(${ARITH}fac_process_root2slave PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}ooc_panel_piv OBJECT ${MUMPS_ROOT}/src/${ARITH}ooc_panel_piv.F)
            target_sources(${ARITH}ooc_panel_piv PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}ooc_panel_piv PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}ooc_panel_piv PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}ooc_panel_piv PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_ooc> $<TARGET_OBJECTS:mumps_ooc_common>)
            target_link_libraries(${ARITH}ooc_panel_piv PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}sol_aux OBJECT ${MUMPS_ROOT}/src/${ARITH}sol_aux.F)
            target_sources(${ARITH}sol_aux PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}sol_aux PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}sol_aux PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}sol_aux PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_ooc> $<TARGET_OBJECTS:${ARITH}mumps_struc_def>)
            target_link_libraries(${ARITH}sol_aux PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}fac_compact_factors_m OBJECT ${MUMPS_ROOT}/src/${ARITH}fac_compact_factors_m.F)
            target_sources(${ARITH}fac_compact_factors_m PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}fac_compact_factors_m PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}fac_compact_factors_m PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_compact_factors_m PUBLIC $<TARGET_OBJECTS:${ARITH}fac_mem_dynamic>)
            target_link_libraries(${ARITH}fac_compact_factors_m PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}end_driver OBJECT ${MUMPS_ROOT}/src/${ARITH}end_driver.F)
            target_sources(${ARITH}end_driver PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}end_driver PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}end_driver PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}end_driver PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_struc_def> $<TARGET_OBJECTS:${ARITH}mumps_intr_types> $<TARGET_OBJECTS:front_data_mgt_m> $<TARGET_OBJECTS:${ARITH}mumps_lr_data_m> $<TARGET_OBJECTS:${ARITH}fac_sol_l0omp_m> $<TARGET_OBJECTS:${ARITH}fac_mem_dynamic> $<TARGET_OBJECTS:mumps_comm_buffer_common> $<TARGET_OBJECTS:mumps_ooc_common>)
            target_link_libraries(${ARITH}end_driver PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}fac_mem_compress_cb OBJECT ${MUMPS_ROOT}/src/${ARITH}fac_mem_compress_cb.F)
            target_sources(${ARITH}fac_mem_compress_cb PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}fac_mem_compress_cb PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}fac_mem_compress_cb PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_mem_compress_cb PUBLIC $<TARGET_OBJECTS:${ARITH}fac_mem_dynamic>)
            target_link_libraries(${ARITH}fac_mem_compress_cb PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}fac_process_contrib_type1 OBJECT ${MUMPS_ROOT}/src/${ARITH}fac_process_contrib_type1.F)
            target_sources(${ARITH}fac_process_contrib_type1 PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}fac_process_contrib_type1 PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}fac_process_contrib_type1 PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_process_contrib_type1 PUBLIC $<TARGET_OBJECTS:${ARITH}fac_mem_dynamic>)
            target_link_libraries(${ARITH}fac_process_contrib_type1 PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}fac_process_master2 OBJECT ${MUMPS_ROOT}/src/${ARITH}fac_process_master2.F)
            target_sources(${ARITH}fac_process_master2 PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}fac_process_master2 PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}fac_process_master2 PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_process_master2 PUBLIC $<TARGET_OBJECTS:mumps_load> $<TARGET_OBJECTS:${ARITH}fac_mem_dynamic>)
            target_link_libraries(${ARITH}fac_process_master2 PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}ana_lr OBJECT ${MUMPS_ROOT}/src/${ARITH}ana_lr.F)
            target_sources(${ARITH}ana_lr PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}ana_lr PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}ana_lr PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}ana_lr PUBLIC $<TARGET_OBJECTS:${ARITH}lr_core> $<TARGET_OBJECTS:lr_stats> $<TARGET_OBJECTS:lr_common> $<TARGET_OBJECTS:ana_orderings_wrappers_m> $<TARGET_OBJECTS:ana_blk_m>)
            target_link_libraries(${ARITH}ana_lr PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}fac_lr OBJECT ${MUMPS_ROOT}/src/${ARITH}fac_lr.F)
            target_sources(${ARITH}fac_lr PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}fac_lr PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}fac_lr PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_lr PUBLIC $<TARGET_OBJECTS:${ARITH}lr_core> $<TARGET_OBJECTS:${ARITH}lr_type> $<TARGET_OBJECTS:${ARITH}mumps_lr_data_m> $<TARGET_OBJECTS:lr_stats> $<TARGET_OBJECTS:lr_common>)
            target_link_libraries(${ARITH}fac_lr PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}mumps_comm_buffer OBJECT ${MUMPS_ROOT}/src/${ARITH}mumps_comm_buffer.F)
            target_sources(${ARITH}mumps_comm_buffer PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}mumps_comm_buffer PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}mumps_comm_buffer PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}mumps_comm_buffer PUBLIC $<TARGET_OBJECTS:${ARITH}lr_type> $<TARGET_OBJECTS:${ARITH}lr_core> $<TARGET_OBJECTS:${ARITH}mumps_lr_data_m> $<TARGET_OBJECTS:mumps_comm_buffer_common>)
            target_link_libraries(${ARITH}mumps_comm_buffer PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}sol_lr OBJECT ${MUMPS_ROOT}/src/${ARITH}sol_lr.F)
            target_sources(${ARITH}sol_lr PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}sol_lr PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}sol_lr PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}sol_lr PUBLIC $<TARGET_OBJECTS:${ARITH}lr_type> $<TARGET_OBJECTS:lr_stats> $<TARGET_OBJECTS:${ARITH}lr_core> $<TARGET_OBJECTS:${ARITH}mumps_lr_data_m> $<TARGET_OBJECTS:mumps_l0_omp_m>)
            target_link_libraries(${ARITH}sol_lr PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}ana_dist_m OBJECT ${MUMPS_ROOT}/src/${ARITH}ana_dist_m.F)
            target_sources(${ARITH}ana_dist_m PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}ana_dist_m PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}ana_dist_m PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}ana_dist_m PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_struc_def> $<TARGET_OBJECTS:${ARITH}mumps_intr_types> $<TARGET_OBJECTS:ana_omp_m> $<TARGET_OBJECTS:${ARITH}lr_core> $<TARGET_OBJECTS:tools_common_m>)
            target_link_libraries(${ARITH}ana_dist_m PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}fac_process_end_facto_slave OBJECT ${MUMPS_ROOT}/src/${ARITH}fac_process_end_facto_slave.F)
            target_sources(${ARITH}fac_process_end_facto_slave PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}fac_process_end_facto_slave PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}fac_process_end_facto_slave PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_process_end_facto_slave PUBLIC $<TARGET_OBJECTS:mumps_load> $<TARGET_OBJECTS:tools_common_m> $<TARGET_OBJECTS:fac_maprow_data_m> $<TARGET_OBJECTS:${ARITH}mumps_lr_data_m> $<TARGET_OBJECTS:${ARITH}lr_type> $<TARGET_OBJECTS:${ARITH}lr_core> $<TARGET_OBJECTS:${ARITH}fac_mem_dynamic> $<TARGET_OBJECTS:mumps_intr_types_common> $<TARGET_OBJECTS:${ARITH}mumps_intr_types>)
            target_link_libraries(${ARITH}fac_process_end_facto_slave PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}sol_c OBJECT ${MUMPS_ROOT}/src/${ARITH}sol_c.F)
            target_sources(${ARITH}sol_c PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}sol_c PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}sol_c PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}sol_c PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_ooc> $<TARGET_OBJECTS:${ARITH}mumps_sol_es> $<TARGET_OBJECTS:${ARITH}sol_omp_m> $<TARGET_OBJECTS:mumps_intr_types_common> $<TARGET_OBJECTS:${ARITH}mumps_intr_types> $<TARGET_OBJECTS:mumps_mpitoomp_m>)
            target_link_libraries(${ARITH}sol_c PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}fac_determinant OBJECT ${MUMPS_ROOT}/src/${ARITH}fac_determinant.F)
            target_sources(${ARITH}fac_determinant PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}fac_determinant PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}fac_determinant PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_determinant PUBLIC $<TARGET_OBJECTS:${ARITH}fac_front_aux>)
            target_link_libraries(${ARITH}fac_determinant PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}mumps_driver OBJECT ${MUMPS_ROOT}/src/${ARITH}mumps_driver.F)
            target_sources(${ARITH}mumps_driver PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}mumps_driver PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}mumps_driver PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}mumps_driver PUBLIC $<TARGET_OBJECTS:mumps_memory_mod> $<TARGET_OBJECTS:${ARITH}mumps_struc_def> $<TARGET_OBJECTS:${ARITH}static_ptr_m> $<TARGET_OBJECTS:${ARITH}mumps_save_restore> $<TARGET_OBJECTS:mumps_mpitoomp_m> $<TARGET_OBJECTS:${ARITH}mumps_config_file> $<TARGET_OBJECTS:${ARITH}mumps_intr_types>)
            target_link_libraries(${ARITH}mumps_driver PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}sol_driver OBJECT ${MUMPS_ROOT}/src/${ARITH}sol_driver.F)
            target_sources(${ARITH}sol_driver PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}sol_driver PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}sol_driver PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}sol_driver PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_struc_def> $<TARGET_OBJECTS:${ARITH}mumps_intr_types> $<TARGET_OBJECTS:${ARITH}mumps_sol_es> $<TARGET_OBJECTS:${ARITH}lr_type> $<TARGET_OBJECTS:sol_omp_common_m> $<TARGET_OBJECTS:${ARITH}fac_sol_l0omp_m> $<TARGET_OBJECTS:mumps_comm_buffer_common> $<TARGET_OBJECTS:${ARITH}mumps_ooc> $<TARGET_OBJECTS:mumps_memory_mod> $<TARGET_OBJECTS:${ARITH}mumps_lr_data_m> $<TARGET_OBJECTS:front_data_mgt_m> $<TARGET_OBJECTS:${ARITH}mumps_save_restore> $<TARGET_OBJECTS:mumps_mpitoomp_m>)
            target_link_libraries(${ARITH}sol_driver PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}fac_driver OBJECT ${MUMPS_ROOT}/src/${ARITH}fac_driver.F)
            target_sources(${ARITH}fac_driver PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}fac_driver PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}fac_driver PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_driver PUBLIC $<TARGET_OBJECTS:mumps_comm_buffer_common> $<TARGET_OBJECTS:mumps_load> $<TARGET_OBJECTS:${ARITH}mumps_ooc> $<TARGET_OBJECTS:${ARITH}mumps_struc_def> $<TARGET_OBJECTS:${ARITH}mumps_intr_types> $<TARGET_OBJECTS:${ARITH}fac_sol_l0omp_m> $<TARGET_OBJECTS:${ARITH}fac_mem_dynamic> $<TARGET_OBJECTS:lr_stats> $<TARGET_OBJECTS:${ARITH}mumps_lr_data_m> $<TARGET_OBJECTS:${ARITH}fac_compact_factors_m> $<TARGET_OBJECTS:${ARITH}lr_type> $<TARGET_OBJECTS:mumps_pivnul_mod> $<TARGET_OBJECTS:front_data_mgt_m> $<TARGET_OBJECTS:fac_descband_data_m> $<TARGET_OBJECTS:fac_maprow_data_m> $<TARGET_OBJECTS:mumps_mpitoomp_m> $<TARGET_OBJECTS:${ARITH}fac_sispointers_m>)
            target_link_libraries(${ARITH}fac_driver PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}fac_asm_master_ELT_m OBJECT ${MUMPS_ROOT}/src/${ARITH}fac_asm_master_ELT_m.F)
            target_sources(${ARITH}fac_asm_master_ELT_m PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}fac_asm_master_ELT_m PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}fac_asm_master_ELT_m PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_asm_master_ELT_m PUBLIC $<TARGET_OBJECTS:omp_tps_common_m> $<TARGET_OBJECTS:fac_asm_build_sort_index_ELT_m> $<TARGET_OBJECTS:lr_common> $<TARGET_OBJECTS:${ARITH}fac_mem_dynamic> $<TARGET_OBJECTS:${ARITH}lr_core> $<TARGET_OBJECTS:${ARITH}ana_lr> $<TARGET_OBJECTS:${ARITH}mumps_lr_data_m> $<TARGET_OBJECTS:${ARITH}mumps_intr_types> $<TARGET_OBJECTS:${ARITH}omp_tps_m> $<TARGET_OBJECTS:mumps_comm_buffer_common> $<TARGET_OBJECTS:mumps_load> $<TARGET_OBJECTS:tools_common_m> $<TARGET_OBJECTS:mumps_intr_types_common>)
            target_link_libraries(${ARITH}fac_asm_master_ELT_m PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}fac_asm_master_m OBJECT ${MUMPS_ROOT}/src/${ARITH}fac_asm_master_m.F)
            target_sources(${ARITH}fac_asm_master_m PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}fac_asm_master_m PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}fac_asm_master_m PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_asm_master_m PUBLIC $<TARGET_OBJECTS:omp_tps_common_m> $<TARGET_OBJECTS:fac_asm_build_sort_index_m> $<TARGET_OBJECTS:lr_common> $<TARGET_OBJECTS:${ARITH}fac_mem_dynamic> $<TARGET_OBJECTS:${ARITH}lr_core> $<TARGET_OBJECTS:${ARITH}ana_lr> $<TARGET_OBJECTS:${ARITH}mumps_lr_data_m> $<TARGET_OBJECTS:${ARITH}mumps_intr_types> $<TARGET_OBJECTS:${ARITH}omp_tps_m> $<TARGET_OBJECTS:mumps_comm_buffer_common> $<TARGET_OBJECTS:mumps_load> $<TARGET_OBJECTS:tools_common_m> $<TARGET_OBJECTS:mumps_intr_types_common>)
            target_link_libraries(${ARITH}fac_asm_master_m PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}ana_driver OBJECT ${MUMPS_ROOT}/src/${ARITH}ana_driver.F)
            target_sources(${ARITH}ana_driver PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}ana_driver PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}ana_driver PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}ana_driver PUBLIC $<TARGET_OBJECTS:mumps_static_mapping> $<TARGET_OBJECTS:${ARITH}mumps_struc_def> $<TARGET_OBJECTS:${ARITH}mumps_intr_types> $<TARGET_OBJECTS:mumps_memory_mod> $<TARGET_OBJECTS:${ARITH}ana_aux_par> $<TARGET_OBJECTS:${ARITH}ana_lr> $<TARGET_OBJECTS:${ARITH}lr_core> $<TARGET_OBJECTS:lr_stats> $<TARGET_OBJECTS:lr_common> $<TARGET_OBJECTS:${ARITH}ana_aux> $<TARGET_OBJECTS:ana_blk_m> $<TARGET_OBJECTS:mumps_mpitoomp_m>)
            target_link_libraries(${ARITH}ana_driver PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}fac_asm_ELT OBJECT ${MUMPS_ROOT}/src/${ARITH}fac_asm_ELT.F)
            target_sources(${ARITH}fac_asm_ELT PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}fac_asm_ELT PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}fac_asm_ELT PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_asm_ELT PUBLIC $<TARGET_OBJECTS:${ARITH}fac_mem_dynamic> $<TARGET_OBJECTS:${ARITH}ana_lr> $<TARGET_OBJECTS:${ARITH}lr_core> $<TARGET_OBJECTS:lr_common>)
            target_link_libraries(${ARITH}fac_asm_ELT PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}fac_asm OBJECT ${MUMPS_ROOT}/src/${ARITH}fac_asm.F)
            target_sources(${ARITH}fac_asm PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}fac_asm PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}fac_asm PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_asm PUBLIC $<TARGET_OBJECTS:${ARITH}fac_mem_dynamic> $<TARGET_OBJECTS:${ARITH}ana_lr> $<TARGET_OBJECTS:${ARITH}lr_core> $<TARGET_OBJECTS:lr_common> $<TARGET_OBJECTS:${ARITH}fac_front_aux>)
            target_link_libraries(${ARITH}fac_asm PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}fac_front_LU_type1 OBJECT ${MUMPS_ROOT}/src/${ARITH}fac_front_LU_type1.F)
            target_sources(${ARITH}fac_front_LU_type1 PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}fac_front_LU_type1 PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}fac_front_LU_type1 PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_front_LU_type1 PUBLIC $<TARGET_OBJECTS:${ARITH}fac_front_aux> $<TARGET_OBJECTS:${ARITH}mumps_ooc> $<TARGET_OBJECTS:${ARITH}fac_lr> $<TARGET_OBJECTS:${ARITH}lr_type> $<TARGET_OBJECTS:${ARITH}mumps_intr_types> $<TARGET_OBJECTS:lr_stats> $<TARGET_OBJECTS:${ARITH}ana_lr> $<TARGET_OBJECTS:${ARITH}mumps_lr_data_m> $<TARGET_OBJECTS:mumps_l0_omp_m> $<TARGET_OBJECTS:mumps_pivnul_mod> $<TARGET_OBJECTS:tools_common_m>)
            target_link_libraries(${ARITH}fac_front_LU_type1 PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}fac_front_LDLT_type1 OBJECT ${MUMPS_ROOT}/src/${ARITH}fac_front_LDLT_type1.F)
            target_sources(${ARITH}fac_front_LDLT_type1 PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}fac_front_LDLT_type1 PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}fac_front_LDLT_type1 PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_front_LDLT_type1 PUBLIC $<TARGET_OBJECTS:${ARITH}fac_front_aux> $<TARGET_OBJECTS:${ARITH}mumps_ooc> $<TARGET_OBJECTS:${ARITH}fac_lr> $<TARGET_OBJECTS:${ARITH}lr_type> $<TARGET_OBJECTS:lr_stats> $<TARGET_OBJECTS:${ARITH}ana_lr> $<TARGET_OBJECTS:${ARITH}mumps_lr_data_m> $<TARGET_OBJECTS:mumps_l0_omp_m> $<TARGET_OBJECTS:mumps_pivnul_mod> $<TARGET_OBJECTS:tools_common_m>)
            target_link_libraries(${ARITH}fac_front_LDLT_type1 PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}fac_process_blfac_slave OBJECT ${MUMPS_ROOT}/src/${ARITH}fac_process_blfac_slave.F)
            target_sources(${ARITH}fac_process_blfac_slave PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}fac_process_blfac_slave PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}fac_process_blfac_slave PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_process_blfac_slave PUBLIC $<TARGET_OBJECTS:mumps_comm_buffer_common> $<TARGET_OBJECTS:mumps_load> $<TARGET_OBJECTS:${ARITH}lr_core> $<TARGET_OBJECTS:${ARITH}lr_type> $<TARGET_OBJECTS:${ARITH}fac_lr> $<TARGET_OBJECTS:${ARITH}mumps_lr_data_m> $<TARGET_OBJECTS:tools_common_m> $<TARGET_OBJECTS:mumps_intr_types_common> $<TARGET_OBJECTS:${ARITH}mumps_intr_types> $<TARGET_OBJECTS:${ARITH}fac_mem_dynamic> $<TARGET_OBJECTS:${ARITH}fac_front_aux>)
            target_link_libraries(${ARITH}fac_process_blfac_slave PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}fac_process_blocfacto OBJECT ${MUMPS_ROOT}/src/${ARITH}fac_process_blocfacto.F)
            target_sources(${ARITH}fac_process_blocfacto PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}fac_process_blocfacto PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}fac_process_blocfacto PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_process_blocfacto PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_ooc> $<TARGET_OBJECTS:mumps_ooc_common> $<TARGET_OBJECTS:tools_common_m> $<TARGET_OBJECTS:mumps_load> $<TARGET_OBJECTS:mumps_comm_buffer_common> $<TARGET_OBJECTS:${ARITH}lr_core> $<TARGET_OBJECTS:${ARITH}lr_type> $<TARGET_OBJECTS:lr_stats> $<TARGET_OBJECTS:${ARITH}fac_lr> $<TARGET_OBJECTS:${ARITH}ana_lr> $<TARGET_OBJECTS:${ARITH}mumps_lr_data_m> $<TARGET_OBJECTS:mumps_intr_types_common> $<TARGET_OBJECTS:${ARITH}mumps_intr_types> $<TARGET_OBJECTS:${ARITH}fac_mem_dynamic>)
            target_link_libraries(${ARITH}fac_process_blocfacto PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}fac_front_type2_aux OBJECT ${MUMPS_ROOT}/src/${ARITH}fac_front_type2_aux.F)
            target_sources(${ARITH}fac_front_type2_aux PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}fac_front_type2_aux PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}fac_front_type2_aux PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_front_type2_aux PUBLIC $<TARGET_OBJECTS:mumps_ooc_common> $<TARGET_OBJECTS:${ARITH}fac_front_aux> $<TARGET_OBJECTS:${ARITH}lr_type> $<TARGET_OBJECTS:${ARITH}mumps_comm_buffer> $<TARGET_OBJECTS:${ARITH}mumps_intr_types> $<TARGET_OBJECTS:mumps_load> $<TARGET_OBJECTS:mumps_pivnul_mod> $<TARGET_OBJECTS:${ARITH}mumps_lr_data_m> $<TARGET_OBJECTS:tools_common_m> $<TARGET_OBJECTS:mumps_intr_types_common>)
            target_link_libraries(${ARITH}fac_front_type2_aux PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}fac_mem_stack OBJECT ${MUMPS_ROOT}/src/${ARITH}fac_mem_stack.F)
            target_sources(${ARITH}fac_mem_stack PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}fac_mem_stack PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}fac_mem_stack PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_mem_stack PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_comm_buffer> $<TARGET_OBJECTS:mumps_comm_buffer_common> $<TARGET_OBJECTS:mumps_load> $<TARGET_OBJECTS:tools_common_m> $<TARGET_OBJECTS:mumps_intr_types_common> $<TARGET_OBJECTS:${ARITH}mumps_intr_types>)
            target_link_libraries(${ARITH}fac_mem_stack PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}fac_process_blocfacto_LDLT OBJECT ${MUMPS_ROOT}/src/${ARITH}fac_process_blocfacto_LDLT.F)
            target_sources(${ARITH}fac_process_blocfacto_LDLT PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}fac_process_blocfacto_LDLT PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}fac_process_blocfacto_LDLT PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_process_blocfacto_LDLT PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_ooc> $<TARGET_OBJECTS:mumps_ooc_common> $<TARGET_OBJECTS:tools_common_m> $<TARGET_OBJECTS:mumps_load> $<TARGET_OBJECTS:mumps_comm_buffer_common> $<TARGET_OBJECTS:${ARITH}mumps_comm_buffer> $<TARGET_OBJECTS:${ARITH}lr_core> $<TARGET_OBJECTS:${ARITH}lr_type> $<TARGET_OBJECTS:lr_stats> $<TARGET_OBJECTS:${ARITH}fac_lr> $<TARGET_OBJECTS:${ARITH}ana_lr> $<TARGET_OBJECTS:${ARITH}mumps_lr_data_m> $<TARGET_OBJECTS:mumps_intr_types_common> $<TARGET_OBJECTS:${ARITH}mumps_intr_types> $<TARGET_OBJECTS:${ARITH}fac_mem_dynamic> $<TARGET_OBJECTS:${ARITH}fac_front_aux>)
            target_link_libraries(${ARITH}fac_process_blocfacto_LDLT PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}fac_process_contrib_type2 OBJECT ${MUMPS_ROOT}/src/${ARITH}fac_process_contrib_type2.F)
            target_sources(${ARITH}fac_process_contrib_type2 PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}fac_process_contrib_type2 PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}fac_process_contrib_type2 PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_process_contrib_type2 PUBLIC $<TARGET_OBJECTS:mumps_load> $<TARGET_OBJECTS:${ARITH}mumps_comm_buffer> $<TARGET_OBJECTS:${ARITH}lr_type> $<TARGET_OBJECTS:lr_stats> $<TARGET_OBJECTS:${ARITH}lr_core> $<TARGET_OBJECTS:mumps_intr_types_common> $<TARGET_OBJECTS:${ARITH}mumps_intr_types> $<TARGET_OBJECTS:${ARITH}fac_mem_dynamic>)
            target_link_libraries(${ARITH}fac_process_contrib_type2 PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}fac_process_maprow OBJECT ${MUMPS_ROOT}/src/${ARITH}fac_process_maprow.F)
            target_sources(${ARITH}fac_process_maprow PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}fac_process_maprow PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}fac_process_maprow PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_process_maprow PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_comm_buffer> $<TARGET_OBJECTS:mumps_load> $<TARGET_OBJECTS:${ARITH}mumps_lr_data_m> $<TARGET_OBJECTS:${ARITH}fac_mem_dynamic> $<TARGET_OBJECTS:${ARITH}fac_front_aux> $<TARGET_OBJECTS:fac_maprow_data_m> $<TARGET_OBJECTS:mumps_intr_types_common> $<TARGET_OBJECTS:${ARITH}mumps_intr_types> $<TARGET_OBJECTS:${ARITH}lr_type> $<TARGET_OBJECTS:lr_stats> $<TARGET_OBJECTS:${ARITH}lr_core>)
            target_link_libraries(${ARITH}fac_process_maprow PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}tools OBJECT ${MUMPS_ROOT}/src/${ARITH}tools.F)
            target_sources(${ARITH}tools PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}tools PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}tools PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}tools PUBLIC $<TARGET_OBJECTS:mumps_load> $<TARGET_OBJECTS:${ARITH}mumps_ooc> $<TARGET_OBJECTS:${ARITH}lr_core> $<TARGET_OBJECTS:${ARITH}fac_mem_dynamic> $<TARGET_OBJECTS:${ARITH}mumps_struc_def> $<TARGET_OBJECTS:${ARITH}mumps_intr_types> $<TARGET_OBJECTS:${ARITH}static_ptr_m> $<TARGET_OBJECTS:${ARITH}mumps_comm_buffer> $<TARGET_OBJECTS:${ARITH}lr_type> $<TARGET_OBJECTS:${ARITH}fac_lr> $<TARGET_OBJECTS:mumps_comm_buffer_common>)
            target_link_libraries(${ARITH}tools PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}type3_root OBJECT ${MUMPS_ROOT}/src/${ARITH}type3_root.F)
            target_sources(${ARITH}type3_root PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}type3_root PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}type3_root PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}type3_root PUBLIC $<TARGET_OBJECTS:mumps_intr_types_common> $<TARGET_OBJECTS:${ARITH}mumps_intr_types> $<TARGET_OBJECTS:${ARITH}mumps_ooc> $<TARGET_OBJECTS:${ARITH}mumps_comm_buffer> $<TARGET_OBJECTS:mumps_load> $<TARGET_OBJECTS:${ARITH}fac_mem_dynamic>)
            target_link_libraries(${ARITH}type3_root PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}sol_bwd_aux OBJECT ${MUMPS_ROOT}/src/${ARITH}sol_bwd_aux.F)
            target_sources(${ARITH}sol_bwd_aux PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}sol_bwd_aux PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}sol_bwd_aux PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}sol_bwd_aux PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_ooc> $<TARGET_OBJECTS:${ARITH}mumps_comm_buffer> $<TARGET_OBJECTS:${ARITH}sol_lr>)
            target_link_libraries(${ARITH}sol_bwd_aux PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}sol_fwd_aux OBJECT ${MUMPS_ROOT}/src/${ARITH}sol_fwd_aux.F)
            target_sources(${ARITH}sol_fwd_aux PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}sol_fwd_aux PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}sol_fwd_aux PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}sol_fwd_aux PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_ooc> $<TARGET_OBJECTS:${ARITH}sol_lr> $<TARGET_OBJECTS:${ARITH}mumps_comm_buffer> $<TARGET_OBJECTS:tools_common_m> $<TARGET_OBJECTS:sol_omp_common_m>)
            target_link_libraries(${ARITH}sol_fwd_aux PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}fac_omp_m OBJECT ${MUMPS_ROOT}/src/${ARITH}fac_omp_m.F)
            target_sources(${ARITH}fac_omp_m PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}fac_omp_m PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}fac_omp_m PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_omp_m PUBLIC $<TARGET_OBJECTS:${ARITH}fac_asm_master_m> $<TARGET_OBJECTS:${ARITH}fac_asm_master_ELT_m> $<TARGET_OBJECTS:${ARITH}fac_front_LU_type1> $<TARGET_OBJECTS:${ARITH}fac_front_LDLT_type1> $<TARGET_OBJECTS:${ARITH}fac_mem_dynamic> $<TARGET_OBJECTS:${ARITH}mumps_intr_types> $<TARGET_OBJECTS:mumps_load> $<TARGET_OBJECTS:omp_tps_common_m> $<TARGET_OBJECTS:${ARITH}omp_tps_m> $<TARGET_OBJECTS:lr_stats> $<TARGET_OBJECTS:mumps_l0_omp_m> $<TARGET_OBJECTS:mumps_pivnul_mod> $<TARGET_OBJECTS:${ARITH}mumps_struc_def> $<TARGET_OBJECTS:mumps_intr_types_common>)
            target_link_libraries(${ARITH}fac_omp_m PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}fac_front_LU_type2 OBJECT ${MUMPS_ROOT}/src/${ARITH}fac_front_LU_type2.F)
            target_sources(${ARITH}fac_front_LU_type2 PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}fac_front_LU_type2 PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}fac_front_LU_type2 PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_front_LU_type2 PUBLIC $<TARGET_OBJECTS:${ARITH}fac_front_aux> $<TARGET_OBJECTS:${ARITH}fac_front_type2_aux> $<TARGET_OBJECTS:${ARITH}mumps_ooc> $<TARGET_OBJECTS:mumps_comm_buffer_common> $<TARGET_OBJECTS:${ARITH}fac_lr> $<TARGET_OBJECTS:${ARITH}lr_core> $<TARGET_OBJECTS:${ARITH}lr_type> $<TARGET_OBJECTS:lr_stats> $<TARGET_OBJECTS:${ARITH}ana_lr> $<TARGET_OBJECTS:${ARITH}mumps_intr_types> $<TARGET_OBJECTS:${ARITH}mumps_lr_data_m> $<TARGET_OBJECTS:mumps_pivnul_mod> $<TARGET_OBJECTS:mumps_intr_types_common> $<TARGET_OBJECTS:tools_common_m>)
            target_link_libraries(${ARITH}fac_front_LU_type2 PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}fac_front_LDLT_type2 OBJECT ${MUMPS_ROOT}/src/${ARITH}fac_front_LDLT_type2.F)
            target_sources(${ARITH}fac_front_LDLT_type2 PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}fac_front_LDLT_type2 PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}fac_front_LDLT_type2 PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_front_LDLT_type2 PUBLIC $<TARGET_OBJECTS:${ARITH}fac_front_aux> $<TARGET_OBJECTS:${ARITH}fac_front_type2_aux> $<TARGET_OBJECTS:${ARITH}mumps_ooc> $<TARGET_OBJECTS:mumps_comm_buffer_common> $<TARGET_OBJECTS:mumps_load> $<TARGET_OBJECTS:${ARITH}fac_lr> $<TARGET_OBJECTS:${ARITH}lr_type> $<TARGET_OBJECTS:lr_stats> $<TARGET_OBJECTS:${ARITH}ana_lr> $<TARGET_OBJECTS:${ARITH}mumps_intr_types> $<TARGET_OBJECTS:${ARITH}mumps_lr_data_m> $<TARGET_OBJECTS:mumps_pivnul_mod> $<TARGET_OBJECTS:mumps_intr_types_common> $<TARGET_OBJECTS:tools_common_m>)
            target_link_libraries(${ARITH}fac_front_LDLT_type2 PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}fac_par_m OBJECT ${MUMPS_ROOT}/src/${ARITH}fac_par_m.F)
            target_sources(${ARITH}fac_par_m PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}fac_par_m PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}fac_par_m PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_par_m PUBLIC $<TARGET_OBJECTS:mumps_load> $<TARGET_OBJECTS:${ARITH}mumps_ooc> $<TARGET_OBJECTS:${ARITH}fac_asm_master_m> $<TARGET_OBJECTS:${ARITH}fac_asm_master_ELT_m> $<TARGET_OBJECTS:${ARITH}omp_tps_m> $<TARGET_OBJECTS:${ARITH}fac_front_LU_type1> $<TARGET_OBJECTS:${ARITH}fac_front_LU_type2> $<TARGET_OBJECTS:${ARITH}fac_front_LDLT_type1> $<TARGET_OBJECTS:${ARITH}fac_front_LDLT_type2> $<TARGET_OBJECTS:${ARITH}fac_mem_dynamic> $<TARGET_OBJECTS:${ARITH}mumps_intr_types> $<TARGET_OBJECTS:lr_stats> $<TARGET_OBJECTS:omp_tps_common_m> $<TARGET_OBJECTS:mumps_l0_omp_m> $<TARGET_OBJECTS:mumps_pivnul_mod> $<TARGET_OBJECTS:mumps_comm_buffer_common> $<TARGET_OBJECTS:mumps_ooc_common> $<TARGET_OBJECTS:mumps_intr_types_common>)
            target_link_libraries(${ARITH}fac_par_m PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(${ARITH}fac_b OBJECT ${MUMPS_ROOT}/src/${ARITH}fac_b.F)
            target_sources(${ARITH}fac_b PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(${ARITH}fac_b PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(${ARITH}fac_b PROPERTIES 
                Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_b PUBLIC $<TARGET_OBJECTS:mumps_load> $<TARGET_OBJECTS:mumps_comm_buffer_common> $<TARGET_OBJECTS:${ARITH}mumps_comm_buffer> $<TARGET_OBJECTS:${ARITH}fac_sispointers_m> $<TARGET_OBJECTS:mumps_pivnul_mod> $<TARGET_OBJECTS:omp_tps_common_m> $<TARGET_OBJECTS:${ARITH}omp_tps_m> $<TARGET_OBJECTS:${ARITH}fac_omp_m> $<TARGET_OBJECTS:${ARITH}fac_mem_dynamic> $<TARGET_OBJECTS:mumps_intr_types_common> $<TARGET_OBJECTS:${ARITH}mumps_intr_types> $<TARGET_OBJECTS:${ARITH}fac_par_m>)
            target_link_libraries(${ARITH}fac_b PRIVATE pord METIS::metis mpiseq OpenBLAS::OpenBLAS)     


            add_library(lib${ARITH}mumps STATIC ${MUMPS_ROOT}/src/${ARITH}ana_reordertree.F ${MUMPS_ROOT}/src/${ARITH}fac_diag.F ${MUMPS_ROOT}/src/${ARITH}fac_mem_stack_aux.F ${MUMPS_ROOT}/src/${ARITH}fac_process_bf.F ${MUMPS_ROOT}/src/${ARITH}fac_scalings_simScaleAbs.F ${MUMPS_ROOT}/src/${ARITH}fac_scalings_simScale_util.F ${MUMPS_ROOT}/src/${ARITH}fac_type3_symmetrize.F ${MUMPS_ROOT}/src/${ARITH}mumps_iXamax.F ${MUMPS_ROOT}/src/${ARITH}ana_mtrans.F ${MUMPS_ROOT}/src/${ARITH}sol_distsol.F ${MUMPS_ROOT}/src/${ARITH}sol_matvec.F ${MUMPS_ROOT}/src/${ARITH}sol_root_parallel.F $<TARGET_OBJECTS:${ARITH}ana_aux> $<TARGET_OBJECTS:${ARITH}ana_aux_par> $<TARGET_OBJECTS:${ARITH}ana_lr> $<TARGET_OBJECTS:${ARITH}fac_asm_master_ELT_m> $<TARGET_OBJECTS:${ARITH}fac_asm_master_m> $<TARGET_OBJECTS:${ARITH}fac_compact_factors_m> $<TARGET_OBJECTS:${ARITH}fac_front_aux> $<TARGET_OBJECTS:${ARITH}fac_front_LU_type1> $<TARGET_OBJECTS:${ARITH}fac_front_LU_type2> $<TARGET_OBJECTS:${ARITH}fac_front_LDLT_type1> $<TARGET_OBJECTS:${ARITH}fac_front_LDLT_type2> $<TARGET_OBJECTS:${ARITH}fac_front_type2_aux> $<TARGET_OBJECTS:${ARITH}fac_sispointers_m> $<TARGET_OBJECTS:${ARITH}fac_lr> $<TARGET_OBJECTS:${ARITH}fac_mem_dynamic> $<TARGET_OBJECTS:${ARITH}fac_omp_m> $<TARGET_OBJECTS:${ARITH}fac_par_m> $<TARGET_OBJECTS:${ARITH}fac_sol_l0omp_m> $<TARGET_OBJECTS:${ARITH}lr_core> $<TARGET_OBJECTS:${ARITH}lr_type> $<TARGET_OBJECTS:${ARITH}mumps_comm_buffer> $<TARGET_OBJECTS:${ARITH}mumps_config_file> $<TARGET_OBJECTS:${ARITH}mumps_intr_types> $<TARGET_OBJECTS:${ARITH}mumps_lr_data_m> $<TARGET_OBJECTS:${ARITH}mumps_mpi3_mod> $<TARGET_OBJECTS:${ARITH}mumps_ooc_buffer> $<TARGET_OBJECTS:${ARITH}mumps_ooc> $<TARGET_OBJECTS:${ARITH}mumps_sol_es> $<TARGET_OBJECTS:${ARITH}mumps_save_restore_files> $<TARGET_OBJECTS:${ARITH}mumps_save_restore> $<TARGET_OBJECTS:${ARITH}mumps_struc_def> $<TARGET_OBJECTS:${ARITH}omp_tps_m> $<TARGET_OBJECTS:${ARITH}sol_lr> $<TARGET_OBJECTS:${ARITH}sol_omp_m> $<TARGET_OBJECTS:${ARITH}static_ptr_m> $<TARGET_OBJECTS:${ARITH}ana_aux_ELT> $<TARGET_OBJECTS:${ARITH}ana_dist_m> $<TARGET_OBJECTS:${ARITH}ana_driver> $<TARGET_OBJECTS:${ARITH}ana_LDLT_preprocess> $<TARGET_OBJECTS:${ARITH}arrowheads> $<TARGET_OBJECTS:${ARITH}bcast_int> $<TARGET_OBJECTS:${ARITH}end_driver> $<TARGET_OBJECTS:${ARITH}fac_asm_ELT> $<TARGET_OBJECTS:${ARITH}fac_asm> $<TARGET_OBJECTS:${ARITH}fac_b> $<TARGET_OBJECTS:${ARITH}fac_distrib_distentry> $<TARGET_OBJECTS:${ARITH}fac_dist_arrowheads_omp> $<TARGET_OBJECTS:${ARITH}fac_distrib_ELT> $<TARGET_OBJECTS:${ARITH}fac_driver> $<TARGET_OBJECTS:${ARITH}fac_lastrtnelind> $<TARGET_OBJECTS:${ARITH}fac_mem_alloc_cb> $<TARGET_OBJECTS:${ARITH}fac_mem_compress_cb> $<TARGET_OBJECTS:${ARITH}fac_mem_free_block_cb> $<TARGET_OBJECTS:${ARITH}fac_mem_stack> $<TARGET_OBJECTS:${ARITH}fac_process_band> $<TARGET_OBJECTS:${ARITH}fac_process_blfac_slave> $<TARGET_OBJECTS:${ARITH}fac_process_blocfacto_LDLT> $<TARGET_OBJECTS:${ARITH}fac_process_blocfacto> $<TARGET_OBJECTS:${ARITH}fac_process_end_facto_slave> $<TARGET_OBJECTS:${ARITH}fac_process_contrib_type1> $<TARGET_OBJECTS:${ARITH}fac_process_contrib_type2> $<TARGET_OBJECTS:${ARITH}fac_process_contrib_type3> $<TARGET_OBJECTS:${ARITH}fac_process_maprow> $<TARGET_OBJECTS:${ARITH}fac_process_master2> $<TARGET_OBJECTS:${ARITH}fac_process_message> $<TARGET_OBJECTS:${ARITH}fac_process_root2slave> $<TARGET_OBJECTS:${ARITH}fac_process_root2son> $<TARGET_OBJECTS:${ARITH}fac_process_rtnelind> $<TARGET_OBJECTS:${ARITH}fac_root_parallel> $<TARGET_OBJECTS:${ARITH}fac_scalings> $<TARGET_OBJECTS:${ARITH}fac_determinant> $<TARGET_OBJECTS:${ARITH}fac_sol_pool> $<TARGET_OBJECTS:${ARITH}ini_defaults> $<TARGET_OBJECTS:${ARITH}ini_driver> $<TARGET_OBJECTS:${ARITH}mumps_c> $<TARGET_OBJECTS:${ARITH}mumps_driver> $<TARGET_OBJECTS:${ARITH}mumps_f77> $<TARGET_OBJECTS:${ARITH}mumps_gpu> $<TARGET_OBJECTS:${ARITH}ooc_panel_piv> $<TARGET_OBJECTS:${ARITH}rank_revealing> $<TARGET_OBJECTS:${ARITH}sol_aux> $<TARGET_OBJECTS:${ARITH}sol_bwd_aux> $<TARGET_OBJECTS:${ARITH}sol_bwd> $<TARGET_OBJECTS:${ARITH}sol_c> $<TARGET_OBJECTS:${ARITH}sol_distrhs> $<TARGET_OBJECTS:${ARITH}sol_driver> $<TARGET_OBJECTS:${ARITH}sol_fwd_aux> $<TARGET_OBJECTS:${ARITH}sol_fwd> $<TARGET_OBJECTS:${ARITH}tools> $<TARGET_OBJECTS:${ARITH}type3_root>)
            target_sources(lib${ARITH}mumps PUBLIC
                      FILE_SET HEADERS
                      BASE_DIRS ${MUMPS_INCLUDEDIR}
                      FILES ${HEADER_FILES})
            target_include_directories(lib${ARITH}mumps PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(lib${ARITH}mumps PROPERTIES
                              Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules
                              LINKER_LANGUAGE C)

            target_link_libraries(lib${ARITH}mumps PUBLIC libmumps_common mumps::pord METIS::metis mumps::mpiseq OpenBLAS::OpenBLAS)
            target_compile_definitions(${ARITH}mumps_c PRIVATE MUMPS_ARITH=MUMPS_ARITH_${ARITH})
        endforeach(ARITH ${ARCHS})
