
from flask import Flask, redirect, render_template, request, url_for
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
    if len(verify_pass) < 1:
        verify_error = "Please verify password."
    if len(password) < 3 or len(password) > 20:
        password_error = "Invalid password."
    if len(username) < 3 or len(username) > 20:
        username_error = "Invalid username."
    #if len(email) < 1:
        #email_error = "Please enter valid email."
    if username_error == '' and verify_error == '' and email_error == '' and verify_error == '':
       return redirect(url_for('welcome', username=username))
    else:
        return render_template('sign-up.html', email_error=email_error, username_error=username_error, verify_error=verify_error, password_error=password_error)


@app.route('/welcome')
def welcome():
    username= request.args.get('username')
    
    return render_template("Welcome.html", username=username)

app.run()