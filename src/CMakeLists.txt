# Propogate the build process to each source code component.

cmake_minimum_required (VERSION 3.7)

# build the "C Benchmarks Library"
add_subdirectory(libcbm)

# process the python interface for the "C Benchmarks Library"
add_subdirectory(pycbm)