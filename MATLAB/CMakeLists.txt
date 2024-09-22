include(FindMatlab)

set(ARCHS)
list(APPEND ARCHS "d" "z")

foreach(ARITH ${ARCHS})
    matlab_add_mex( NAME ${ARITH}mumps_mex
                    SRC mumpsmex.c
                    OUTPUT_NAME ${ARITH}mumpsmex
                    LINK_TO ${ARITH}mumps
                    R2017b
                    )
    target_compile_definitions(${ARITH}mumps_mex PRIVATE MUMPS_ARITH=MUMPS_ARITH_${ARITH})
endforeach(ARITH ${ARCHS})


