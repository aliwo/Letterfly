from application import application
from flask import request, render_template, session, redirect, url_for
from .forms import LoginForm


@application.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        session['room'] = form.room.data
        return redirect(url_for('editor'))
    elif request.method == 'GET':
        form.name.data = session.get('name', '')
        form.room.data = session.get('room', '')
    return render_template('index.html', form=form)

@application.route('/text', methods=['GET', 'POST'])
def show_text():
    if request.method=='GET':
        return render_template('text_for_colorblinded.html')

    if request.method == 'POST':
        if request.form['button'] == 'on':
            return render_template('text.html')
        elif request.form['button'] == 'off':
            return render_template('text_for_colorblinded.html')

@application.route('/editor', methods=['GET', 'POST'])
def editor():
    name = session.get('name', '')
    room = session.get('room', '')
    if name == '' or room == '':
        return redirect(url_for('index'))
    return render_template('word.html', name=name, room=room)

#GET을 하면 에디터 페이지를 보여줌
#글자를 써서 /editor에 포스트 하면 해당 내용을 .txt로 써서 저장.
#백엔드의 모든 기능을 사용한다. 난 백으로 지원한 거임 ^^