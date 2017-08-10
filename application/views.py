from application import application
from flask import request, render_template

@application.route('/')
def hello_world():
    return 'Hello LetterFly!'

@application.route('/text_color', methods=['GET', 'POST'])
def text_color_page():
    if request.method=='GET':
        return render_template('for_textcolor.html')

    if request.method == 'POST':
        btn = False
        if request.form['button'] == 'on':
            btn = True
        elif request.form['button'] == 'off':
            btn = False

        return render_template('for_textcolor.html', btn = btn)

