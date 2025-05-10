#!/bin/bash

# conditionals

# if [ condition ]
# then
#     command
# fi

condition=true

if [ $condition == true ]; then
    echo "condition is true"
else
    echo "condition is false"
fi # fi is the end of the if statement (opposite of if)

number=1

if [ $number -eq 1 ]; then
    echo "number is 1"
elif [ $number -eq 2 ]; then
    echo "number is 2"
else
    echo "number is not 1 or 2"
fi


# operators
# = means equal
# != means not equal
# -z means empty


# statments operators
# -eq = equal
# -ne = not equal
# -gt = greater than
# -lt = less than
# -ge = greater than or equal to
# -le = less than or equal to


# example
if [ $condition != true ]; then
    echo "condition is not true"
elif [ $number -ne 1 ]; then
    echo "number is not 1"
else
    echo "number is 1"
fi

# bool operators
# -a = and
# -o = or
# ! = not

# example
if [ $condition != true -a $number -ne 1 ]; then
    echo "condition is not true and number is not 1"
fi

empty_string=""

if [ -z $empty_string ]; then
    echo "empty_string is empty"
else
    echo "empty_string is not empty"
fi


# file operators
# -e = exists
# -d = directory
# -f = file
# -r = readable
# -w = writable
# -x = executable

file="lesson_26.sh"

if [ -x $file ]; then
    # echo the permission of the file
    echo "file is executable $(ls -l $file)"
else
    echo "file is not executable"
fi




# logical operators
# && = and
# || = or
# ! = not

