from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return 'Flask is running COOL!'


@app.route('/data')
def names():
    data = {
        "first_names": ["John", "Jacob", "Julie", "Jenny", "Another boy"]
    }
    return jsonify(data)


if __name__ == '__main__':
    app.run()
