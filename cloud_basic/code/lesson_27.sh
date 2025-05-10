#!/bin/bash

# loops

# for loop
for i in 1 2 3 4 5; do
    echo "i is $i"
done

# itarators in bash
for i in {1..5}; do
    # pass
    :
done

# for loop with range and step
for i in {1..5..2}; do
    # pass
    :
done

fruits="apple banana cherry"
for fruit in $fruits; do
    echo "fruit is $fruit"
done

fruits=("apple" "banana" "cherry")

for fruit in ${fruits[@]}; do
    echo "fruit is $fruit"
done

# create a directory
if [ ! -d lesson_27 ]; then
    mkdir lesson_27
fi
# while loop
i=1
while [ $i -le 5 ]; do
    touch lesson_27/file_$i.txt
    i=$((i+1))
done

# remove all the files in the directory in a loop
for file in lesson_27/*; do
    echo "removing $file"
    rm $file
done







