from flask import Flask, jsonify, send_file

app = Flask(__name__)


@app.route('/')
def index():
    return 'Flask is running COOL!'


@app.route('/data')
def names():
    data = {
        "first_names": ["John", "Jacob", "Julie", "Jenny",]
    }
    return jsonify(data)

@app.route('/legacy')
def get_file():
    return send_file('test.csv')

@app.route('/beenverified')
def get_another_file():
    return send_file('sample.txt')

if __name__ == '__main__':
    app.run()
