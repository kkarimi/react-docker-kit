from gevent import monkey
monkey.patch_all()

from flask import Flask
from flask_socketio import SocketIO

socketio = SocketIO()


def create_app(debug=False):
    """Create an application."""
    app = Flask(__name__)
    app.debug = debug
    app.config.from_object('configs')

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    socketio.init_app(app)

    return app
