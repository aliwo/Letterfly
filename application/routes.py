from application import application,models
from flask import request, render_template, session, redirect, url_for, send_from_directory, jsonify
from .forms import LoginForm
from application.errors import InvalidUsage
from sqlalchemy import desc


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

@application.route('/static/<string:filename>')
def static_file(filename):
    return send_from_directory('./templates', filename)

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

@application.route('/storeData', methods=['POST'])
def storeData():
    text = request.form.get('text')
    name = session.get('name', '')
    letter = models.Letter(text=text, user_id=name)
    models.db.session.add(letter)
    models.db.session.commit()
    return 'letter saved'

@application.route('/recommendation', methods=['GET', 'POST'])
def recommendation():
    if request.method=='GET':
        targets = models.Target.query.all()
        targets = {'targets':targets}
        return render_template('recommendation.html', targets=targets)

    if request.method== 'POST':
        target = request.form.get('target')
        if target:
            target = models.Target.query.filter_by(name=target).first()
            recommendations = models.Recommendation.query\
                .filter_by(target_id=target.id)\
                .order_by(desc(models.Recommendation.upvotes))\
                .all()
            result = {'recommendations':recommendations}
            return render_template('recommendation.html', result=result)
        else:
            raise InvalidUsage('invalid target', status_code=400)

@application.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response
