cmake_minimum_required(VERSION 4.1.2)
project(FinanceDataProcessor VERSION 1.0.0 LANGUAGES CXX)
set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

if(CMAKE_BUILD_TYPE STREQUAL "Debug")
    # Maximum debug information for line-by-line debugging
    # -g3: Maximum debug info including macro definitions
    # -glldb: LLDB-optimized debug format
    # -O0: No optimization (critical for accurate debugging)
    # -fno-omit-frame-pointer: Preserve frame pointers for better stack traces
    # -fno-inline: Don't inline functions (allows stepping into all functions)
    # -fno-optimize-sibling-calls: Preserve call stack structure
    # -fstandalone-debug: Include all debug info (not just what's referenced)
    set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -g3 -glldb -O0 -fno-omit-frame-pointer -fno-inline -fno-optimize-sibling-calls -fstandalone-debug")
endif()

include(dependencies.cmake)
add_subdirectory(../src src)
option(BUILD_TESTING "Build the testing tree" OFF)

if(BUILD_TESTING)
    enable_testing()
    add_subdirectory(../tests tests)
endif()