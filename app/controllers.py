from flask import render_template, flash, redirect, url_for
from app import app, db
from flask_login import current_user, login_user, logout_user, login_required
from app.forms import LoginForm, RegistrationForm
from app.models import User, Posts
from flask import request
from werkzeug.urls import url_parse
from datetime import datetime
class UserController():
    
    def login():
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(id=form.id.data).first()
            if user is not None and user.verify_password(form.password.data):
                login_user(user)
                return redirect(url_for('index'))
            return redirect(url_for('chat'))
        return render_template('Login_Page.html', form=form)
    
    def logout():
        logout_user()
        return redirect(url_for('index'))
    
    def register():
        form = RegistrationForm()
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user is not None:
                flash('Username already exists')
                return redirect(url_for('register'))
            if current_user.is_authenticated:
                return redirect(url_for('chat'))
            else:
                user = User(username=form.username.data, email=form.email.data, first_name=form.first_name.data, last_name=form.last_name.data, dob=form.dob.data, country=form.country.data, city=form.city.data)
                user.set_password(form.password.data)
                db.session.add(user)
                db.session.commit()
                login_user(user)
                return redirect(url_for('chat'))
        return render_template('Register_Page.html', form=form)
            