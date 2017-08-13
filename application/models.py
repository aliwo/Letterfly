from application import db
import datetime

class Target(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    name_kor = db.Column(db.String, unique=True)

    def __init__(self, name, name_kor):
        self.name = name
        self.name_kor = name_kor

class Recommendation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String)
    text = db.Column(db.String, nullable=False)
    target_id = db.Column(db.Integer, db.ForeignKey('target.id'))
    target = db.relationship('Target', backref=db.backref('recommendation', lazy='dynamic'))
    upvotes = db.Column(db.Integer)

    def __init__(self, text, target, image_url='', upvotes=0, ):
        self.text = text
        self.target = target
        self.upvotes = upvotes
        self.image_url = image_url

class Letter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    font_id = db.Column(db.Integer) #fiddler러를 통해 본 실제 Letter fly서버의 /loadData 응답을 토대로 필드 구성.
    color_id = db.Column(db.Integer)
    text = db.Column(db.String)
    created_at = db.Column(db.DateTime)
    user_name = db.Column(db.String)

    def __init__(self, text, user_id, font_id=0, color_id=0):
        self.font_id = font_id
        self.color_id = color_id
        self.text = text
        self.user_name = user_id
        self.created_at = datetime.datetime.now()