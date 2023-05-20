from app import app, sql_conn, sql_cursor
from flask import render_template, url_for, request, make_response, redirect, jsonify
from python_chat_with_ChatGPT import get_response


@app.route('/')
def index():
    return render_template('Chat_Page.html')


@app.route('/login_page/')
def login_page():
    return render_template('Login_Page.html')


@app.route('/login', methods=["POST"])
def login():
    print("hello")
    login_info = request.get_json()
    login_userName = login_info["username"]
    login_passwd = login_info["passwd"]
    sql_conn.commit()
    sql_cursor.execute(f"SELECT username, password_hash FROM user WHERE username = '{login_userName}';")
    db_user_info = sql_cursor.fetchall()
    print(db_user_info)
    if len(db_user_info[0]) == 0:
        return jsonify({"login_state": "invalid_username"})
    else:
        if db_user_info[0][1] != login_passwd:
            return jsonify({"login_state": "invalid_password"})
        else:
            return jsonify({"login_state": "success"})


@app.route('/forget password_page/')
def forget_passwd_page():
    return render_template('Forgot_Password_Page.html')


@app.route('/register_page/')
def register_page():
    return render_template('Register_page.html')


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
        print(msg)
        return jsonify({'message': msg})
    except KeyError:
        print("no response from ChatGPT")
        return '/'




