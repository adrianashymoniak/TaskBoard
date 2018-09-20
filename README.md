#####Required:
* python3.6
* django 2.0
#####Optional:
* virtual env

#####Installation process:
* Clone repository: **git clone https://adrianashymoniak@bitbucket.org/adrianashymoniak/tasks-board.git**
* Create virtual env:  run command in terminal **python -m venv myvenv**
* Activate virtual env (optional): 
    - For Linux: **source myvenv/bin/activate**
    - For Windows **myenv\Scripts\activate**
* run: **pip install -r requirements.txt** (for installing required libraries in your virtual env)
* Install postgresql: 
    - run **sudo apt-get update** 
    - run **sudo apt-get install postgresql postgresql-contrib**

* Create db and db user: 
    * **sudo -i -u postgres**
    * run: **psql**
    * CREATE USER **set_user_name_here** WITH PASSWORD '**set_password_here**';
    * CREATE DATABASE task_board_db;
    
* For setting correct db time zone go to terminal and run:
    * **sudo -u postgres psql**
    * **\c task_board_db;**
    * **DATABASE task_board_db SET timezone TO 'UTC';**
    * **SELECT pg_reload_conf();**
    
* Edit DEBUG parameter in task_board_application/settings/local.py:
    * DEBUG = False   
* Edit task_board_application/settings/local.py with updating the following **DATABASES** params:
    * 'NAME': 'task_board_db',
    * 'USER': 'set_user_name_created_in_previous_step', 
    * 'PASSWORD': 'set_password_created_in_previous_step',
    * 'HOST': 'set_host_url',
*   For sending messages during resetting passwords edit task_board_application/settings/local.py with following parameters:
    * EMAIL_HOST = 'set_smtp_host_here'
    * EMAIL_USE_TLS = True
    * EMAIL_PORT = 'set_port_here'
    * EMAIL_HOST_USER = 'set_email_here'
    * EMAIL_HOST_PASSWORD = 'set_password_here'
* Make sure your virtual environment is activated and requirements are installed    
* Go to **task-board** folder and run migration: **python manage.py migrate --settings=task_board_application.settings.local**
* Run server locally: **python manage.py runserver --settings=task_board_application.settings.local**
* Open browser and go to  **http://127.0.0.1:8000/** -> click signup and create your own user
 
#####End to end tests
* Run tests with **python -m unittest discover e2etests -v** (chrome should be installed)
* Edit tasks-board/e2etests/configs.py with following parameters:
    * BASE_URL = 'http://127.0.0.1:8000'
    * DB_SETUP = {'database': 'task_board_db',
            'user': 'set_user_name_created_in_previous_step',
            'password': 'set_password_created_in_previous_step',
            'host': 'set_host_url',
            'port': '5432'}
    * HEADLESS = False
    * APP_TIME_ZONE = 'Europe/Kiev'
    * AUTO_INSTALL_DRIVER = True

