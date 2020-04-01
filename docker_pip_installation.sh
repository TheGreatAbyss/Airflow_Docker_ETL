#!/bin/bash

cd /app
pip install --upgrade pip
pip install --upgrade pipenv wheel
pipenv install
pipenv lock
pipenv install --dev --deploy --system --skip-lock -v