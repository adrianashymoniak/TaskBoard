#!/bin/bash

python3 manage.py runserver --settings=task_board_application.settings.local
python3 -m unittest discover e2etests -v
