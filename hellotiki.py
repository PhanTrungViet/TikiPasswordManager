from flask import Flask, render_template, redirect, url_for, session, request
from PasswordManagerLib import *
app = Flask(__name__)
app.secret_key = 'cf4fa245-618c-4844-a7e7-1104c88e2976'

@app.route('/', methods=['POST', 'GET'])
def signin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        signin = PasswordManager()
        if signin.validateUsername(username) == False:
            return render_template('index.html', err='Invalid username')
        if signin.validatePassword(password) == False:
            return render_template('index.html', err='Invalid password')
        else:
            if signin.verifyPassword(username, password):
                session['username'] = username
            return redirect(url_for('signin'))
    return render_template('index.html')

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        signup = PasswordManager()
        if signup.validateUsername(username) == False:
            return render_template('signup.html', err='Invalid username')
        if signup.validatePassword(password) == False:
            return render_template('signup.html', err='Invalid password')
        else:
            passwordToEncrypt = signup.encrypt(password)
            signup.setNewPassword(username, passwordToEncrypt)
            return redirect(url_for('signin'))
    return render_template('signup.html')

@app.route('/signout', methods=['GET'])
def signout():
    session.clear()
    return redirect(url_for('signin'))

if __name__ == '__main__':
    app.run(debug=True)
