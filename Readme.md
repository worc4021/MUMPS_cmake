# Overview

This skeleton repo requires to be populated with the licensed MUMPS source code. The folders with `CMakeLists.txt` files mirror where they need to be within the source tree of MUMPS.

The main complexity of compiling MUMPS on windows with cmake while retaining your mental health is extracting the build of `libdmumps` etc from `src/Makefile`. This is done with the parser project in `./buildutilities`. To run it, simply install the dependencies and run `python Driver.py repopath/src/Makefile` and a template `CMakeLists.txt` is genereted in your current directory. This build worked for MUMPS 5.7.3.