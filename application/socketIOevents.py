from flask import session
from flask_socketio import emit, join_room, leave_room
from application import socketio

@socketio.on('joined', namespace='/word')
def joined(message):
    room = session.get('room')
    join_room(room)
    emit('status', {'msg': session.get('name') + ' has entered the room.'}, room=room)

@socketio.on('type_word', namespace='/word')
def word_space(message):
    room = session.get('room')
    code = message['code']
    if code == 13:
        emit('word_message', {'msg':message['msg']+ '\n'}, room=room)
    elif code == 32:
        emit('word_message', {'msg':message['msg']+ ' '}, room=room)
    elif code == 8:
        emit('word_message', {'msg':message['msg'][:-1]}, room=room)

@socketio.on('left', namespace='/word')
def left(message):
    room = session.get('room')
    leave_room(room)
    emit('status', {'msg': session.get('name') + ' has left the room.'}, room=room)