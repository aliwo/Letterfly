from flask import Flask
from flask_socketio import SocketIO

socketio = SocketIO()
application = Flask(__name__)
application.debug= False
socketio.init_app(application)

application.config['SECRET_KEY'] = 'gjr39dkjn344_!67#'

from application import routes, jinja, socketIOevents