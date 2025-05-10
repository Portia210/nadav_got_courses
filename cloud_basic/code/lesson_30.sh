#! /bin/bash

# environment variables


# see all environment variables
# env
# or
# printenv

# see a specific environment variable
echo "VAR_NAME 1st try: $VAR_NAME"  

# set an environment variable
export VAR_NAME="my value"
echo "VAR_NAME 2nd try: $VAR_NAME"

# unset an environment variable
unset VAR_NAME


