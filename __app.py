from django.contrib.auth.models import User
from flask import Flask, redirect, url_for, request, render_template, session
from flask_httpauth import HTTPBasicAuth
from flask_login import LoginManager
import flask
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

auth = HTTPBasicAuth()

users = {
    "admin": generate_password_hash("123"),
}

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.
    form = LoginForm()
    if form.validate_on_submit():
        # Login and validate the user.
        # user should be an instance of your `User` class
        login_user(user)

        flask.flash('Logged in successfully.')

        next = flask.request.args.get('next')
        # is_safe_url should check if the url is safe for redirects.
        # See http://flask.pocoo.org/snippets/62/ for an example.
        if not is_safe_url(next):
            return flask.abort(400)

        return flask.redirect(next or flask.url_for('index'))
    return flask.render_template('login.html', form=form)

@app.route('/logout')
def logout():
    session.clear()
    return ('Please Login!', 401)
if __name__ == '__main__':

    app.secret_key = "b'\x8b\x16\xc1\x02N&Nr\xee\x02!0'"
    app.config['SESSION_TYPE'] = 'filesystem'

    app.run()