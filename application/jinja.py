from application import application

def clever_function():
    return u'HELLO'

def random_color(words, cycler):
    result = ''
    for character in words:
        return '<span style=\"color: '+cycler.next()+'\">'+character+'</span> '
    return result

# application.jinja_env.globals.update(clever_function=clever_function)
# application.jinja_env.globals.update(random_color=random_color)