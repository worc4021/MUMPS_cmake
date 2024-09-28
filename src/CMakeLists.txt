add_library(ana_orderings_wrappers_m OBJECT ana_orderings_wrappers_m.F)
target_include_directories(ana_orderings_wrappers_m PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
set_target_properties(ana_orderings_wrappers_m PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
target_link_libraries(ana_orderings_wrappers_m PRIVATE pord metis::metis mpiseq MKL::MKL)     

add_library(ana_blk_m OBJECT ana_blk_m.F)
target_include_directories(ana_blk_m PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
set_target_properties(ana_blk_m PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
target_link_libraries(ana_blk_m PRIVATE pord metis::metis mpiseq MKL::MKL)     

add_library(mumps_memory_mod OBJECT mumps_memory_mod.F)
target_include_directories(mumps_memory_mod PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
set_target_properties(mumps_memory_mod PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
target_link_libraries(mumps_memory_mod PRIVATE pord metis::metis mpiseq MKL::MKL)     

add_library(lr_common OBJECT lr_common.F)
target_include_directories(lr_common PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
set_target_properties(lr_common PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
target_link_libraries(lr_common PRIVATE pord metis::metis mpiseq MKL::MKL)     

add_library(omp_tps_common_m OBJECT omp_tps_common_m.F)
target_include_directories(omp_tps_common_m PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
set_target_properties(omp_tps_common_m PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
target_link_libraries(omp_tps_common_m PRIVATE pord metis::metis mpiseq MKL::MKL)     

add_library(mumps_ooc_common OBJECT mumps_ooc_common.F)
target_include_directories(mumps_ooc_common PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
set_target_properties(mumps_ooc_common PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
target_link_libraries(mumps_ooc_common PRIVATE pord metis::metis mpiseq MKL::MKL)     

add_library(mumps_l0_omp_m OBJECT mumps_l0_omp_m.F)
target_include_directories(mumps_l0_omp_m PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
set_target_properties(mumps_l0_omp_m PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
target_link_libraries(mumps_l0_omp_m PRIVATE pord metis::metis mpiseq MKL::MKL)     

add_library(mumps_pivnul_mod OBJECT mumps_pivnul_mod.F)
target_include_directories(mumps_pivnul_mod PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
set_target_properties(mumps_pivnul_mod PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
target_link_libraries(mumps_pivnul_mod PRIVATE pord metis::metis mpiseq MKL::MKL)     

add_library(fac_future_niv2_mod OBJECT fac_future_niv2_mod.F)
target_include_directories(fac_future_niv2_mod PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
set_target_properties(fac_future_niv2_mod PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
target_link_libraries(fac_future_niv2_mod PRIVATE pord metis::metis mpiseq MKL::MKL)     

add_library(front_data_mgt_m OBJECT front_data_mgt_m.F)
target_include_directories(front_data_mgt_m PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
set_target_properties(front_data_mgt_m PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
target_link_libraries(front_data_mgt_m PRIVATE pord metis::metis mpiseq MKL::MKL)     

add_library(double_linked_list OBJECT double_linked_list.F)
target_include_directories(double_linked_list PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
set_target_properties(double_linked_list PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
target_link_libraries(double_linked_list PRIVATE pord metis::metis mpiseq MKL::MKL)     

add_library(mumps_addr OBJECT mumps_addr.c)
target_include_directories(mumps_addr PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
set_target_properties(mumps_addr PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
target_link_libraries(mumps_addr PRIVATE pord metis::metis mpiseq MKL::MKL)     

add_library(mumps_common OBJECT mumps_common.c)
target_include_directories(mumps_common PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
set_target_properties(mumps_common PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
target_link_libraries(mumps_common PRIVATE pord metis::metis mpiseq MKL::MKL)     

add_library(mumps_pord OBJECT mumps_pord.c)
target_include_directories(mumps_pord PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
set_target_properties(mumps_pord PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
target_link_libraries(mumps_pord PRIVATE pord metis::metis mpiseq MKL::MKL)     

add_library(mumps_metis OBJECT mumps_metis.c)
target_include_directories(mumps_metis PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
set_target_properties(mumps_metis PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
target_link_libraries(mumps_metis PRIVATE pord metis::metis mpiseq MKL::MKL)     

add_library(mumps_metis64 OBJECT mumps_metis64.c)
target_include_directories(mumps_metis64 PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
set_target_properties(mumps_metis64 PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
target_link_libraries(mumps_metis64 PRIVATE pord metis::metis mpiseq MKL::MKL)     

add_library(mumps_metis_int OBJECT mumps_metis_int.c)
target_include_directories(mumps_metis_int PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
set_target_properties(mumps_metis_int PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
target_link_libraries(mumps_metis_int PRIVATE pord metis::metis mpiseq MKL::MKL)     

add_library(mumps_scotch OBJECT mumps_scotch.c)
target_include_directories(mumps_scotch PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
set_target_properties(mumps_scotch PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
target_link_libraries(mumps_scotch PRIVATE pord metis::metis mpiseq MKL::MKL)     

add_library(mumps_scotch64 OBJECT mumps_scotch64.c)
target_include_directories(mumps_scotch64 PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
set_target_properties(mumps_scotch64 PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
target_link_libraries(mumps_scotch64 PRIVATE pord metis::metis mpiseq MKL::MKL)     

add_library(mumps_scotch_int OBJECT mumps_scotch_int.c)
target_include_directories(mumps_scotch_int PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
set_target_properties(mumps_scotch_int PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
target_link_libraries(mumps_scotch_int PRIVATE pord metis::metis mpiseq MKL::MKL)     

add_library(mumps_io OBJECT mumps_io.c)
target_include_directories(mumps_io PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
set_target_properties(mumps_io PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
target_link_libraries(mumps_io PRIVATE pord metis::metis mpiseq MKL::MKL)     

add_library(mumps_io_basic OBJECT mumps_io_basic.c)
target_include_directories(mumps_io_basic PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
set_target_properties(mumps_io_basic PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
target_link_libraries(mumps_io_basic PRIVATE pord metis::metis mpiseq MKL::MKL)     

add_library(mumps_io_thread OBJECT mumps_io_thread.c)
target_include_directories(mumps_io_thread PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
set_target_properties(mumps_io_thread PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
target_link_libraries(mumps_io_thread PRIVATE pord metis::metis mpiseq MKL::MKL)     

add_library(mumps_io_err OBJECT mumps_io_err.c)
target_include_directories(mumps_io_err PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
set_target_properties(mumps_io_err PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
target_link_libraries(mumps_io_err PRIVATE pord metis::metis mpiseq MKL::MKL)     

add_library(mumps_numa OBJECT mumps_numa.c)
target_include_directories(mumps_numa PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
set_target_properties(mumps_numa PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
target_link_libraries(mumps_numa PRIVATE pord metis::metis mpiseq MKL::MKL)     

add_library(mumps_thread OBJECT mumps_thread.c)
target_include_directories(mumps_thread PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
set_target_properties(mumps_thread PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
target_link_libraries(mumps_thread PRIVATE pord metis::metis mpiseq MKL::MKL)     

add_library(mumps_save_restore_C OBJECT mumps_save_restore_C.c)
target_include_directories(mumps_save_restore_C PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
set_target_properties(mumps_save_restore_C PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
target_link_libraries(mumps_save_restore_C PRIVATE pord metis::metis mpiseq MKL::MKL)     

add_library(mumps_config_file_C OBJECT mumps_config_file_C.c)
target_include_directories(mumps_config_file_C PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
set_target_properties(mumps_config_file_C PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
target_link_libraries(mumps_config_file_C PRIVATE pord metis::metis mpiseq MKL::MKL)     

add_library(mumps_thread_affinity OBJECT mumps_thread_affinity.c)
target_include_directories(mumps_thread_affinity PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
set_target_properties(mumps_thread_affinity PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
target_link_libraries(mumps_thread_affinity PRIVATE pord metis::metis mpiseq MKL::MKL)     

add_library(mumps_register_thread OBJECT mumps_register_thread.c)
target_include_directories(mumps_register_thread PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
set_target_properties(mumps_register_thread PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
target_link_libraries(mumps_register_thread PRIVATE pord metis::metis mpiseq MKL::MKL)     

add_library(ana_blk OBJECT ana_blk.F)
target_include_directories(ana_blk PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
set_target_properties(ana_blk PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
target_link_libraries(ana_blk PUBLIC $<TARGET_OBJECTS:ana_blk_m>)
set_target_properties(ana_blk PROPERTIES LINKER_LANGUAGE C)
target_link_libraries(ana_blk PRIVATE pord metis::metis mpiseq MKL::MKL)     

add_library(mumps_static_mapping OBJECT mumps_static_mapping.F)
target_include_directories(mumps_static_mapping PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
set_target_properties(mumps_static_mapping PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
target_link_libraries(mumps_static_mapping PUBLIC $<TARGET_OBJECTS:lr_common>)
set_target_properties(mumps_static_mapping PROPERTIES LINKER_LANGUAGE C)
target_link_libraries(mumps_static_mapping PRIVATE pord metis::metis mpiseq MKL::MKL)     

add_library(tools_common OBJECT tools_common.F)
target_include_directories(tools_common PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
set_target_properties(tools_common PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
target_link_libraries(tools_common PUBLIC $<TARGET_OBJECTS:lr_common>)
set_target_properties(tools_common PROPERTIES LINKER_LANGUAGE C)
target_link_libraries(tools_common PRIVATE pord metis::metis mpiseq MKL::MKL)     

add_library(fac_asm_build_sort_index_ELT_m OBJECT fac_asm_build_sort_index_ELT_m.F)
target_include_directories(fac_asm_build_sort_index_ELT_m PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
set_target_properties(fac_asm_build_sort_index_ELT_m PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
target_link_libraries(fac_asm_build_sort_index_ELT_m PUBLIC $<TARGET_OBJECTS:omp_tps_common_m>)
set_target_properties(fac_asm_build_sort_index_ELT_m PROPERTIES LINKER_LANGUAGE C)
target_link_libraries(fac_asm_build_sort_index_ELT_m PRIVATE pord metis::metis mpiseq MKL::MKL)     

add_library(fac_asm_build_sort_index_m OBJECT fac_asm_build_sort_index_m.F)
target_include_directories(fac_asm_build_sort_index_m PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
set_target_properties(fac_asm_build_sort_index_m PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
target_link_libraries(fac_asm_build_sort_index_m PUBLIC $<TARGET_OBJECTS:omp_tps_common_m>)
set_target_properties(fac_asm_build_sort_index_m PROPERTIES LINKER_LANGUAGE C)
target_link_libraries(fac_asm_build_sort_index_m PRIVATE pord metis::metis mpiseq MKL::MKL)     

add_library(mumps_comm_ibcast OBJECT mumps_comm_ibcast.F)
target_include_directories(mumps_comm_ibcast PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
set_target_properties(mumps_comm_ibcast PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
target_link_libraries(mumps_comm_ibcast PUBLIC $<TARGET_OBJECTS:fac_future_niv2_mod>)
set_target_properties(mumps_comm_ibcast PROPERTIES LINKER_LANGUAGE C)
target_link_libraries(mumps_comm_ibcast PRIVATE pord metis::metis mpiseq MKL::MKL)     

add_library(fac_ibct_data_m OBJECT fac_ibct_data_m.F)
target_include_directories(fac_ibct_data_m PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
set_target_properties(fac_ibct_data_m PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
target_link_libraries(fac_ibct_data_m PUBLIC $<TARGET_OBJECTS:front_data_mgt_m>)
set_target_properties(fac_ibct_data_m PROPERTIES LINKER_LANGUAGE C)
target_link_libraries(fac_ibct_data_m PRIVATE pord metis::metis mpiseq MKL::MKL)     

add_library(fac_descband_data_m OBJECT fac_descband_data_m.F)
target_include_directories(fac_descband_data_m PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
set_target_properties(fac_descband_data_m PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
target_link_libraries(fac_descband_data_m PUBLIC $<TARGET_OBJECTS:front_data_mgt_m>)
set_target_properties(fac_descband_data_m PROPERTIES LINKER_LANGUAGE C)
target_link_libraries(fac_descband_data_m PRIVATE pord metis::metis mpiseq MKL::MKL)     

add_library(fac_maprow_data_m OBJECT fac_maprow_data_m.F)
target_include_directories(fac_maprow_data_m PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
set_target_properties(fac_maprow_data_m PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
target_link_libraries(fac_maprow_data_m PUBLIC $<TARGET_OBJECTS:front_data_mgt_m>)
set_target_properties(fac_maprow_data_m PROPERTIES LINKER_LANGUAGE C)
target_link_libraries(fac_maprow_data_m PRIVATE pord metis::metis mpiseq MKL::MKL)     

add_library(ana_omp_m OBJECT ana_omp_m.F)
target_include_directories(ana_omp_m PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
set_target_properties(ana_omp_m PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
target_link_libraries(ana_omp_m PUBLIC $<TARGET_OBJECTS:double_linked_list>)
set_target_properties(ana_omp_m PROPERTIES LINKER_LANGUAGE C)
target_link_libraries(ana_omp_m PRIVATE pord metis::metis mpiseq MKL::MKL)     

add_library(libmumps_common STATIC mumps_mpitoomp_m.F sol_ds_common_m.F ana_orderings.F ana_set_ordering.F ana_AMDMF.F bcast_errors.F estim_flops.F mumps_type2_blocking.F mumps_version.F mumps_print_defined.F sol_common.F)
target_include_directories(libmumps_common PUBLIC $<BUILD_INTERFACE:${MUMPS_INCLUDEDIR}> $<INSTALL_INTERFACE:${HEADER_INSTALL_DIR}>)
target_include_directories(libmumps_common PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
set_target_properties(libmumps_common PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
target_link_libraries(libmumps_common PRIVATE $<TARGET_OBJECTS:mumps_pivnul_mod> $<TARGET_OBJECTS:ana_omp_m> $<TARGET_OBJECTS:ana_blk_m> $<TARGET_OBJECTS:ana_orderings_wrappers_m> $<TARGET_OBJECTS:double_linked_list> $<TARGET_OBJECTS:fac_asm_build_sort_index_ELT_m> $<TARGET_OBJECTS:fac_asm_build_sort_index_m> $<TARGET_OBJECTS:fac_descband_data_m> $<TARGET_OBJECTS:fac_future_niv2_mod> $<TARGET_OBJECTS:fac_ibct_data_m> $<TARGET_OBJECTS:fac_maprow_data_m> $<TARGET_OBJECTS:front_data_mgt_m> $<TARGET_OBJECTS:lr_common> $<TARGET_OBJECTS:mumps_comm_ibcast> $<TARGET_OBJECTS:mumps_l0_omp_m> $<TARGET_OBJECTS:mumps_memory_mod> $<TARGET_OBJECTS:mumps_ooc_common> $<TARGET_OBJECTS:mumps_static_mapping> $<TARGET_OBJECTS:omp_tps_common_m> $<TARGET_OBJECTS:ana_blk> $<TARGET_OBJECTS:mumps_addr> $<TARGET_OBJECTS:mumps_common> $<TARGET_OBJECTS:mumps_pord> $<TARGET_OBJECTS:mumps_metis> $<TARGET_OBJECTS:mumps_metis64> $<TARGET_OBJECTS:mumps_metis_int> $<TARGET_OBJECTS:mumps_scotch> $<TARGET_OBJECTS:mumps_scotch64> $<TARGET_OBJECTS:mumps_scotch_int> $<TARGET_OBJECTS:mumps_io> $<TARGET_OBJECTS:mumps_io_basic> $<TARGET_OBJECTS:mumps_io_thread> $<TARGET_OBJECTS:mumps_io_err> $<TARGET_OBJECTS:mumps_numa> $<TARGET_OBJECTS:mumps_thread> $<TARGET_OBJECTS:mumps_save_restore_C> $<TARGET_OBJECTS:mumps_config_file_C> $<TARGET_OBJECTS:mumps_thread_affinity> $<TARGET_OBJECTS:mumps_register_thread> $<TARGET_OBJECTS:tools_common>)
set_target_properties(libmumps_common PROPERTIES LINKER_LANGUAGE C)
target_link_libraries(libmumps_common PUBLIC mumps::pord metis::metis mumps::mpiseq MKL::MKL)
        foreach(ARITH ${ARCHS})
            add_library(${ARITH}mumps_struc_def OBJECT ${ARITH}mumps_struc_def.F)
            target_include_directories(${ARITH}mumps_struc_def PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}mumps_struc_def PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}mumps_struc_def PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}omp_tps_m OBJECT ${ARITH}omp_tps_m.F)
            target_include_directories(${ARITH}omp_tps_m PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}omp_tps_m PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}omp_tps_m PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}lr_type OBJECT ${ARITH}lr_type.F)
            target_include_directories(${ARITH}lr_type PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}lr_type PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}lr_type PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}fac_sispointers_m OBJECT ${ARITH}fac_sispointers_m.F)
            target_include_directories(${ARITH}fac_sispointers_m PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}fac_sispointers_m PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}fac_sispointers_m PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}static_ptr_m OBJECT ${ARITH}static_ptr_m.F)
            target_include_directories(${ARITH}static_ptr_m PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}static_ptr_m PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}static_ptr_m PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}mumps_ooc_buffer OBJECT ${ARITH}mumps_ooc_buffer.F)
            target_include_directories(${ARITH}mumps_ooc_buffer PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}mumps_ooc_buffer PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}mumps_ooc_buffer PUBLIC $<TARGET_OBJECTS:mumps_ooc_common>)
            set_target_properties(${ARITH}mumps_ooc_buffer PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}mumps_ooc_buffer PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}mumps_mpi3_mod OBJECT ${ARITH}mumps_mpi3_mod.F)
            target_include_directories(${ARITH}mumps_mpi3_mod PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}mumps_mpi3_mod PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}mumps_mpi3_mod PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}ana_aux_ELT OBJECT ${ARITH}ana_aux_ELT.F)
            target_include_directories(${ARITH}ana_aux_ELT PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}ana_aux_ELT PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}ana_aux_ELT PUBLIC $<TARGET_OBJECTS:ana_orderings_wrappers_m>)
            set_target_properties(${ARITH}ana_aux_ELT PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}ana_aux_ELT PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}mumps_c OBJECT mumps_c.c)
            target_include_directories(${ARITH}mumps_c PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}mumps_c PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}mumps_c PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}mumps_gpu OBJECT ${ARITH}mumps_gpu.c)
            target_include_directories(${ARITH}mumps_gpu PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}mumps_gpu PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}mumps_gpu PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}ana_aux OBJECT ${ARITH}ana_aux.F)
            target_include_directories(${ARITH}ana_aux PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}ana_aux PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}ana_aux PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_struc_def> $<TARGET_OBJECTS:mumps_static_mapping> $<TARGET_OBJECTS:ana_orderings_wrappers_m> $<TARGET_OBJECTS:ana_blk_m>)
            set_target_properties(${ARITH}ana_aux PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}ana_aux PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}ana_aux_par OBJECT ${ARITH}ana_aux_par.F)
            target_include_directories(${ARITH}ana_aux_par PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}ana_aux_par PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}ana_aux_par PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_struc_def> $<TARGET_OBJECTS:mumps_memory_mod> $<TARGET_OBJECTS:ana_orderings_wrappers_m> $<TARGET_OBJECTS:ana_blk_m>)
            set_target_properties(${ARITH}ana_aux_par PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}ana_aux_par PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}fac_sol_l0omp_m OBJECT ${ARITH}fac_sol_l0omp_m.F)
            target_include_directories(${ARITH}fac_sol_l0omp_m PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}fac_sol_l0omp_m PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}fac_sol_l0omp_m PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_struc_def>)
            set_target_properties(${ARITH}fac_sol_l0omp_m PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_sol_l0omp_m PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}mumps_config_file OBJECT ${ARITH}mumps_config_file.F)
            target_include_directories(${ARITH}mumps_config_file PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}mumps_config_file PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}mumps_config_file PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_struc_def>)
            set_target_properties(${ARITH}mumps_config_file PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}mumps_config_file PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}mumps_save_restore_files OBJECT ${ARITH}mumps_save_restore_files.F)
            target_include_directories(${ARITH}mumps_save_restore_files PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}mumps_save_restore_files PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}mumps_save_restore_files PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_struc_def>)
            set_target_properties(${ARITH}mumps_save_restore_files PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}mumps_save_restore_files PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}sol_omp_m OBJECT ${ARITH}sol_omp_m.F)
            target_include_directories(${ARITH}sol_omp_m PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}sol_omp_m PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}sol_omp_m PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_struc_def>)
            set_target_properties(${ARITH}sol_omp_m PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}sol_omp_m PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}sol_distrhs OBJECT ${ARITH}sol_distrhs.F)
            target_include_directories(${ARITH}sol_distrhs PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}sol_distrhs PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}sol_distrhs PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_struc_def>)
            set_target_properties(${ARITH}sol_distrhs PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}sol_distrhs PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}ana_LDLT_preprocess OBJECT ${ARITH}ana_LDLT_preprocess.F)
            target_include_directories(${ARITH}ana_LDLT_preprocess PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}ana_LDLT_preprocess PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}ana_LDLT_preprocess PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_struc_def>)
            set_target_properties(${ARITH}ana_LDLT_preprocess PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}ana_LDLT_preprocess PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}arrowheads OBJECT ${ARITH}arrowheads.F)
            target_include_directories(${ARITH}arrowheads PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}arrowheads PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}arrowheads PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_struc_def>)
            set_target_properties(${ARITH}arrowheads PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}arrowheads PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}fac_distrib_distentry OBJECT ${ARITH}fac_distrib_distentry.F)
            target_include_directories(${ARITH}fac_distrib_distentry PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}fac_distrib_distentry PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}fac_distrib_distentry PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_struc_def>)
            set_target_properties(${ARITH}fac_distrib_distentry PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_distrib_distentry PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}fac_dist_arrowheads_omp OBJECT ${ARITH}fac_dist_arrowheads_omp.F)
            target_include_directories(${ARITH}fac_dist_arrowheads_omp PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}fac_dist_arrowheads_omp PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}fac_dist_arrowheads_omp PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_struc_def>)
            set_target_properties(${ARITH}fac_dist_arrowheads_omp PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_dist_arrowheads_omp PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}fac_distrib_ELT OBJECT ${ARITH}fac_distrib_ELT.F)
            target_include_directories(${ARITH}fac_distrib_ELT PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}fac_distrib_ELT PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}fac_distrib_ELT PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_struc_def>)
            set_target_properties(${ARITH}fac_distrib_ELT PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_distrib_ELT PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}fac_process_root2son OBJECT ${ARITH}fac_process_root2son.F)
            target_include_directories(${ARITH}fac_process_root2son PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}fac_process_root2son PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}fac_process_root2son PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_struc_def>)
            set_target_properties(${ARITH}fac_process_root2son PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_process_root2son PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}fac_scalings OBJECT ${ARITH}fac_scalings.F)
            target_include_directories(${ARITH}fac_scalings PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}fac_scalings PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}fac_scalings PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_struc_def>)
            set_target_properties(${ARITH}fac_scalings PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_scalings PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}ini_defaults OBJECT ${ARITH}ini_defaults.F)
            target_include_directories(${ARITH}ini_defaults PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}ini_defaults PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}ini_defaults PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_struc_def>)
            set_target_properties(${ARITH}ini_defaults PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}ini_defaults PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}mumps_f77 OBJECT ${ARITH}mumps_f77.F)
            target_include_directories(${ARITH}mumps_f77 PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}mumps_f77 PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}mumps_f77 PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_struc_def>)
            set_target_properties(${ARITH}mumps_f77 PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}mumps_f77 PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}rank_revealing OBJECT ${ARITH}rank_revealing.F)
            target_include_directories(${ARITH}rank_revealing PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}rank_revealing PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}rank_revealing PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_struc_def>)
            set_target_properties(${ARITH}rank_revealing PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}rank_revealing PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}lr_stats OBJECT ${ARITH}lr_stats.F)
            target_include_directories(${ARITH}lr_stats PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}lr_stats PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}lr_stats PUBLIC $<TARGET_OBJECTS:${ARITH}lr_type> $<TARGET_OBJECTS:${ARITH}mumps_struc_def>)
            set_target_properties(${ARITH}lr_stats PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}lr_stats PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}mumps_lr_data_m OBJECT ${ARITH}mumps_lr_data_m.F)
            target_include_directories(${ARITH}mumps_lr_data_m PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}mumps_lr_data_m PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}mumps_lr_data_m PUBLIC $<TARGET_OBJECTS:${ARITH}lr_type> $<TARGET_OBJECTS:front_data_mgt_m>)
            set_target_properties(${ARITH}mumps_lr_data_m PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}mumps_lr_data_m PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}sol_bwd OBJECT ${ARITH}sol_bwd.F)
            target_include_directories(${ARITH}sol_bwd PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}sol_bwd PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}sol_bwd PUBLIC $<TARGET_OBJECTS:${ARITH}static_ptr_m> $<TARGET_OBJECTS:${ARITH}mumps_struc_def>)
            set_target_properties(${ARITH}sol_bwd PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}sol_bwd PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}sol_fwd OBJECT ${ARITH}sol_fwd.F)
            target_include_directories(${ARITH}sol_fwd PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}sol_fwd PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}sol_fwd PUBLIC $<TARGET_OBJECTS:${ARITH}static_ptr_m> $<TARGET_OBJECTS:${ARITH}mumps_struc_def>)
            set_target_properties(${ARITH}sol_fwd PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}sol_fwd PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}mumps_ooc OBJECT ${ARITH}mumps_ooc.F)
            target_include_directories(${ARITH}mumps_ooc PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}mumps_ooc PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}mumps_ooc PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_struc_def> $<TARGET_OBJECTS:${ARITH}mumps_ooc_buffer> $<TARGET_OBJECTS:mumps_ooc_common>)
            set_target_properties(${ARITH}mumps_ooc PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}mumps_ooc PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}fac_root_parallel OBJECT ${ARITH}fac_root_parallel.F)
            target_include_directories(${ARITH}fac_root_parallel PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}fac_root_parallel PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}fac_root_parallel PUBLIC $<TARGET_OBJECTS:${ARITH}lr_stats> $<TARGET_OBJECTS:${ARITH}mumps_struc_def>)
            set_target_properties(${ARITH}fac_root_parallel PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_root_parallel PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}lr_core OBJECT ${ARITH}lr_core.F)
            target_include_directories(${ARITH}lr_core PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}lr_core PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}lr_core PUBLIC $<TARGET_OBJECTS:${ARITH}lr_type> $<TARGET_OBJECTS:${ARITH}mumps_lr_data_m> $<TARGET_OBJECTS:${ARITH}lr_stats> $<TARGET_OBJECTS:lr_common>)
            set_target_properties(${ARITH}lr_core PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}lr_core PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}mumps_sol_es OBJECT ${ARITH}mumps_sol_es.F)
            target_include_directories(${ARITH}mumps_sol_es PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}mumps_sol_es PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}mumps_sol_es PUBLIC $<TARGET_OBJECTS:${ARITH}lr_type> $<TARGET_OBJECTS:${ARITH}mumps_lr_data_m>)
            set_target_properties(${ARITH}mumps_sol_es PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}mumps_sol_es PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}mumps_save_restore OBJECT ${ARITH}mumps_save_restore.F)
            target_include_directories(${ARITH}mumps_save_restore PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}mumps_save_restore PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}mumps_save_restore PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_struc_def> $<TARGET_OBJECTS:${ARITH}mumps_save_restore_files> $<TARGET_OBJECTS:${ARITH}mumps_lr_data_m> $<TARGET_OBJECTS:${ARITH}mumps_ooc> $<TARGET_OBJECTS:${ARITH}fac_sol_l0omp_m> $<TARGET_OBJECTS:${ARITH}mumps_mpi3_mod> $<TARGET_OBJECTS:front_data_mgt_m>)
            set_target_properties(${ARITH}mumps_save_restore PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}mumps_save_restore PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}ooc_panel_piv OBJECT ${ARITH}ooc_panel_piv.F)
            target_include_directories(${ARITH}ooc_panel_piv PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}ooc_panel_piv PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}ooc_panel_piv PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_ooc> $<TARGET_OBJECTS:mumps_ooc_common>)
            set_target_properties(${ARITH}ooc_panel_piv PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}ooc_panel_piv PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}sol_aux OBJECT ${ARITH}sol_aux.F)
            target_include_directories(${ARITH}sol_aux PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}sol_aux PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}sol_aux PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_ooc> $<TARGET_OBJECTS:${ARITH}mumps_struc_def>)
            set_target_properties(${ARITH}sol_aux PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}sol_aux PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}ana_lr OBJECT ${ARITH}ana_lr.F)
            target_include_directories(${ARITH}ana_lr PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}ana_lr PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}ana_lr PUBLIC $<TARGET_OBJECTS:${ARITH}lr_core> $<TARGET_OBJECTS:${ARITH}lr_stats> $<TARGET_OBJECTS:lr_common> $<TARGET_OBJECTS:ana_orderings_wrappers_m> $<TARGET_OBJECTS:ana_blk_m>)
            set_target_properties(${ARITH}ana_lr PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}ana_lr PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}mumps_comm_buffer OBJECT ${ARITH}mumps_comm_buffer.F)
            target_include_directories(${ARITH}mumps_comm_buffer PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}mumps_comm_buffer PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}mumps_comm_buffer PUBLIC $<TARGET_OBJECTS:mumps_comm_ibcast> $<TARGET_OBJECTS:${ARITH}lr_type> $<TARGET_OBJECTS:${ARITH}lr_core> $<TARGET_OBJECTS:${ARITH}mumps_lr_data_m> $<TARGET_OBJECTS:fac_ibct_data_m>)
            set_target_properties(${ARITH}mumps_comm_buffer PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}mumps_comm_buffer PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}fac_lr OBJECT ${ARITH}fac_lr.F)
            target_include_directories(${ARITH}fac_lr PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}fac_lr PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}fac_lr PUBLIC $<TARGET_OBJECTS:${ARITH}lr_core> $<TARGET_OBJECTS:${ARITH}lr_type> $<TARGET_OBJECTS:${ARITH}mumps_lr_data_m> $<TARGET_OBJECTS:${ARITH}lr_stats>)
            set_target_properties(${ARITH}fac_lr PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_lr PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}sol_lr OBJECT ${ARITH}sol_lr.F)
            target_include_directories(${ARITH}sol_lr PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}sol_lr PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}sol_lr PUBLIC $<TARGET_OBJECTS:${ARITH}lr_type> $<TARGET_OBJECTS:${ARITH}lr_stats> $<TARGET_OBJECTS:${ARITH}lr_core> $<TARGET_OBJECTS:${ARITH}mumps_lr_data_m>)
            set_target_properties(${ARITH}sol_lr PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}sol_lr PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}ana_dist_m OBJECT ${ARITH}ana_dist_m.F)
            target_include_directories(${ARITH}ana_dist_m PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}ana_dist_m PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}ana_dist_m PUBLIC $<TARGET_OBJECTS:${ARITH}lr_core>)
            set_target_properties(${ARITH}ana_dist_m PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}ana_dist_m PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}sol_c OBJECT ${ARITH}sol_c.F)
            target_include_directories(${ARITH}sol_c PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}sol_c PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}sol_c PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_ooc> $<TARGET_OBJECTS:${ARITH}mumps_sol_es> $<TARGET_OBJECTS:${ARITH}sol_omp_m> $<TARGET_OBJECTS:${ARITH}mumps_struc_def>)
            set_target_properties(${ARITH}sol_c PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}sol_c PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}mumps_driver OBJECT ${ARITH}mumps_driver.F)
            target_include_directories(${ARITH}mumps_driver PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}mumps_driver PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}mumps_driver PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_ooc> $<TARGET_OBJECTS:mumps_memory_mod> $<TARGET_OBJECTS:${ARITH}mumps_struc_def> $<TARGET_OBJECTS:${ARITH}static_ptr_m> $<TARGET_OBJECTS:${ARITH}mumps_save_restore>)
            set_target_properties(${ARITH}mumps_driver PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}mumps_driver PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}mumps_load OBJECT ${ARITH}mumps_load.F)
            target_include_directories(${ARITH}mumps_load PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}mumps_load PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}mumps_load PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_comm_buffer> $<TARGET_OBJECTS:${ARITH}mumps_struc_def> $<TARGET_OBJECTS:fac_future_niv2_mod>)
            set_target_properties(${ARITH}mumps_load PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}mumps_load PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}ini_driver OBJECT ${ARITH}ini_driver.F)
            target_include_directories(${ARITH}ini_driver PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}ini_driver PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}ini_driver PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_struc_def> $<TARGET_OBJECTS:${ARITH}mumps_comm_buffer>)
            set_target_properties(${ARITH}ini_driver PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}ini_driver PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}sol_driver OBJECT ${ARITH}sol_driver.F)
            target_include_directories(${ARITH}sol_driver PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}sol_driver PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}sol_driver PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_struc_def> $<TARGET_OBJECTS:${ARITH}mumps_sol_es> $<TARGET_OBJECTS:${ARITH}sol_omp_m> $<TARGET_OBJECTS:${ARITH}mumps_comm_buffer> $<TARGET_OBJECTS:${ARITH}mumps_ooc> $<TARGET_OBJECTS:mumps_memory_mod> $<TARGET_OBJECTS:${ARITH}mumps_lr_data_m> $<TARGET_OBJECTS:front_data_mgt_m> $<TARGET_OBJECTS:${ARITH}mumps_save_restore>)
            set_target_properties(${ARITH}sol_driver PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}sol_driver PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}end_driver OBJECT ${ARITH}end_driver.F)
            target_include_directories(${ARITH}end_driver PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}end_driver PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}end_driver PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_struc_def> $<TARGET_OBJECTS:front_data_mgt_m> $<TARGET_OBJECTS:${ARITH}mumps_lr_data_m> $<TARGET_OBJECTS:${ARITH}mumps_ooc> $<TARGET_OBJECTS:${ARITH}fac_sol_l0omp_m> $<TARGET_OBJECTS:${ARITH}mumps_comm_buffer>)
            set_target_properties(${ARITH}end_driver PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}end_driver PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}bcast_int OBJECT ${ARITH}bcast_int.F)
            target_include_directories(${ARITH}bcast_int PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}bcast_int PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}bcast_int PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_comm_buffer>)
            set_target_properties(${ARITH}bcast_int PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}bcast_int PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}fac_lastrtnelind OBJECT ${ARITH}fac_lastrtnelind.F)
            target_include_directories(${ARITH}fac_lastrtnelind PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}fac_lastrtnelind PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}fac_lastrtnelind PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_comm_buffer> $<TARGET_OBJECTS:${ARITH}mumps_struc_def>)
            set_target_properties(${ARITH}fac_lastrtnelind PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_lastrtnelind PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}sol_bwd_aux OBJECT ${ARITH}sol_bwd_aux.F)
            target_include_directories(${ARITH}sol_bwd_aux PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}sol_bwd_aux PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}sol_bwd_aux PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_ooc> $<TARGET_OBJECTS:${ARITH}mumps_comm_buffer> $<TARGET_OBJECTS:${ARITH}sol_lr>)
            set_target_properties(${ARITH}sol_bwd_aux PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}sol_bwd_aux PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}sol_fwd_aux OBJECT ${ARITH}sol_fwd_aux.F)
            target_include_directories(${ARITH}sol_fwd_aux PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}sol_fwd_aux PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}sol_fwd_aux PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_ooc> $<TARGET_OBJECTS:${ARITH}sol_lr> $<TARGET_OBJECTS:${ARITH}mumps_comm_buffer> $<TARGET_OBJECTS:${ARITH}sol_omp_m>)
            set_target_properties(${ARITH}sol_fwd_aux PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}sol_fwd_aux PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}fac_mem_dynamic OBJECT ${ARITH}fac_mem_dynamic.F)
            target_include_directories(${ARITH}fac_mem_dynamic PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}fac_mem_dynamic PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}fac_mem_dynamic PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_load> $<TARGET_OBJECTS:${ARITH}static_ptr_m>)
            set_target_properties(${ARITH}fac_mem_dynamic PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_mem_dynamic PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}fac_front_aux OBJECT ${ARITH}fac_front_aux.F)
            target_include_directories(${ARITH}fac_front_aux PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}fac_front_aux PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}fac_front_aux PUBLIC $<TARGET_OBJECTS:${ARITH}lr_type> $<TARGET_OBJECTS:${ARITH}lr_stats> $<TARGET_OBJECTS:${ARITH}mumps_comm_buffer> $<TARGET_OBJECTS:${ARITH}mumps_load> $<TARGET_OBJECTS:${ARITH}mumps_ooc> $<TARGET_OBJECTS:mumps_ooc_common> $<TARGET_OBJECTS:mumps_l0_omp_m> $<TARGET_OBJECTS:mumps_pivnul_mod>)
            set_target_properties(${ARITH}fac_front_aux PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_front_aux PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}ana_driver OBJECT ${ARITH}ana_driver.F)
            target_include_directories(${ARITH}ana_driver PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}ana_driver PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}ana_driver PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_load> $<TARGET_OBJECTS:mumps_static_mapping> $<TARGET_OBJECTS:${ARITH}mumps_struc_def> $<TARGET_OBJECTS:mumps_memory_mod> $<TARGET_OBJECTS:${ARITH}ana_aux_par> $<TARGET_OBJECTS:${ARITH}ana_lr> $<TARGET_OBJECTS:${ARITH}lr_core> $<TARGET_OBJECTS:${ARITH}lr_stats> $<TARGET_OBJECTS:lr_common> $<TARGET_OBJECTS:${ARITH}ana_aux> $<TARGET_OBJECTS:ana_blk_m> $<TARGET_OBJECTS:ana_omp_m>)
            set_target_properties(${ARITH}ana_driver PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}ana_driver PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}fac_driver OBJECT ${ARITH}fac_driver.F)
            target_include_directories(${ARITH}fac_driver PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}fac_driver PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}fac_driver PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_comm_buffer> $<TARGET_OBJECTS:${ARITH}mumps_load> $<TARGET_OBJECTS:${ARITH}mumps_ooc> $<TARGET_OBJECTS:${ARITH}mumps_struc_def> $<TARGET_OBJECTS:${ARITH}fac_sol_l0omp_m> $<TARGET_OBJECTS:${ARITH}lr_stats> $<TARGET_OBJECTS:${ARITH}mumps_lr_data_m> $<TARGET_OBJECTS:mumps_pivnul_mod> $<TARGET_OBJECTS:front_data_mgt_m> $<TARGET_OBJECTS:fac_descband_data_m> $<TARGET_OBJECTS:fac_maprow_data_m> $<TARGET_OBJECTS:${ARITH}fac_sispointers_m>)
            set_target_properties(${ARITH}fac_driver PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_driver PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}fac_mem_alloc_cb OBJECT ${ARITH}fac_mem_alloc_cb.F)
            target_include_directories(${ARITH}fac_mem_alloc_cb PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}fac_mem_alloc_cb PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}fac_mem_alloc_cb PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_load>)
            set_target_properties(${ARITH}fac_mem_alloc_cb PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_mem_alloc_cb PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}fac_mem_free_block_cb OBJECT ${ARITH}fac_mem_free_block_cb.F)
            target_include_directories(${ARITH}fac_mem_free_block_cb PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}fac_mem_free_block_cb PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}fac_mem_free_block_cb PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_load>)
            set_target_properties(${ARITH}fac_mem_free_block_cb PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_mem_free_block_cb PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}fac_mem_stack OBJECT ${ARITH}fac_mem_stack.F)
            target_include_directories(${ARITH}fac_mem_stack PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}fac_mem_stack PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}fac_mem_stack PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_comm_buffer> $<TARGET_OBJECTS:${ARITH}mumps_load> $<TARGET_OBJECTS:${ARITH}mumps_struc_def>)
            set_target_properties(${ARITH}fac_mem_stack PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_mem_stack PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}fac_process_band OBJECT ${ARITH}fac_process_band.F)
            target_include_directories(${ARITH}fac_process_band PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}fac_process_band PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}fac_process_band PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_load> $<TARGET_OBJECTS:${ARITH}mumps_lr_data_m> $<TARGET_OBJECTS:fac_descband_data_m> $<TARGET_OBJECTS:${ARITH}mumps_struc_def>)
            set_target_properties(${ARITH}fac_process_band PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_process_band PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}fac_process_end_facto_slave OBJECT ${ARITH}fac_process_end_facto_slave.F)
            target_include_directories(${ARITH}fac_process_end_facto_slave PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}fac_process_end_facto_slave PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}fac_process_end_facto_slave PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_load> $<TARGET_OBJECTS:fac_maprow_data_m> $<TARGET_OBJECTS:${ARITH}mumps_lr_data_m> $<TARGET_OBJECTS:${ARITH}mumps_struc_def>)
            set_target_properties(${ARITH}fac_process_end_facto_slave PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_process_end_facto_slave PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}fac_process_contrib_type3 OBJECT ${ARITH}fac_process_contrib_type3.F)
            target_include_directories(${ARITH}fac_process_contrib_type3 PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}fac_process_contrib_type3 PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}fac_process_contrib_type3 PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_load> $<TARGET_OBJECTS:${ARITH}mumps_ooc> $<TARGET_OBJECTS:${ARITH}mumps_struc_def>)
            set_target_properties(${ARITH}fac_process_contrib_type3 PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_process_contrib_type3 PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}fac_process_message OBJECT ${ARITH}fac_process_message.F)
            target_include_directories(${ARITH}fac_process_message PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}fac_process_message PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}fac_process_message PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_load> $<TARGET_OBJECTS:${ARITH}mumps_struc_def> $<TARGET_OBJECTS:${ARITH}mumps_comm_buffer>)
            set_target_properties(${ARITH}fac_process_message PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_process_message PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}fac_process_root2slave OBJECT ${ARITH}fac_process_root2slave.F)
            target_include_directories(${ARITH}fac_process_root2slave PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}fac_process_root2slave PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}fac_process_root2slave PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_load> $<TARGET_OBJECTS:${ARITH}mumps_ooc> $<TARGET_OBJECTS:${ARITH}mumps_struc_def>)
            set_target_properties(${ARITH}fac_process_root2slave PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_process_root2slave PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}fac_process_rtnelind OBJECT ${ARITH}fac_process_rtnelind.F)
            target_include_directories(${ARITH}fac_process_rtnelind PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}fac_process_rtnelind PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}fac_process_rtnelind PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_load> $<TARGET_OBJECTS:${ARITH}mumps_struc_def>)
            set_target_properties(${ARITH}fac_process_rtnelind PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_process_rtnelind PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}fac_sol_pool OBJECT ${ARITH}fac_sol_pool.F)
            target_include_directories(${ARITH}fac_sol_pool PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}fac_sol_pool PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}fac_sol_pool PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_load>)
            set_target_properties(${ARITH}fac_sol_pool PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_sol_pool PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}fac_asm_master_ELT_m OBJECT ${ARITH}fac_asm_master_ELT_m.F)
            target_include_directories(${ARITH}fac_asm_master_ELT_m PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}fac_asm_master_ELT_m PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}fac_asm_master_ELT_m PUBLIC $<TARGET_OBJECTS:omp_tps_common_m> $<TARGET_OBJECTS:fac_ibct_data_m> $<TARGET_OBJECTS:fac_asm_build_sort_index_ELT_m> $<TARGET_OBJECTS:lr_common> $<TARGET_OBJECTS:${ARITH}fac_mem_dynamic> $<TARGET_OBJECTS:${ARITH}lr_core> $<TARGET_OBJECTS:${ARITH}ana_lr> $<TARGET_OBJECTS:${ARITH}mumps_lr_data_m> $<TARGET_OBJECTS:${ARITH}mumps_struc_def> $<TARGET_OBJECTS:${ARITH}omp_tps_m> $<TARGET_OBJECTS:${ARITH}mumps_comm_buffer> $<TARGET_OBJECTS:${ARITH}mumps_load>)
            set_target_properties(${ARITH}fac_asm_master_ELT_m PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_asm_master_ELT_m PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}fac_asm_master_m OBJECT ${ARITH}fac_asm_master_m.F)
            target_include_directories(${ARITH}fac_asm_master_m PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}fac_asm_master_m PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}fac_asm_master_m PUBLIC $<TARGET_OBJECTS:omp_tps_common_m> $<TARGET_OBJECTS:fac_ibct_data_m> $<TARGET_OBJECTS:fac_asm_build_sort_index_m> $<TARGET_OBJECTS:lr_common> $<TARGET_OBJECTS:${ARITH}fac_mem_dynamic> $<TARGET_OBJECTS:${ARITH}lr_core> $<TARGET_OBJECTS:${ARITH}ana_lr> $<TARGET_OBJECTS:${ARITH}mumps_lr_data_m> $<TARGET_OBJECTS:${ARITH}mumps_struc_def> $<TARGET_OBJECTS:${ARITH}omp_tps_m> $<TARGET_OBJECTS:${ARITH}mumps_comm_buffer> $<TARGET_OBJECTS:${ARITH}mumps_load>)
            set_target_properties(${ARITH}fac_asm_master_m PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_asm_master_m PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}fac_asm_ELT OBJECT ${ARITH}fac_asm_ELT.F)
            target_include_directories(${ARITH}fac_asm_ELT PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}fac_asm_ELT PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}fac_asm_ELT PUBLIC $<TARGET_OBJECTS:${ARITH}fac_mem_dynamic> $<TARGET_OBJECTS:${ARITH}ana_lr> $<TARGET_OBJECTS:${ARITH}lr_core> $<TARGET_OBJECTS:lr_common>)
            set_target_properties(${ARITH}fac_asm_ELT PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_asm_ELT PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}fac_mem_compress_cb OBJECT ${ARITH}fac_mem_compress_cb.F)
            target_include_directories(${ARITH}fac_mem_compress_cb PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}fac_mem_compress_cb PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}fac_mem_compress_cb PUBLIC $<TARGET_OBJECTS:${ARITH}fac_mem_dynamic>)
            set_target_properties(${ARITH}fac_mem_compress_cb PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_mem_compress_cb PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}fac_process_blocfacto OBJECT ${ARITH}fac_process_blocfacto.F)
            target_include_directories(${ARITH}fac_process_blocfacto PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}fac_process_blocfacto PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}fac_process_blocfacto PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_ooc> $<TARGET_OBJECTS:mumps_ooc_common> $<TARGET_OBJECTS:${ARITH}mumps_load> $<TARGET_OBJECTS:${ARITH}lr_core> $<TARGET_OBJECTS:${ARITH}lr_type> $<TARGET_OBJECTS:${ARITH}lr_stats> $<TARGET_OBJECTS:${ARITH}fac_lr> $<TARGET_OBJECTS:${ARITH}ana_lr> $<TARGET_OBJECTS:${ARITH}mumps_lr_data_m> $<TARGET_OBJECTS:${ARITH}mumps_struc_def> $<TARGET_OBJECTS:${ARITH}fac_mem_dynamic>)
            set_target_properties(${ARITH}fac_process_blocfacto PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_process_blocfacto PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}fac_process_contrib_type1 OBJECT ${ARITH}fac_process_contrib_type1.F)
            target_include_directories(${ARITH}fac_process_contrib_type1 PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}fac_process_contrib_type1 PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}fac_process_contrib_type1 PUBLIC $<TARGET_OBJECTS:${ARITH}fac_mem_dynamic>)
            set_target_properties(${ARITH}fac_process_contrib_type1 PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_process_contrib_type1 PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}fac_process_contrib_type2 OBJECT ${ARITH}fac_process_contrib_type2.F)
            target_include_directories(${ARITH}fac_process_contrib_type2 PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}fac_process_contrib_type2 PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}fac_process_contrib_type2 PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_load> $<TARGET_OBJECTS:${ARITH}mumps_comm_buffer> $<TARGET_OBJECTS:${ARITH}lr_type> $<TARGET_OBJECTS:${ARITH}lr_stats> $<TARGET_OBJECTS:${ARITH}mumps_struc_def> $<TARGET_OBJECTS:${ARITH}fac_mem_dynamic>)
            set_target_properties(${ARITH}fac_process_contrib_type2 PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_process_contrib_type2 PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}fac_process_master2 OBJECT ${ARITH}fac_process_master2.F)
            target_include_directories(${ARITH}fac_process_master2 PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}fac_process_master2 PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}fac_process_master2 PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_load> $<TARGET_OBJECTS:${ARITH}fac_mem_dynamic>)
            set_target_properties(${ARITH}fac_process_master2 PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_process_master2 PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}tools OBJECT ${ARITH}tools.F)
            target_include_directories(${ARITH}tools PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}tools PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}tools PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_load> $<TARGET_OBJECTS:${ARITH}mumps_ooc> $<TARGET_OBJECTS:${ARITH}lr_core> $<TARGET_OBJECTS:${ARITH}fac_mem_dynamic> $<TARGET_OBJECTS:${ARITH}mumps_struc_def> $<TARGET_OBJECTS:${ARITH}static_ptr_m> $<TARGET_OBJECTS:${ARITH}mumps_comm_buffer> $<TARGET_OBJECTS:${ARITH}lr_type> $<TARGET_OBJECTS:${ARITH}fac_lr>)
            set_target_properties(${ARITH}tools PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}tools PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}type3_root OBJECT ${ARITH}type3_root.F)
            target_include_directories(${ARITH}type3_root PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}type3_root PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}type3_root PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_struc_def> $<TARGET_OBJECTS:${ARITH}mumps_ooc> $<TARGET_OBJECTS:${ARITH}mumps_comm_buffer> $<TARGET_OBJECTS:${ARITH}mumps_load> $<TARGET_OBJECTS:${ARITH}fac_mem_dynamic>)
            set_target_properties(${ARITH}type3_root PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}type3_root PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}fac_front_LU_type1 OBJECT ${ARITH}fac_front_LU_type1.F)
            target_include_directories(${ARITH}fac_front_LU_type1 PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}fac_front_LU_type1 PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}fac_front_LU_type1 PUBLIC $<TARGET_OBJECTS:${ARITH}fac_front_aux> $<TARGET_OBJECTS:${ARITH}mumps_ooc> $<TARGET_OBJECTS:${ARITH}fac_lr> $<TARGET_OBJECTS:${ARITH}lr_type> $<TARGET_OBJECTS:${ARITH}lr_stats> $<TARGET_OBJECTS:${ARITH}ana_lr> $<TARGET_OBJECTS:${ARITH}mumps_lr_data_m> $<TARGET_OBJECTS:mumps_l0_omp_m> $<TARGET_OBJECTS:mumps_pivnul_mod>)
            set_target_properties(${ARITH}fac_front_LU_type1 PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_front_LU_type1 PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}fac_front_type2_aux OBJECT ${ARITH}fac_front_type2_aux.F)
            target_include_directories(${ARITH}fac_front_type2_aux PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}fac_front_type2_aux PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}fac_front_type2_aux PUBLIC $<TARGET_OBJECTS:mumps_ooc_common> $<TARGET_OBJECTS:${ARITH}fac_front_aux> $<TARGET_OBJECTS:${ARITH}lr_type> $<TARGET_OBJECTS:${ARITH}mumps_struc_def> $<TARGET_OBJECTS:${ARITH}mumps_comm_buffer> $<TARGET_OBJECTS:${ARITH}mumps_load> $<TARGET_OBJECTS:mumps_comm_ibcast> $<TARGET_OBJECTS:fac_ibct_data_m> $<TARGET_OBJECTS:mumps_pivnul_mod>)
            set_target_properties(${ARITH}fac_front_type2_aux PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_front_type2_aux PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}fac_front_LDLT_type1 OBJECT ${ARITH}fac_front_LDLT_type1.F)
            target_include_directories(${ARITH}fac_front_LDLT_type1 PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}fac_front_LDLT_type1 PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}fac_front_LDLT_type1 PUBLIC $<TARGET_OBJECTS:${ARITH}fac_front_aux> $<TARGET_OBJECTS:${ARITH}mumps_ooc> $<TARGET_OBJECTS:${ARITH}fac_lr> $<TARGET_OBJECTS:${ARITH}lr_type> $<TARGET_OBJECTS:${ARITH}lr_stats> $<TARGET_OBJECTS:${ARITH}ana_lr> $<TARGET_OBJECTS:${ARITH}mumps_lr_data_m> $<TARGET_OBJECTS:mumps_l0_omp_m> $<TARGET_OBJECTS:mumps_pivnul_mod>)
            set_target_properties(${ARITH}fac_front_LDLT_type1 PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_front_LDLT_type1 PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}fac_asm OBJECT ${ARITH}fac_asm.F)
            target_include_directories(${ARITH}fac_asm PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}fac_asm PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}fac_asm PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_load> $<TARGET_OBJECTS:${ARITH}fac_mem_dynamic> $<TARGET_OBJECTS:${ARITH}ana_lr> $<TARGET_OBJECTS:${ARITH}lr_core> $<TARGET_OBJECTS:lr_common> $<TARGET_OBJECTS:${ARITH}fac_front_aux>)
            set_target_properties(${ARITH}fac_asm PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_asm PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}fac_process_blfac_slave OBJECT ${ARITH}fac_process_blfac_slave.F)
            target_include_directories(${ARITH}fac_process_blfac_slave PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}fac_process_blfac_slave PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}fac_process_blfac_slave PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_comm_buffer> $<TARGET_OBJECTS:${ARITH}mumps_load> $<TARGET_OBJECTS:${ARITH}lr_core> $<TARGET_OBJECTS:${ARITH}lr_type> $<TARGET_OBJECTS:${ARITH}fac_lr> $<TARGET_OBJECTS:${ARITH}mumps_lr_data_m> $<TARGET_OBJECTS:${ARITH}mumps_struc_def> $<TARGET_OBJECTS:${ARITH}fac_mem_dynamic> $<TARGET_OBJECTS:${ARITH}fac_front_aux>)
            set_target_properties(${ARITH}fac_process_blfac_slave PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_process_blfac_slave PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}fac_process_blocfacto_LDLT OBJECT ${ARITH}fac_process_blocfacto_LDLT.F)
            target_include_directories(${ARITH}fac_process_blocfacto_LDLT PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}fac_process_blocfacto_LDLT PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}fac_process_blocfacto_LDLT PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_ooc> $<TARGET_OBJECTS:mumps_ooc_common> $<TARGET_OBJECTS:${ARITH}mumps_load> $<TARGET_OBJECTS:${ARITH}mumps_comm_buffer> $<TARGET_OBJECTS:${ARITH}lr_core> $<TARGET_OBJECTS:${ARITH}lr_type> $<TARGET_OBJECTS:${ARITH}lr_stats> $<TARGET_OBJECTS:${ARITH}fac_lr> $<TARGET_OBJECTS:${ARITH}ana_lr> $<TARGET_OBJECTS:${ARITH}mumps_lr_data_m> $<TARGET_OBJECTS:${ARITH}mumps_struc_def> $<TARGET_OBJECTS:${ARITH}fac_mem_dynamic> $<TARGET_OBJECTS:${ARITH}fac_front_aux>)
            set_target_properties(${ARITH}fac_process_blocfacto_LDLT PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_process_blocfacto_LDLT PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}fac_process_maprow OBJECT ${ARITH}fac_process_maprow.F)
            target_include_directories(${ARITH}fac_process_maprow PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}fac_process_maprow PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}fac_process_maprow PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_comm_buffer> $<TARGET_OBJECTS:${ARITH}mumps_load> $<TARGET_OBJECTS:${ARITH}mumps_lr_data_m> $<TARGET_OBJECTS:${ARITH}fac_mem_dynamic> $<TARGET_OBJECTS:${ARITH}fac_front_aux> $<TARGET_OBJECTS:fac_maprow_data_m> $<TARGET_OBJECTS:${ARITH}mumps_struc_def> $<TARGET_OBJECTS:${ARITH}lr_type> $<TARGET_OBJECTS:${ARITH}lr_stats>)
            set_target_properties(${ARITH}fac_process_maprow PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_process_maprow PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}fac_determinant OBJECT ${ARITH}fac_determinant.F)
            target_include_directories(${ARITH}fac_determinant PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}fac_determinant PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}fac_determinant PUBLIC $<TARGET_OBJECTS:${ARITH}fac_front_aux>)
            set_target_properties(${ARITH}fac_determinant PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_determinant PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}fac_front_LU_type2 OBJECT ${ARITH}fac_front_LU_type2.F)
            target_include_directories(${ARITH}fac_front_LU_type2 PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}fac_front_LU_type2 PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}fac_front_LU_type2 PUBLIC $<TARGET_OBJECTS:${ARITH}fac_front_aux> $<TARGET_OBJECTS:${ARITH}fac_front_type2_aux> $<TARGET_OBJECTS:${ARITH}mumps_ooc> $<TARGET_OBJECTS:${ARITH}mumps_comm_buffer> $<TARGET_OBJECTS:mumps_comm_ibcast> $<TARGET_OBJECTS:${ARITH}fac_lr> $<TARGET_OBJECTS:${ARITH}lr_core> $<TARGET_OBJECTS:${ARITH}lr_type> $<TARGET_OBJECTS:${ARITH}lr_stats> $<TARGET_OBJECTS:${ARITH}ana_lr> $<TARGET_OBJECTS:${ARITH}mumps_lr_data_m> $<TARGET_OBJECTS:${ARITH}mumps_struc_def> $<TARGET_OBJECTS:mumps_pivnul_mod>)
            set_target_properties(${ARITH}fac_front_LU_type2 PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_front_LU_type2 PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}fac_front_LDLT_type2 OBJECT ${ARITH}fac_front_LDLT_type2.F)
            target_include_directories(${ARITH}fac_front_LDLT_type2 PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}fac_front_LDLT_type2 PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}fac_front_LDLT_type2 PUBLIC $<TARGET_OBJECTS:${ARITH}fac_front_aux> $<TARGET_OBJECTS:${ARITH}fac_front_type2_aux> $<TARGET_OBJECTS:${ARITH}mumps_ooc> $<TARGET_OBJECTS:${ARITH}mumps_comm_buffer> $<TARGET_OBJECTS:${ARITH}mumps_load> $<TARGET_OBJECTS:${ARITH}fac_lr> $<TARGET_OBJECTS:${ARITH}lr_type> $<TARGET_OBJECTS:${ARITH}lr_stats> $<TARGET_OBJECTS:${ARITH}ana_lr> $<TARGET_OBJECTS:${ARITH}mumps_lr_data_m> $<TARGET_OBJECTS:${ARITH}mumps_struc_def> $<TARGET_OBJECTS:mumps_pivnul_mod>)
            set_target_properties(${ARITH}fac_front_LDLT_type2 PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_front_LDLT_type2 PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}fac_omp_m OBJECT ${ARITH}fac_omp_m.F)
            target_include_directories(${ARITH}fac_omp_m PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}fac_omp_m PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}fac_omp_m PUBLIC $<TARGET_OBJECTS:${ARITH}fac_asm_master_m> $<TARGET_OBJECTS:${ARITH}fac_asm_master_ELT_m> $<TARGET_OBJECTS:${ARITH}fac_front_LU_type1> $<TARGET_OBJECTS:${ARITH}fac_front_LDLT_type1> $<TARGET_OBJECTS:${ARITH}mumps_load> $<TARGET_OBJECTS:${ARITH}omp_tps_m> $<TARGET_OBJECTS:${ARITH}lr_stats> $<TARGET_OBJECTS:${ARITH}mumps_struc_def> $<TARGET_OBJECTS:omp_tps_common_m> $<TARGET_OBJECTS:mumps_l0_omp_m> $<TARGET_OBJECTS:mumps_pivnul_mod> $<TARGET_OBJECTS:${ARITH}fac_mem_dynamic>)
            set_target_properties(${ARITH}fac_omp_m PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_omp_m PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}fac_par_m OBJECT ${ARITH}fac_par_m.F)
            target_include_directories(${ARITH}fac_par_m PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}fac_par_m PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}fac_par_m PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_load> $<TARGET_OBJECTS:${ARITH}mumps_ooc> $<TARGET_OBJECTS:${ARITH}fac_asm_master_m> $<TARGET_OBJECTS:${ARITH}fac_asm_master_ELT_m> $<TARGET_OBJECTS:${ARITH}omp_tps_m> $<TARGET_OBJECTS:${ARITH}fac_front_LU_type1> $<TARGET_OBJECTS:${ARITH}fac_front_LU_type2> $<TARGET_OBJECTS:${ARITH}fac_front_LDLT_type1> $<TARGET_OBJECTS:${ARITH}fac_front_LDLT_type2> $<TARGET_OBJECTS:${ARITH}fac_mem_dynamic> $<TARGET_OBJECTS:${ARITH}mumps_struc_def> $<TARGET_OBJECTS:${ARITH}lr_stats> $<TARGET_OBJECTS:omp_tps_common_m> $<TARGET_OBJECTS:mumps_l0_omp_m> $<TARGET_OBJECTS:mumps_pivnul_mod> $<TARGET_OBJECTS:${ARITH}mumps_comm_buffer>)
            set_target_properties(${ARITH}fac_par_m PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_par_m PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(${ARITH}fac_b OBJECT ${ARITH}fac_b.F)
            target_include_directories(${ARITH}fac_b PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/modules ${MUMPS_INCLUDEDIR})
            set_target_properties(${ARITH}fac_b PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(${ARITH}fac_b PUBLIC $<TARGET_OBJECTS:${ARITH}mumps_load> $<TARGET_OBJECTS:${ARITH}mumps_comm_buffer> $<TARGET_OBJECTS:${ARITH}fac_sispointers_m> $<TARGET_OBJECTS:mumps_pivnul_mod> $<TARGET_OBJECTS:omp_tps_common_m> $<TARGET_OBJECTS:${ARITH}omp_tps_m> $<TARGET_OBJECTS:${ARITH}fac_omp_m> $<TARGET_OBJECTS:${ARITH}mumps_struc_def> $<TARGET_OBJECTS:${ARITH}mumps_ooc> $<TARGET_OBJECTS:${ARITH}fac_asm_master_m> $<TARGET_OBJECTS:${ARITH}fac_asm_master_ELT_m> $<TARGET_OBJECTS:${ARITH}fac_front_LDLT_type1> $<TARGET_OBJECTS:${ARITH}fac_front_LDLT_type2> $<TARGET_OBJECTS:${ARITH}fac_front_LU_type1> $<TARGET_OBJECTS:${ARITH}fac_front_LU_type2> $<TARGET_OBJECTS:${ARITH}fac_par_m>)
            set_target_properties(${ARITH}fac_b PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(${ARITH}fac_b PRIVATE pord metis::metis mpiseq MKL::MKL)     


            add_library(lib${ARITH}mumps STATIC ${ARITH}sol_distsol.F ${ARITH}ana_reordertree.F ${ARITH}fac_diag.F ${ARITH}fac_mem_stack_aux.F ${ARITH}fac_process_bf.F ${ARITH}fac_scalings_simScaleAbs.F ${ARITH}fac_scalings_simScale_util.F ${ARITH}fac_type3_symmetrize.F ${ARITH}mumps_iXamax.F ${ARITH}ana_mtrans.F ${ARITH}sol_matvec.F ${ARITH}sol_root_parallel.F)
            target_include_directories(lib${ARITH}mumps PUBLIC $<BUILD_INTERFACE:${MUMPS_INCLUDEDIR}> $<INSTALL_INTERFACE:${HEADER_INSTALL_DIR}>)
            target_include_directories(lib${ARITH}mumps PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/modules)
            set_target_properties(lib${ARITH}mumps PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules)
            target_link_libraries(lib${ARITH}mumps PRIVATE $<TARGET_OBJECTS:${ARITH}ana_aux> $<TARGET_OBJECTS:${ARITH}ana_aux_par> $<TARGET_OBJECTS:${ARITH}ana_lr> $<TARGET_OBJECTS:${ARITH}fac_asm_master_ELT_m> $<TARGET_OBJECTS:${ARITH}fac_asm_master_m> $<TARGET_OBJECTS:${ARITH}fac_front_aux> $<TARGET_OBJECTS:${ARITH}fac_front_LU_type1> $<TARGET_OBJECTS:${ARITH}fac_front_LU_type2> $<TARGET_OBJECTS:${ARITH}fac_front_LDLT_type1> $<TARGET_OBJECTS:${ARITH}fac_front_LDLT_type2> $<TARGET_OBJECTS:${ARITH}fac_front_type2_aux> $<TARGET_OBJECTS:${ARITH}fac_sispointers_m> $<TARGET_OBJECTS:${ARITH}fac_lr> $<TARGET_OBJECTS:${ARITH}fac_mem_dynamic> $<TARGET_OBJECTS:${ARITH}fac_omp_m> $<TARGET_OBJECTS:${ARITH}fac_par_m> $<TARGET_OBJECTS:${ARITH}fac_sol_l0omp_m> $<TARGET_OBJECTS:${ARITH}lr_core> $<TARGET_OBJECTS:${ARITH}lr_stats> $<TARGET_OBJECTS:${ARITH}lr_type> $<TARGET_OBJECTS:${ARITH}mumps_comm_buffer> $<TARGET_OBJECTS:${ARITH}mumps_config_file> $<TARGET_OBJECTS:${ARITH}mumps_load> $<TARGET_OBJECTS:${ARITH}mumps_lr_data_m> $<TARGET_OBJECTS:${ARITH}mumps_ooc_buffer> $<TARGET_OBJECTS:${ARITH}mumps_ooc> $<TARGET_OBJECTS:${ARITH}mumps_sol_es> $<TARGET_OBJECTS:${ARITH}mumps_save_restore> $<TARGET_OBJECTS:${ARITH}mumps_save_restore_files> $<TARGET_OBJECTS:${ARITH}mumps_struc_def> $<TARGET_OBJECTS:${ARITH}omp_tps_m> $<TARGET_OBJECTS:${ARITH}sol_lr> $<TARGET_OBJECTS:${ARITH}sol_omp_m> $<TARGET_OBJECTS:${ARITH}static_ptr_m> $<TARGET_OBJECTS:${ARITH}mumps_mpi3_mod> $<TARGET_OBJECTS:${ARITH}ini_driver> $<TARGET_OBJECTS:${ARITH}ana_driver> $<TARGET_OBJECTS:${ARITH}fac_driver> $<TARGET_OBJECTS:${ARITH}sol_driver> $<TARGET_OBJECTS:${ARITH}sol_distrhs> $<TARGET_OBJECTS:${ARITH}end_driver> $<TARGET_OBJECTS:${ARITH}ana_aux_ELT> $<TARGET_OBJECTS:${ARITH}ana_dist_m> $<TARGET_OBJECTS:${ARITH}ana_LDLT_preprocess> $<TARGET_OBJECTS:${ARITH}arrowheads> $<TARGET_OBJECTS:${ARITH}bcast_int> $<TARGET_OBJECTS:${ARITH}fac_asm_ELT> $<TARGET_OBJECTS:${ARITH}fac_asm> $<TARGET_OBJECTS:${ARITH}fac_b> $<TARGET_OBJECTS:${ARITH}fac_distrib_distentry> $<TARGET_OBJECTS:${ARITH}fac_dist_arrowheads_omp> $<TARGET_OBJECTS:${ARITH}fac_distrib_ELT> $<TARGET_OBJECTS:${ARITH}fac_lastrtnelind> $<TARGET_OBJECTS:${ARITH}fac_mem_alloc_cb> $<TARGET_OBJECTS:${ARITH}fac_mem_compress_cb> $<TARGET_OBJECTS:${ARITH}fac_mem_free_block_cb> $<TARGET_OBJECTS:${ARITH}fac_mem_stack> $<TARGET_OBJECTS:${ARITH}fac_process_band> $<TARGET_OBJECTS:${ARITH}fac_process_blfac_slave> $<TARGET_OBJECTS:${ARITH}fac_process_blocfacto_LDLT> $<TARGET_OBJECTS:${ARITH}fac_process_blocfacto> $<TARGET_OBJECTS:${ARITH}fac_process_end_facto_slave> $<TARGET_OBJECTS:${ARITH}fac_process_contrib_type1> $<TARGET_OBJECTS:${ARITH}fac_process_contrib_type2> $<TARGET_OBJECTS:${ARITH}fac_process_contrib_type3> $<TARGET_OBJECTS:${ARITH}fac_process_maprow> $<TARGET_OBJECTS:${ARITH}fac_process_master2> $<TARGET_OBJECTS:${ARITH}fac_process_message> $<TARGET_OBJECTS:${ARITH}fac_process_root2slave> $<TARGET_OBJECTS:${ARITH}fac_process_root2son> $<TARGET_OBJECTS:${ARITH}fac_process_rtnelind> $<TARGET_OBJECTS:${ARITH}fac_root_parallel> $<TARGET_OBJECTS:${ARITH}fac_scalings> $<TARGET_OBJECTS:${ARITH}fac_determinant> $<TARGET_OBJECTS:${ARITH}fac_sol_pool> $<TARGET_OBJECTS:${ARITH}ini_defaults> $<TARGET_OBJECTS:${ARITH}mumps_c> $<TARGET_OBJECTS:${ARITH}mumps_driver> $<TARGET_OBJECTS:${ARITH}mumps_f77> $<TARGET_OBJECTS:${ARITH}mumps_gpu> $<TARGET_OBJECTS:${ARITH}ooc_panel_piv> $<TARGET_OBJECTS:${ARITH}rank_revealing> $<TARGET_OBJECTS:${ARITH}sol_aux> $<TARGET_OBJECTS:${ARITH}sol_bwd_aux> $<TARGET_OBJECTS:${ARITH}sol_bwd> $<TARGET_OBJECTS:${ARITH}sol_c> $<TARGET_OBJECTS:${ARITH}sol_fwd_aux> $<TARGET_OBJECTS:${ARITH}sol_fwd> $<TARGET_OBJECTS:${ARITH}tools> $<TARGET_OBJECTS:${ARITH}type3_root>)
            set_target_properties(lib${ARITH}mumps PROPERTIES LINKER_LANGUAGE C)
            target_link_libraries(lib${ARITH}mumps PUBLIC libmumps_common mumps::pord metis::metis mumps::mpiseq MKL::MKL)
            target_compile_definitions(${ARITH}mumps_c PRIVATE MUMPS_ARITH=MUMPS_ARITH_${ARITH})
        endforeach(ARITH ${ARCHS})
