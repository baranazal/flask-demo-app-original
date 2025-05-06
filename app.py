import socket
import os
import uuid
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def home():
    hostname = socket.gethostname()
    randomid = uuid.uuid4()
    my_name = os.environ.get('MY_NAME', 'Default Name')
    my_role = os.environ.get('MY_ROLE', 'Default Role')

    return (
        f'Container Hostname: {hostname}<br>'
        f'UUID: {randomid}<br>'
        f'Name: {my_name}<br>'
        f'Role: {my_role}<br>'
    )

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
