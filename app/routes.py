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

@app.route('/forgot', methods=['GET', 'POST'])
def forgot():
    return render_template('Forgot_Password_Page.html')

@app.route("/landing_page/")
def landing_page():
    return render_template("Landing_Page.html")


@app.route("/register", methods=["POST"])
def register():
    """this is a method that collect the user information from the register page,
        this method will save user_name, email, password into the sqlite database"""
    print("hello")
    user_info = request.get_json()
    user_name = user_info["username"]
    email = user_info["email"]
    passwd = user_info["passwd"]

    sql_cursor.execute(f"INSERT INTO user (username, email, password_hash) VALUES"
                       f" ('{user_name}', '{email}', '{passwd}')")
    sql_conn.commit()

    print(f"user name: {user_name}, email: {email}, passwd: {passwd}")
    return redirect(url_for('landing_page'))


@app.route("/submit", methods=["POST"])
def submit():
    """this is a method that collect the user input from the form when they pressed the 'send' button,
    this method will send the user input to the ChatGPT api and get a response"""
    user_input_content = request.form.get('user_input_content')
    print(user_input_content)
    GPT_response = get_response(user_input_content)
    try:
        print(f"original response:{GPT_response}")
        msg = GPT_response['choices'][0]['text']
        check = check_response(user_input_content, msg)
        if check == True:
            print(msg)
            return jsonify({'message': msg})
        else:
            msg = "This question/answer could not be understood in the context of travel, food, accommodation etc.\nPlease rephrase the question and try again."
            print(msg)
            return jsonify({'message': msg})
    except KeyError:
        print("no response from ChatGPT")
        return '/'




