#! /bin/bash

# get the file to search and the seconds to wait
file_to_search=$1
seconds_to_wait=$2

# wait for the file to search to be created
for seconds in $(seq 1 $seconds_to_wait); do
    if [ -e $file_to_search ]; then
        echo "File $file_to_search found"
        exit 0
    fi
    echo "$((seconds_to_wait - seconds)) seconds left"
    sleep 1
done

echo "File $file_to_search not found"
exit 1