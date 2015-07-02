from flask import Flask, jsonify, send_file, render_template, request, session
from main_pilot import MainPilot
from flask.ext.mail import Mail, Message
import os, threading, time, logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)
app.config['SECRET_KEY'] = 'top-secret!'

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


def send_email(email):

    msg = Message("Hello",
                  sender="simanto605@gmail.com",
                  recipients=["simanto604@gmail.com" ])
    msg.body = "Generated Data"
    msg.html = "<b>Here's generated data attached</b>"
    print email
    msg.add_recipient(email)
    with app.open_resource("test.csv") as fp:
        msg.attach("test.csv", "text/csv", fp.read())
    with app.open_resource("doc.csv") as fd:
        msg.attach("doc.csv", "text/csv", fd.read())
    with app.open_resource("result.csv") as fr:
        msg.attach("result.csv", "text/csv", fr.read())
    with app.app_context():
        print '$$$$$Send mail now$$$$$$$$'
        mail.send(msg)

def foo(email):
    app.logger.info("f started"+ "email: "+email+"\n")
    print email
    if get_globvar():
        set_globvar_to(False)
        main_pilot = MainPilot()
        main_pilot.run()
        send_email(email)
        set_globvar_to(True)


    app.logger.info("Foo finished\n")



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', email=session.get('email', ''))
    if request.method == 'POST':
        email = ''.join([request.form['email']])
        session['email'] = email
        print email
        with app.test_request_context():
            thr = threading.Thread(target=foo, args=(email,), kwargs={})
            if not thr.is_alive():
                thr.start() # will run "foo"

        # thr.is_alive() # will return whether foo is running currently
        if not get_globvar():
            return "Already Running previous task"
        # thr.join()

        return "You'll get a mail in an hour"


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






if __name__ == '__main__':
    formatter = logging.Formatter(
        "[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
    handler = RotatingFileHandler('../../foo.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
    app.run(debug=True)
