from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Member(db.Model):
    __tablename__ = "members"  
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    phone_number = db.Column(db.String)  
    password = db.Column(db.String)
    
    exercises = db.relationship('Exercise', backref='member')
    
    def __repr__(self):  
        return f'<Member: {self.name}>'

class Exercise(db.Model):
    __tablename__ = "exercises"  
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    type = db.Column(db.String)
    muscle = db.Column(db.String)
    equipment = db.Column(db.String)
    difficulty = db.Column(db.String)
    instructions = db.Column(db.String)
    
    member_id = db.Column(db.Integer, db.ForeignKey("members.id"))  # Corrected the ForeignKey reference

