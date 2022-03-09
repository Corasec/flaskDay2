## Flask Blog
 Two-side app developped with Python: flask, sqlite.
 Api : app.py is the server side.
 Front : client.py the client side.
 Client can send requests to the server: login, register, view articles etc...

*****************************************
# Install Flask
 python3 -m pip install flask
 dnf install python3-pip (on fedora) : create the script /usr/bin/pip3


# instal sqlite3
 >>>sudo dnf install sqlite3
 >>>sqlite3 + help to command


# Launch the app

-----------------
Server (from '/App' folder) --- app.py:

>>>export FLASK_APP = app.py export FLASK_DEBUG=true
>>>flask run

run on port:5000 

Postman tests url:
login + POST
register + POST
users + GET/PUT
users/id + GET/DELETE/POST
artciles + GET/PUT
artciles/id + GET/DELETE/POST

------------------
Client (from '/Client' folder) --- client.py:

>>>export FLASK_APP = client.py export FLASK_DEBUG = true
>>>flask run --port:3000

run on port:3000

------------------
to do: implement articles crud on client-side