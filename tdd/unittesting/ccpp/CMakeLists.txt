cmake_minimum_required(VERSION 3.21)

include(CMakeSettings.cmake)

project(AI)

include(CTest)
include(CMakeTests.cmake)
enable_testing()

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY "${CMAKE_SOURCE_DIR}/bin")

include_directories(
    "include"
    "lib/include"
)


add_executable(${CMAKE_PROJECT_NAME} src/Main.cpp src/App.cpp)