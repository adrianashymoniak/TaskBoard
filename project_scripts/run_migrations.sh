#!/bin/bash

python3 manage.py makemigrations --settings=task_board_application.settings.local

python3 manage.py migrate --settings=task_board_application.settings.local



