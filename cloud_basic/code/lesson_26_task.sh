#!/bin/bash


user_name=1
password="thisispassword"
age=20

if [ $user_name == 1 -a $password == "thisispassword" -a $age -ge 18 ]; then
    echo "login successful"
    if [ $age -ge 18 ]; then
        echo "you are an adult"
    else
        echo "you are not an adult"
    fi
else
    echo "login failed"
fi

dir_name="."
file_name="lesson_26.sh"

if [ -d $dir_name ]; then
    echo "directory exists"
fi

if [ -f $file_name ]; then
    echo "file exists"
fi









