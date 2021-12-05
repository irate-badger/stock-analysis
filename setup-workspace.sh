#!/bin/bash

if [ ! -d "$(<.venv)" ]; then
  echo "Creating env folder"
  python -m venv $(<.venv)
else
  echo "Folder already exists"
fi

source $(<.venv)/bin/activate

pip install -r requirements.txt

pre-commit install