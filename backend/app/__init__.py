from gevent import monkey
monkey.patch_all()

import os
from flask import Flask
from flask_socketio import SocketIO
from flask_cors import CORS
from worker import celery

socketio = SocketIO()


def create_app(debug=False):
    """Create an application."""
    env = os.environ
    app = Flask(__name__)
    cors = CORS(app)
    app.debug = debug
    app.config['SECRET_KEY'] = 'supersecret!'
    app.config['CORS_HEADERS'] = 'Content-Type'

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    socketio.init_app(app)
    return app
