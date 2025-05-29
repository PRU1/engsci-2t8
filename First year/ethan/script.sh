#!/bin/bash

read arg
read n1
read n2
read n3

if [ "$arg" == "a" ] && [ "$n3" -eq $((n1 + n2)) ]; then
    echo "yes"
elif [ "$arg" == "s" ] && [ "$n3" -eq $((n1 - n2)) ]; then
    echo "yes"
fi
