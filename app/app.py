#!/usr/bin/env python3

from flask import Flask, make_response, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

from models import db, Exercise, Member

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

# Define a route for the root URL
@app.route('/', methods=['GET'])
def index():
    return '<h1>Welcome to the Gym Project!</h1>'


# Define a route to retrieve a list of all members
@app.route('/members', methods=['GET'])
def get_members():
    members = Member.query.all()
    member_list = []
    for member in members:
        member_data = {
            'id': member.id,
            'name': member.name,
            'email': member.email,
            'phone_number': member.phone_number
        }
        member_list.append(member_data)
    return jsonify(member_list)


@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid data, expected JSON"}), 400

    # Assuming the Member model has appropriate fields (name, email, phone_number, password)
    member = Member(
        name=data.get('name'),
        email=data.get('email'),
        phone_number=data.get('phone_number'),
        password=data.get('password')
    )

    db.session.add(member)
    db.session.commit()

    return jsonify({"message": "Member signed up successfully"}), 201
   
   
    

# Define a route to retrieve a list of all exercises
@app.route('/exercises', methods=['GET'])
def get_exercises():
    exercises = Exercise.query.all()
    exercise_list = []
    for exercise in exercises:
        exercise_data = {
            'id': exercise.id,
            'name': exercise.name,
            'type': exercise.type,
            'muscle': exercise.muscle,
            'equipment': exercise.equipment,
            'difficulty': exercise.difficulty,
            'instructions': exercise.instructions,
            'member_id': exercise.member_id
        }
        exercise_list.append(exercise_data)
    return jsonify(exercise_list)

# Define a route to retrieve a specific exercise by its ID
@app.route('/exercises/<int:exercise_id>', methods=['GET'])
def get_exercise(exercise_id):
    exercise = Exercise.query.get(exercise_id)
    if exercise:
        exercise_data = {
            'id': exercise.id,
            'name': exercise.name,
            'type': exercise.type,
            'muscle': exercise.muscle,
            'equipment': exercise.equipment,
            'difficulty': exercise.difficulty,
            'instructions': exercise.instructions,
            'member_id': exercise.member_id
        }
        return jsonify(exercise_data)
    else:
        return jsonify({'message': 'Exercise not found'}), 404



# Define a route to retrieve a specific member by their ID
@app.route('/members/<int:member_id>', methods=['GET'])
def get_member(member_id):
    member = Member.query.get(member_id)
    if member:
        member_data = {
            'id': member.id,
            'name': member.name,
            'email': member.email,
            'phone_number': member.phone_number
        }
        return jsonify(member_data)
    else:
        return jsonify({'message': 'Member not found'}), 404



if __name__ == '__main__':
    app.run(port=5555, debug=True)
    