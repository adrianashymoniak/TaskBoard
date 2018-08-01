####Required:
* python3.6
* django 2.0
####Optional:
* virtual env

####Installation process:
* **install python3.6** (before verify python version installed, if 2.7 you should install python 3.6)
* Create virtual env:  run command in terminal **python -m venv myvenv**
* Activate virtual env (optional): 
    - For Linux: **source myvenv/bin/activate**
    - For Windows **myenv\Scripts\activate**
* Install django: **pip install django~=2.0**
* Clone repository: **git clone https://adrianashymoniak@bitbucket.org/adrianashymoniak/tasks-board.git**
* Install postgresql: <br />
**sudo apt-get update** <br />
**sudo apt-get install postgresql postgresql-contrib**
* Create db and db user: 
    * **sudo -i -u postgres**
    * CREATE USER **set_user_name_here** WITH PASSWORD '**set_password_here**'
    * CREATE DATABASE task_board_db
* Edit settings/local.py with updating the following **DATABASES** params:
    * 'NAME': 'task_board_db',
    * 'USER': 'set_user_name_created_in_previous_step', 
    * 'PASSWORD': 'set_password_created_in_previous_step',
    * 'HOST': 'set_host_url',
* Go to **task-board** folder and run migration: **python manage.py migrate --settings=task_board_application.settings.local**
* **python manage.py makemigrations --settings=task_board_application.settings.local** 
* Run server locally: **python manage.py runserver --settings=task_board_application.settings.local**
* Open browser and go to  **http://127.0.0.1:8000/** -> click signup and create your own user

#####Please set url to your server and full path to your database in configs.py
 
#####End to end tests
* Run command **pip install git+https://github.com/yashaka/selene.git** for installing Selene framework
* Run command **pip install psycopg2-binary** for installing Psycopg (for creating connection to db)
* Run tests with **python -m unittest discover e2etests -v** (chrome should be installed)
