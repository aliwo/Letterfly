from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO

application = Flask(__name__)
application.config.from_object('config') # config 파일을 불러와서 app객체를 설정합니다.
async_mode =None
thread = None

db=SQLAlchemy(application)

socketio = SocketIO()
socketio.init_app(application)

from application import routes, socketIOevents, models