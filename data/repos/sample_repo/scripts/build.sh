#!/bin/sh
set -e
echo "Building sample_repo..."
make -C "$(dirname "$0")/.."
