# Process the python interface for the "C Benchmarks Library".

cmake_minimum_required (VERSION 3.7)

# process the python interface script
configure_file(pycbm.py.in pycbm.py @ONLY)

# specifiy the installation path for the library
install(FILES 
        "${CMAKE_CURRENT_BINARY_DIR}/pycbm.py" 
        DESTINATION 
        ${MODULE_INSTALL_DIR})