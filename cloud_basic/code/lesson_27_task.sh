#! /bin/bash

# create a directory
if [ ! -d lesson_27 ]; then
    mkdir lesson_27
fi


for i in {1..199}; do
    rm lesson_27/file_$i.txt
done
echo "199 files removed"
