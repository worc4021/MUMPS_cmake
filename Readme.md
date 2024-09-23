# Overview

This skeleton repo requires to be populated with the licensed MUMPS source code. The folders with `CMakeLists.txt` files mirror where they need to be within the source tree of MUMPS.

The main complexity of compiling MUMPS on windows with cmake while retaining your mental health is extracting the build of `libdmumps` etc from `src/Makefile`. This is done with the parser project in `./buildutilities`. To run it, simply install the dependencies and run `python Driver.py repopath/src/Makefile` and a template `CMakeLists.txt` is genereted in your current directory. This build worked for MUMPS 5.7.3.

## Problems with linux

- There are issues around name mangling when trying to build the cmake project on linux. 
- Some of the fortran files use modules, in which case the compiler needs to resolve the module name not the symbol name and fails. 
- Added some printout that resolves global symbols based on the compiler in use. However, this doesn't do anything since we have this module problem and the module of the symbol that we are resolving needs to be known. This leads to some chicken and egg problem. We need to know the symbol name and the module that contains it for all symbols. But the module is in fortran and the caller in c..