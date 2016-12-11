# This is the root cmake script for the HPCA semester project.

cmake_minimum_required (VERSION 3.7)

# set the project's name
project (hpca_semester_project)

# ------------------------------------------------------------------------------
# Set build parameters.

set(LIB_INSTALL_DIR   
    "${CMAKE_SOURCE_DIR}/lib" 
    CACHE STRING      
    "Install directory for libraries.")

set(MODULE_INSTALL_DIR   
    "${CMAKE_SOURCE_DIR}/module" 
    CACHE STRING      
    "Install directory for python modules.")
    
set(LIBCBM_NAME       
    "cbm" 
    CACHE STRING
    "Output name for the 'C Benchmarks Library'. (lib<output_name>.so)")
    
set(LIBCBM_PATH    "${LIB_INSTALL_DIR}/lib${LIBCBM_NAME}.so")
set(UNINSTALL_PATH "${CMAKE_SOURCE_DIR}/bin/uninstall")
set(UNINSTALL_ARG  "${PROJECT_BINARY_DIR}/install_manifest.txt")

################################################################################
# Add custom build targets.                                                    #                        
################################################################################
    
add_custom_target(uninstall COMMAND ${UNINSTALL_PATH} ${UNINSTALL_ARG})

################################################################################
# Add subdirectories to the build process.                                     #                        
################################################################################

# build and process source files
add_subdirectory(src)
