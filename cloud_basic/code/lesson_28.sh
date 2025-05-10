#! /bin/bash

# while true; do
#     sleep 1
#     echo "waiting for ctrl+c"
# done

while [ ! -e "stop.txt" ]; do
    echo "file not found"
    sleep 1
done
echo "file found"



