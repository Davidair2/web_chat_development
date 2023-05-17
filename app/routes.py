from app import app
from flask import render_template, url_for

@app.route('/')
def index():
    return render_template('Chat_Page.html')

@app.route('/login/')
def login():
    return render_template('Login_Page.html')

@app.route('/register/')
def register():
    return render_template('Register_page.html')