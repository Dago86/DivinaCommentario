from db import db

""" id chiave primaria
name: Canto I...
parte: Inferno
text: "Nel mezzo del cammin..." """
class CantoModel(db.Model):
    __tablename__= 'canti'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    parte = db.Column(db.String(80))
    text = db.Column(db.String(512))

    comments = db.relationship('CommentModel', lazy='dynamic')

    def __init__(self,name, parte, text):
        self.name = name
        self.parte= parte
        self.text=text

    
    def json(self):
        return {'name':self.name, 'parte':self.parte, 'text':self.text, 'comments':[comment.json() for comment in self.comments.all()]}


    def json_comments(self):
        return {'comments':[comment.json() for comment in self.comments.all()]}

    @classmethod
    def find_by_name(cls,name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_nameAndParte(cls,name, parte):
        return cls.query.filter_by(name=name, parte=parte).first()


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()