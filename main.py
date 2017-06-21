
from flask import Flask, redirect, render_template, request
import os
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/user-input') #sends to form
def index():
    return render_template('sign-up.html')

@app.route('/user-input', methods=['POST']) #sends to form
def validate():
    username = request.form['username']
    password = request.form['password']
    verify_pass = request.form['verify_pass']
    email = request.form['email']

    verify_error = ''
    password_error = ''
    username_error = ''
    email_error = ''

    if password != verify_pass:
        verify_error = "Password and Verify Password do not match."
    if len(password) < 3 or len(password) > 20:
        password_error = "Invalid password."
    if password == '':
        password_error = "Invalid password."
    if username == '':
        username_error = "Invalid username, cannot be left blank."
    if len(username) < 3 or len(username) > 20:
        username_error = "Invalid username."
    if username_error == '' and verify_error == '' and email_error == '' and verify_error == '':
       return redirect('/welcome')
    else:
        return render_template('sign-up.html', username_error=username_error)


@app.route('/welcome')
def welcome():
    request.args.get('username')
    return render_template('Welcome.html', username=username)

app.run()