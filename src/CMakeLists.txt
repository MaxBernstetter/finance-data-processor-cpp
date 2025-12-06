# Include commons subdirectory
add_subdirectory(commons)

# Protobuf generated files
set(PROTO_CPP_DIR "${CMAKE_SOURCE_DIR}/../finance-proto-models/build/cpp")

# Recursively find all .pb.cc files
file(GLOB_RECURSE PROTO_SOURCES "${PROTO_CPP_DIR}/*.pb.cc")
if(NOT PROTO_SOURCES)
    message(FATAL_ERROR "No .pb.cc files found in ${PROTO_CPP_DIR}. Run build.sh cpp first.")
endif()

# Create protobuf library (must be before target_* commands)
add_library(proto_models STATIC ${PROTO_SOURCES})

# Set include directories for protobuf headers
# Add both: direct path for generated files to find each other, and project root for user includes
target_include_directories(proto_models PUBLIC
    ${PROTO_CPP_DIR}              # For generated files to find each other (relative includes)
    ${CMAKE_SOURCE_DIR}/..        # Project root for finance-proto-models/build/cpp/... includes
)

# Link protobuf library (needed to compile the .pb.cc files)
target_link_libraries(proto_models PUBLIC
    protobuf::libprotobuf
)

# Add library target as INTERFACE library (aggregates commons and dependencies)
# This allows the main library to exist even when it has no sources of its own
add_library(${PROJECT_NAME}_lib INTERFACE)

# Link commons to the main library (INTERFACE since this is an INTERFACE library)
target_link_libraries(${PROJECT_NAME}_lib INTERFACE
    commons
    proto_models
)

# Link dependencies to library (INTERFACE since this is an INTERFACE library)
target_link_libraries(${PROJECT_NAME}_lib INTERFACE
    fmt::fmt-header-only
    magic_enum::magic_enum
    spdlog::spdlog
)

# Executable source files
set(EXE_SOURCES
    main.cpp
)

# Add executable that links to the library
add_executable(${PROJECT_NAME}
    ${EXE_SOURCES}
)

# Link the library to the executable
target_link_libraries(${PROJECT_NAME} PRIVATE
    ${PROJECT_NAME}_lib
)

# Set output directory to build root (not build/src/)
set_target_properties(${PROJECT_NAME} PROPERTIES
    RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}
    OUTPUT_NAME "finance-data-processor"
)