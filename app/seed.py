from random import choice as rc
from faker import Faker
from app import app, db  # Import the 'db' from your Flask app
from models import Exercise, Member
import requests

def fetch_data_from_api():
    muscle = 'biceps'
    api_url = 'https://api.api-ninjas.com/v1/exercises?muscle={}'.format(muscle)
    response = requests.get(api_url, headers={'X-Api-Key': 'iUot3Px10NcYQadCWz/qJQ==GsNy1hGoaGHhT2V1'})
    if response.status_code == requests.codes.ok:
        return response.json()  # Return the JSON data from the API response
    else:
        print("Error:", response.status_code, response.text)
        return []  # Return an empty list in case of an error

# Ensure you fetch the data before creating fake data
items = fetch_data_from_api()

fake = Faker()

# Define some fake data lists
emails = [
    "qy9g0@example.com",
    "t6l4w3@example.com",
    "t9w5k2@example.com"
]

phone_numbers = [
    "(123) 456-7890",
    "(987) 654-3210",
    "(194) 528-3607"
]

passwords = [
    "J#p2&Lz4@",
    "K4!p8Tq2@",
    "W4!g1Zm6$"
]

with app.app_context():

    # Delete all existing records to start fresh
    db.session.query(Exercise).delete()
    db.session.query(Member).delete()
    
    members = []
    
    # Create 3 Member instances and associate exercises with each member
    for _ in range(3):  # Loop through the desired number of members

        member = Member(
            name=fake.name(),
            email=rc(emails),
            phone_number=rc(phone_numbers),
            password=rc(passwords)
        )

        exercises = []

        # Create 5 Exercise instances for each member
        for item in items:  # Loop through the fetched exercise data
            exercise = Exercise(
                name=item.get('name'),  # Access data using 'get'
                type=item.get('type'),
                muscle=item.get('muscle'),
                equipment=item.get('equipment'),  # Correct the typo 'equipement'
                difficulty=item.get('difficulty'),
                instructions=item.get('instructions'),
                member=member  # Associate the exercise with the member
            )
            exercises.append(exercise)

        # Set the exercises for the member
        member.exercises = exercises
        members.append(member)

    # Add all members to the session and commit
    db.session.add_all(members)
    db.session.commit()
