from flask import Flask, render_template

app = Flask(__name__)

RAQUETS = [
  {
    'id': 1,
    'name': 'Wilson Blade 98',
    'price': 200,
    'head size': '640',
    'weight': '300g'
  },
  {
    'id': 2,
    'name': 'Head Radical mp',
    'price': 250,
    'head size': '630',
    'weight': '310g'
  },
  {
    'id': 3,
    'name': 'Babolat aero',
    'price': 220,
    'head size': '660',
    'weight': '305g'
  }
]

@app.route('/')
def hello_world():
  return render_template('home.html', r=RAQUETS)

print(__name__)
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)