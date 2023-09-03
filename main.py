from flask import Flask, request, jsonify, redirect, url_for, render_template
import logging

app = Flask(__name__)

#tyring logging
logging.basicConfig(filename='app.log', level=logging.INFO)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return "Login Page"

@app.route('/signup')
def signup():
    return "SignUp Page"

@app.route('/services')
def services():
    return "services"

@app.route('/bot_action/<string:action>')
def bot_action(action):
    if action == 'login':
        return redirect(url_for('login'))
    elif action == 'signup':
        return redirect(url_for('signup'))
    elif action == 'services':
        return redirect(url_for('services'))

if __name__ == '__main__':
    app.run(debug=True)
