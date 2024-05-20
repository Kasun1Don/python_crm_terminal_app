#!/bin/bash

if ! [[ -x "$(command -v python3)" ]]
then
  echo "Error: 
    This program runs on Python3, but it looks like Python3 is not installed.
    To install Python3, check out https://www.python.org/downloads/" >&2
  exit 1
fi

#cd path to applicatoin

if [ ! -d ".venv" ]; then
  python3 -m venv .venv
fi

source .venv/bin/activate
pip3 install -r ./requirements.txt
python3 main.py

