from app import app, db
from flask import render_template, url_for, request, make_response, redirect, jsonify, flash
from flask_login import current_user, login_user, logout_user, login_required
from python_chat_with_ChatGPT import get_response
from werkzeug.urls import url_parse
from app.controllers import UserController

@app.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('chat'))
    return render_template('Landing_Page.html')

@app.route('/chat/')
def chat():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    return render_template('Chat_Page.html')

@app.route('/login/', methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('chat'))
    return UserController.login()


@app.route('/register/', methods=['GET', 'POST'])
def register():
    return UserController.register()

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    return UserController.logout()

@app.route("/submit", methods=["POST"])
def submit():
    """this is a method that collect the user input from the form when they pressed the 'send' button,
    this method will send the user input to the ChatGPT api and get a response"""
    user_input_content = request.form.get('user_input_content')
    print(user_input_content)
    GPT_response = get_response(user_input_content)
    try:
        print(f"original response:{GPT_response}")
        message = GPT_response['choices'][0]['text']
        print(message)
        return jsonify({'message': message})
    except KeyError:
        print("no response from ChatGPT")
        return '/'




