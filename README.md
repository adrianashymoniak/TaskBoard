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
* Go to **task-board** folder and run migration: **python manage.py migrate**
* **python manage.py makemigrations**
* Run server locally: **python manage.py runserver**
* Open browser and go to  **http://127.0.0.1:8000/** -> click signup and create your own user