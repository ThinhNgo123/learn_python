#!/bin/sh -e

export CXX=clang++
export CC=clang

# Silence a git warning
git config --global advice.detachedHead false

DEPENDENCIES_ROOT="/tmp/openmw-deps"

QT_PATH=$(brew --prefix qt@5)
ICU_PATH=$(brew --prefix icu4c)
OPENAL_PATH=$(brew --prefix openal-soft)
CCACHE_EXECUTABLE=$(brew --prefix ccache)/bin/ccache
mkdir build
cd build

cmake \
-D CMAKE_PREFIX_PATH="$DEPENDENCIES_ROOT;$QT_PATH;$OPENAL_PATH" \
-D CMAKE_C_COMPILER_LAUNCHER="$CCACHE_EXECUTABLE" \
-D CMAKE_CXX_COMPILER_LAUNCHER="$CCACHE_EXECUTABLE" \
-D CMAKE_CXX_FLAGS="-stdlib=libc++" \
-D CMAKE_C_FLAGS_RELEASE="-g -O0" \
-D CMAKE_CXX_FLAGS_RELEASE="-g -O0" \
-D CMAKE_OSX_DEPLOYMENT_TARGET="11" \
-D CMAKE_BUILD_TYPE=RELEASE \
-D OPENMW_OSX_DEPLOYMENT=TRUE \
-D OPENMW_USE_SYSTEM_RECASTNAVIGATION=TRUE \
-D BUILD_OPENMW=TRUE \
-D BUILD_OPENCS=TRUE \
-D BUILD_ESMTOOL=TRUE \
-D BUILD_BSATOOL=TRUE \
-D BUILD_ESSIMPORTER=TRUE \
-D BUILD_NIFTEST=TRUE \
-D BUILD_NAVMESHTOOL=TRUE \
-D BUILD_BULLETOBJECTTOOL=TRUE \
-D ICU_ROOT="$ICU_PATH" \
-G"Unix Makefiles" \
..