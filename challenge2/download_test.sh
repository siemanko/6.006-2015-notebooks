#!/bin/bash

# stop script on error and print it
set -e
# inform me of undefined variables
set -u
# handle cascading failures well
set -o pipefail

 curl -o tests.zip "http://main.edu.pl/en/user.phtml?op=tests&c=1700&task=633"
 unzip tests.zip -d tests
