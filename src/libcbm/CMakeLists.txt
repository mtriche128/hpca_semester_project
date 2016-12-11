# This cmake script builds the "C Benchmarks Library".

cmake_minimum_required (VERSION 3.2)

# list all source files here
set(SRC_LIST libcbm.c)

# build the library
add_library(${LIBCBM_NAME} SHARED ${SRC_LIST})

# specifiy the installation path for the library
install(TARGETS ${LIBCBM_NAME} DESTINATION ${LIB_INSTALL_DIR})