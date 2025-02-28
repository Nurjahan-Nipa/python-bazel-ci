#!/bin/bash
set -e

pip install black
#black --check src/ tests/


# Get Bazel's execution environment path
PROJECT_ROOT=$(pwd)

# Locate source and test files in Bazel's sandbox environment
SRC_DIR="$PROJECT_ROOT/src"
TESTS_DIR="$PROJECT_ROOT/tests"

# Check if directories exist before running Black
if [ -d "$SRC_DIR" ] && [ -d "$TESTS_DIR" ]; then
    black --check "$SRC_DIR" "$TESTS_DIR"
else
    echo "No files to format: exiting."
fi
