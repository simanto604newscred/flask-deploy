from flask import Flask, jsonify, send_file, render_template
from main_pilot import MainPilot
from flask.ext.mail import Mail, Message
app = Flask(__name__)
import os, threading, time

# Flask-Mail configuration
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'simanto605'#os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = '01911123665'#os.environ.get('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = 'simanto605@gmail.com'


# Initialize extensions
mail = Mail(app)

flag = True

def set_globvar_to(value):
    global flag    # Needed to modify global copy of globvar
    flag = value

def get_globvar():
    global flag
    return flag


def send_email():
    msg = Message("Hello",
                  sender="simanto605@gmail.com",
                  recipients=["simanto604@gmail.com" ])
    # import ipdb;ipdb.set_trace()
    msg.body = "testing"
    msg.html = "<b>testing</b>"
    with app.open_resource("test.csv") as fp:
        msg.attach("test.csv", "text/csv", fp.read())
    with app.open_resource("doc.csv") as fd:
        msg.attach("doc.csv", "text/csv", fd.read())
    with app.open_resource("result.csv") as fr:
        msg.attach("result.csv", "text/csv", fr.read())
    with app.app_context():
        mail.send(msg)

def foo():
    print "f started"

    if get_globvar():
        set_globvar_to(False)
        main_pilot = MainPilot()
        main_pilot.run()
        send_email()
        set_globvar_to(True)
    print "f finished"


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

@app.route('/mail')
def progress():
    thr = threading.Thread(target=foo, args=(), kwargs={})
    # import ipdb;ipdb.set_trace()
    if not thr.is_alive():
        thr.start() # will run "foo"

    # thr.is_alive() # will return whether foo is running currently

    # thr.join()

    return "You'll get a mail...."

@app.route('/report')
def create_report():

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
