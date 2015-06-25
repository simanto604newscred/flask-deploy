from flask import Flask, jsonify, send_file
from scraptest import Legacy

app = Flask(__name__)

@app.route('/')
def index():
    return 'Flask is Running now!'


@app.route('/data')
def names():
    data = {
        "first_names": ["John", "Jacob","change","more",]
    }
    return jsonify(data)

@app.route('/legacy')
def get_file():



    return send_file('test.csv')

@app.route('/beenverified')
def get_another_file():
    return send_file('sample.csv')

if __name__ == '__main__':
    app.run()
