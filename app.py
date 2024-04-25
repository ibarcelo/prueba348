from flask import Flask, render_template, jsonify, request
from database import engine, load_raquets_from_db, uploadRaquet, disp_raquets, elimRaquet, editRaquet
from sqlalchemy import text

app = Flask(__name__)

  

@app.route('/')
def hello_world():
  raquets = load_raquets_from_db()
  return render_template('home.html' , raquets=raquets)

@app.route('/home')
def rethome():
  return render_template('home.html')

@app.route('/insert')
def insert():
  raquets = load_raquets_from_db()
  return render_template('insert.html', raquets=raquets)

@app.route('/edit')
def edit():
   return render_template('edit.html')

@app.route('/eliminate')
def eliminate():
   return render_template('eliminate.html')

@app.route('/display')
def display():
   return render_template('display.html')

@app.route('/add_raquet', methods=['POST'])
def add_raquet():
  brand = request.form['brand']
  model = request.form['model']
  weight = request.form['weight']
  price = request.form['price']
  head_size = request.form['head_size']
  uploadRaquet(brand, model, weight, price, head_size)
  return render_template('insert.html')

@app.route('/elim_raquet', methods=['POST'])
def elim_raquet():
  id = request.form['id']
  elimRaquet(id)
  return render_template('eliminate.html')

@app.route('/edit_raquet', methods=['POST'])
def edit_raquet():
  id = request.form['id']
  characteristic = request.form['characteristic']
  newValue = request.form['newValue']
  editRaquet(characteristic, newValue, id)
  return render_template('edit.html')

@app.route('/display_raquet', methods=['POST'])
def display_raquet():
    characteristic = request.form['characteristic']
    if characteristic == 'price':
        min_price = request.form['min_price']
        max_price = request.form['max_price']
        value = request.form['value']
        disp_raquets(characteristic, value, min_price, max_price)
    else:
        value = request.form['value']
        min_price = request.form['min_price']
        max_price = request.form['max_price']
        disp_raquets(characteristic, value, min_price, max_price)
    return render_template('display.html')

    
@app.route('/displayed', methods=['POST'])
def displayed():
  data=request.form
  return jsonify(data)

print(__name__)
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)