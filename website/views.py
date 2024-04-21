from flask import Blueprint, render_template
from flask_login import login_required, current_user
import sqlite3
from .models import User
from . import db_path

views = Blueprint('views', __name__)

@views.route('/home')
@login_required
def home():
    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute('''
            SELECT f.airline, fd.date, fd.departure, fd.landing, fd.flight_id, fd.from_destination, fd.to_destination
            FROM booking AS b
            JOIN flight_details AS fd ON b.detail_id = fd.detail_id
            JOIN flights AS f ON fd.flight_id = f.flight_id
            WHERE b.user_id = ?
        ''', (current_user.id,))

        
        booked_flights = cursor.fetchall()

    return render_template('home.html', user=current_user, booked_flights=booked_flights)
