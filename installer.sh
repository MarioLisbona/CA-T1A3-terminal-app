#!/bin/bash
#if pip is not installed
if [[ -x "$(command -v pip3)" ]]
then
    #if python is installed and version 3 and above
    if [[ -x "$(command -v python3)" ]]
    then
        py_version="$(python3 -V 2>&1)"
        if [[ $py_version == "Python 3"* ]]
        then
            python3 -m pip install rich
            python3 -m pip install tinydb
            python3 main.py
        else
            echo "Your running Python $py_version, that is so old school! This program needs the latest version.
        You can get it here - https://www.python.org/downloads/" >&2
        fi 
    else
        echo "Looks like you don't have Python3 installed.
            You can download it here - https://www.python.org/downloads/" >&2
    fi
else
    #install pip
    python3 -m ensurepip
    #if python is installed and version 3 and above
    if [[ -x "$(command -v python3)" ]]
    then
        py_version="$(python3 -V 2>&1)"
        if [[ $py_version == "Python 3"* ]]
        then
            python3 -m pip install rich
            python3 -m pip install tinydb
            python3 main.py
        else
            echo "Your running Python $py_version, that is so old school! This program needs the latest version.
        You can get it here - https://www.python.org/downloads/" >&2
        fi 
    else
        echo "Looks like you don't have Python3 installed.
            You can download it here - https://www.python.org/downloads/" >&2
    fi

fi
    
    
    
    
    
    
    
    

