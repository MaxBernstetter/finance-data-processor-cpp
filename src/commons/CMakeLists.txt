# Commons library sources
set(COMMONS_SOURCES
    commons.cpp
)

set(COMMONS_HEADERS
    commons.h
)

# Create commons library
add_library(commons
    ${COMMONS_SOURCES}
    ${COMMONS_HEADERS}
)

# Set include directories so other targets can find commons.h
target_include_directories(commons PUBLIC
    ${CMAKE_CURRENT_SOURCE_DIR}
)

