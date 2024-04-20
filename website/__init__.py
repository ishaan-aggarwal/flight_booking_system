from flask import Flask
import os

db_path = os.path.join(os.path.dirname(__file__), 'database.db')

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'asldfj_slkdf_sefwe_sdfvvw'
    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import create_database
    if not os.path.exists(db_path):
        create_database(db_path)

    return app