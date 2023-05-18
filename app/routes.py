from app import app
from flask import render_template, url_for, request, make_response, redirect, jsonify
from python_chat_with_ChatGPT import get_response


@app.route('/')
def index():
    return render_template('Chat_Page.html')


@app.route('/login/')
def login():
    return render_template('Login_Page.html')


@app.route('/register/')
def register():
    return render_template('Register_page.html')


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




