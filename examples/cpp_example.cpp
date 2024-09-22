/*
 *
 *  This file is part of MUMPS 5.7.3, released
 *  on Mon Jul 15 11:44:21 UTC 2024
 *
 */
/* Example program using the C interface to the 
 * double real arithmetic version of MUMPS, dmumps_c.
 * We solve the system A x = RHS with
 *   A = diag(1 2) and RHS = [1 4]^T
 * Solution is [1 2]^T */
#include <stdio.h>
#include <string.h>
#include <gtest/gtest.h>
#include "FCmangle.h"
#include "mpi.h"
#include "dmumps_c.h"
#define JOB_INIT -1
#define JOB_END -2
#define USE_COMM_WORLD -987654

#define FC_main FC_GLOBAL(main,MAIN)

TEST(dmumps_c, cpp_example) {

  DMUMPS_STRUC_C id;
  MUMPS_INT n = 2;
  MUMPS_INT8 nnz = 2;
  MUMPS_INT irn[] = {1,2};
  MUMPS_INT jcn[] = {1,2};
  double a[2];
  double rhs[2];

/* When compiling with -DINTSIZE64, MUMPS_INT is 64-bit but MPI
   ilp64 versions normally still require standard int for C */
/* MUMPS_INT myid, ierr; */
  int myid, ierr;

  int error = 0;
    char** argv;
  ierr = MPI_Init(&error, &argv); // Meaningless call since we build without MPI
  ierr = MPI_Comm_rank(MPI_COMM_WORLD, &myid);
  /* Define A and rhs */
  rhs[0]=1.0;rhs[1]=4.0;
  a[0]=1.0;a[1]=2.0;

  /* Initialize a MUMPS instance. Use MPI_COMM_WORLD */
  id.comm_fortran=USE_COMM_WORLD;
  id.par=1; id.sym=0;
  id.job=JOB_INIT;
  dmumps_c(&id);

  /* Define the problem on the host */
  if (myid == 0) {
    id.n = n; id.nnz =nnz; id.irn=irn; id.jcn=jcn;
    id.a = a; id.rhs = rhs;
  }
#define ICNTL(I) icntl[(I)-1] /* macro s.t. indices match documentation */
  /* No outputs */
  id.ICNTL(1)=-1; id.ICNTL(2)=-1; id.ICNTL(3)=-1; id.ICNTL(4)=0;

  /* Call the MUMPS package (analyse, factorization and solve). */
  id.job=6;
  dmumps_c(&id);
  if (id.infog[0]<0) {
    printf(" (PROC %d) ERROR RETURN: \tINFOG(1)= %d\n\t\t\t\tINFOG(2)= %d\n",
        myid, id.infog[0], id.infog[1]);
    error = 1;
  }

  /* Terminate instance. */
  id.job=JOB_END;
  dmumps_c(&id);
  
  if (myid == 0) {
    EXPECT_TRUE(0 == error);
  }
  ierr = MPI_Finalize();
  SUCCEED();
}


int FC_main(int argc, char **argv) {
  return 0;
}

int main(int argc, char **argv) {
  FC_main(argc, argv);
  testing::InitGoogleTest();
  return RUN_ALL_TESTS();
}