from importlib.resources import Resource

from instruments.guitar import Guitar
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return '<p>Music PyTheory<p>'


@app.route('/guitar/chord/<chord>')
def get_guitar_chord(chord):
    guitar = Guitar()
    chord = guitar.get_chord_positions(chord)
    return jsonify({'message': 'Success', 'data': chord})


app.run(host='0.0.0.0', port=7999, debug=True)