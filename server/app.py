#!/usr/bin/env python3

from flask import Flask, make_response, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from  werkzeug.security import generate_password_hash, check_password_hash
from models import db, Exercise, Member

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

from datetime import datetime, timedelta 
from functools import wraps

app = Flask(__name__)
CORS(app)

app.config["JWT_SECRET_KEY"] = "ufhjdsag843!u*#*#yh REFD734X498rq8nm"  # Change this!
jwt = JWTManager(app)

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


'''@app.route('/Signup', methods=['POST'])
def Signup():
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


@app.route('/Signin', methods=['POST'])
def Signin():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid data, expected JSON"}), 400

    # Assuming the Member model has appropriate fields (name, email, phone_number, password)
    member = Member(
        name=data.get('name'),
        email=data.get('email'),
        password=data.get('password')
    )

    db.session.add(member)
    db.session.commit()

    return jsonify({"message": "Member logged in successfully"}), 201'''
   
   
@app.route('/protected', methods=['GET'])
class token_required():
    @jwt_required()
    def get(self):
        # Access the identity of the current user with get_jwt_identity
        current_user = get_jwt_identity()
        return {'user_email': current_user}, 200


@app.route('/members', methods =['GET'])
# @token_required
def get_all_users(current_user):
    # querying the database
    # for all the entries in it
    users = Member.query.all()
    # converting the query objects
    # to list of jsons
    output = []
    for user in users:
        # appending the user data json 
        # to the response list
        output.append({
            'public_id': user.public_id,
            'name' : user.name,
            'email' : user.email
        })
  
    return jsonify({'users': output})



@app.route('/login', methods = ['POST'])
def login():
    auth = request.get_json()
    print(auth)
    if not auth or not auth.get('email') or not auth.get('password'):
        return make_response(
            'Could not verify', 401,
            {'WWW-Authenticate': 'Basic realm="User does not exist!!"'}
        )

    member = Member.query\
        .filter_by(email = auth.get('email'))\
        .first()
    #
    #
    if not member:
        # returns 401 if user does not exist
        return make_response(
            'User does not exist',
            401,
            {'WWW-Authenticate' : 'Basic realm ="User does not exist !!"'}
        )

    if check_password_hash(member.password, auth.get('password')):
        # generates the JWT Token
        access_token = create_access_token(identity = auth.get('email'))
        return make_response(jsonify({'token': access_token}), 201)

    return make_response(
        'Invalid password',
        403,
        {'WWW-Authenticate': 'Basic realm="Wrong Password !!"'}
    )
    
@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()

    name, email = data.get('name'), data.get('email')
    password = data.get('password')

    member = Member.query\
        .filter_by(email = email)\
        .first()

    if not member:
        member = Member(
            name=name,
            email=email,
            password=generate_password_hash(password)
        )
        db.session.add(member)
        db.session.commit()

        return make_response('Successfully registered.', 201)
    else:
        return make_response('User already exists. Please Log in', 202)

    
    


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


@app.route("/login", methods=["POST"])
def create_token():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if username != "test" or password != "test":
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)









if __name__ == '__main__':
    app.run(port=5555, debug=True)
    