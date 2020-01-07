#!/bin/bash

cd /home/ivan/github/Qwich
source "gdei-env/bin/activate"
atom
python manage.py runserver
