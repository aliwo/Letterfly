from flask import session
from flask_socketio import emit, join_room, leave_room
from application import socketio

@socketio.on('joined', namespace='/word')
def joined(message):
    room = session.get('room')
    join_room(room)
    emit('status', {'msg': session.get('name') + '님이 편지를 쓰러 오셨습니다.'}, room=room)

@socketio.on('type_word', namespace='/word')
def word_space(message):
    room = session.get('room')
    emit('word_message', {'msg':message['msg']}, room=room)

@socketio.on('left', namespace='/word')
def left(message):
    room = session.get('room')
    leave_room(room)
    emit('status', {'msg': session.get('name') + ' has left the room.'}, room=room)