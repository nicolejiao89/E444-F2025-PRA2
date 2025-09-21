from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from datetime import datetime
from flask_moment import Moment

app = Flask(__name__) 
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/user/<name>') 
def user(name):
    return render_template("user.html", name=name, current_time=datetime.utcnow())