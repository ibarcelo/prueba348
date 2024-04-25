from flask import Flask, render_template
from database import engine, load_raquets_from_db
from sqlalchemy import text

app = Flask(__name__)

  

@app.route('/')
def hello_world():
  raquets = load_raquets_from_db()
  return render_template('home.html' , raquets=raquets)

@app.route('/insert')
def insert():
   return render_template('insert.html')

@app.route('/edit')
def edit():
   return render_template('edit.html')

@app.route('/eliminate')
def eliminate():
   return render_template('eliminate.html')

@app.route('/display')
def display():
   return render_template('display.html')

print(__name__)
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)