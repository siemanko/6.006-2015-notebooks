#!/bin/bash

# stop script on error and print it
set -e
# inform me of undefined variables
set -u
# handle cascading failures well
set -o pipefail

SCRIPT_DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

for filename in `ls $SCRIPT_DIR/tests/*.in | sort --version-sort -f`; do
    output_filename=${filename::-3}.out
    time $@ < $filename | diff -bs - $output_filename
done
