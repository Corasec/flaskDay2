from flask import Flask, g, redirect, url_for, abort, render_template, flash
import sqlite3
import os


app=Flask( __name__ ) # app name = file name


    
app.config.from_object( __name__ ) # load config from  app.py

app.config.update(dict(
    DATABASE = os.path.join(app.root_path , '../flaskr.db '),
    SECRET_KEY = 'development key',
    USERNAME = 'admin',
    PASSWORD = 'default'
))
app.config.from_envvar ( 'FLASKR_SETTINGS' , silent=True ) 


def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    

@app.cli.command('initdb')
def initdb_command():
    init_db()
    print('Initialized the database.')

def get_db(): 
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db
    

def query_db( query, args=(), one=False):
    cur = get_db().execute(query, args)
    result = cur.fetchall()
    cur.close()
    return (result[0] if result else None) if one else result

def close_db():
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()