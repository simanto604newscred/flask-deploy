from flask import Flask, jsonify, send_file, render_template
from scraptest import Legacy
from flask.ext.mail import Mail, Message
app = Flask(__name__)
import os

# Flask-Mail configuration
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'simanto605'#os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = '01911123665'#os.environ.get('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = 'simanto605@gmail.com'


# Initialize extensions
mail = Mail(app)

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
    return send_file('doc.csv')

@app.route('/in-progress')
def progress():
    msg = Message("Hello",
                  sender="simanto605@gmail.com",
                  recipients=["simanto604@gmail.com" ])
    msg.body = "testing"
    msg.html = "<b>testing</b>"
    with app.open_resource("test.csv") as fp:
        msg.attach("test.csv", "text/csv", fp.read())
    with app.open_resource("sample.csv") as fd:
        msg.attach("sample.csv", "text/csv", fd.read())
    with app.open_resource("result.csv") as fr:
        msg.attach("result.csv", "text/csv", fr.read())

    mail.send(msg)

    return 'This part is in progress....'

@app.route('/report')
def create_report():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
