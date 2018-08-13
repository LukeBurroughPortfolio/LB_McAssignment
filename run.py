from flask import Flask, render_template, request, session, redirect, url_for
import sqlite3

app = Flask(__name__)
app.secret_key = '9970436dddec6e16b82c62475435623fdbe7fa03'

# to run:
# cd to directory
# source env/bin/activate
# export FLASK_APP=run.py; export FLASK_DEBUG=1
# flask run

MENUDB = 'menu.db'

def fetchMenu(con):
  burgers = []
  free = '0'
  cur = con.execute('SELECT burger,price FROM burgers WHERE price>=?', (free,))
  for row in cur:
    burgers.append(list(row))

  drinks = []
  cur = con.execute('SELECT drink,price FROM drinks')
  for row in cur:
    drinks.append(list(row))

  sides = []
  cur = con.execute('SELECT side,price FROM sides')
  for row in cur:
    sides.append(list(row))

  return {'burgers':burgers, 'drinks':drinks, 'sides':sides}

@app.route('/')
def index():
  '''
  con = sqlite3.connect(MENUDB)
  menu = fetchMenu(con)
  con.close()
  '''
  return render_template('index.html')
