#!/bin/sh
set -e
echo "Cleaning sample_repo..."
make -C "$(dirname "$0")/.." clean
