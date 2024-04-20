from flask import Blueprint, render_template, request, flash, redirect, url_for
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
from . import db_path

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return '<p>Logout</p>'

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if not name or not email or not password1 or not password2:
            flash('Please fill out all fields.', category='error')
        elif len(email) < 4:
            flash('Email must be at least 4 characters.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 6:
            flash('Password must be at least 6 characters.', category='error')
        else:
            with sqlite3.connect(db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                INSERT INTO user (email, password, name)
                VALUES (?, ?, ?);
                ''', (email, generate_password_hash(password1), name))
                conn.commit()
            flash('Account created successfully', category='success')
            return redirect(url_for('auth.login'))

    return render_template('sign_up.html')