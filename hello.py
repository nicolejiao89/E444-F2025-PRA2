from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from datetime import datetime
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email
from wtforms.fields import EmailField  # WTForms 3.x

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

Bootstrap(app)
Moment(app)

# chapter 3 activity
@app.route('/user/<name>') 
def user(name):
    return render_template("user.html", name=name, current_time=datetime.utcnow())

if __name__ == '__main__':
    app.run(debug=True)

# chapter 4 activity
class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    email = EmailField('What is your UofT Email address?', validators=[DataRequired(), Email()])
    submit = SubmitField('Submit')

def is_uoft_email(addr: str) -> bool:
    return isinstance(addr, str) and (addr.endswith('@mail.utoronto.ca'))

@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    email = None
    form = NameForm()
    if form.validate_on_submit():
        old_name  = session.get('name')
        old_email = session.get('email')

        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        if old_email is not None and old_email != form.email.data:
            flash('Looks like you have changed your email!')
            
        session['show_non_uoft'] = not is_uoft_email(form.email.data)

        session['name'] = form.name.data
        session['email'] = form.email.data
        return redirect(url_for('index'))  # PRG pattern
    
    show_non_uoft = session.pop('show_non_uoft', False)

    return render_template(
        'index.html', 
        form=form, 
        name=session.get('name'), 
        email=session.get('email'), 
        show_non_uoft=show_non_uoft, 
        current_time=datetime.utcnow()
    )


