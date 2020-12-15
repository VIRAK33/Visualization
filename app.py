from flask import Flask, redirect, url_for, request, render_template
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

auth = HTTPBasicAuth()

users = {
    "admin": generate_password_hash("123"),
}

@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username

@app.route('/')
@auth.login_required
def index():
    return render_template('index.html')



if __name__ == '__main__':
    app.run()