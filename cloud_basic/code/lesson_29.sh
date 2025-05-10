#! /bin/bash

for seconds in {1..10}; do
    if [ -e "stop.txt" ]; then
        echo "stop.txt found"
        exit 0
    fi
    echo "waiting for $seconds seconds"
    sleep 1
done
echo "time's up"

# remove all txt files
find . -maxdepth 1 -name "*.txt" -delete




