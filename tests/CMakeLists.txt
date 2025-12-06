# Find test framework
find_package(GTest REQUIRED)

# Test executable
add_executable(tests
    test_commons.cpp
)

# Link test framework and production code library
target_link_libraries(tests PRIVATE
    GTest::gtest
    GTest::gtest_main
    FinanceDataProcessor_lib
)

# Register tests with CTest
include(GoogleTest)
gtest_discover_tests(tests)