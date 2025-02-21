#!/bin/sh

# Go to the right directory
cd /opt/opencti-connector-{{ cookiecutter.__connector_name_kebabcase }}

# Launch the worker
python3 main.py
