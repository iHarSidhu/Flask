At Terminal
Create a folder named Flask, 
ex. mkdir Flask

inside Flask, do the project setup as stated below, 
ex. cd Flask

Project setup
Flask> py -3 -m venv .venv
Flask> .venv\Scripts\activate
(.venv) ...\Flask>
Flask> pip install Flask
Flask> python.exe -m pip install --upgrade pip

create a folder named: learnFlask
ex. mkdir learnFlask (do not get inside using cd learnFlask)
Terminal must stay in Flask Directory: Flask>

Git
Chapter01/
│
├── learnFlask.py
└── learnFlaskApp/
    ├── __init__.py
    └── routes.py

From: Chapeter01, Copy all folder and files as it is in to: Flask, so it looks like;

LocalPc
Flask/
├──
    learnFlask/
    ├── learnFlask.py
    └── learnFlaskApp/
        ├── __init__.py
        └── routes.py

Replace folder and files as moving along with the chapters

First run
Flask> $env:FLASK_APP="learnFlask.py"
Flask> flask run

    * Serving Flask app 'learnFlask.py'
    * Debug mode: off
        WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
    * Running on http://127.0.0.1:5000
        Press CTRL+C to quit