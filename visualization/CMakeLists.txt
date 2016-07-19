cmake_minimum_required(VERSION 3.5)
project(visualization)
set(CMAKE_C_FLAGS "-lrt -lSDL2")
add_executable(visualization visualization.c)
