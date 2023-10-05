from random import choice as rc
from faker import Faker
from app import app
from models import db, Exercise, Member

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
        for _ in range(5):  # Loop through the desired number of exercises per member
            exercise = Exercise(
                name=fake.name(),
                type=fake.word(),
                muscle=fake.word(),
                equipment=fake.word(),
                difficulty=fake.word(),
                instructions=fake.sentence(),
                member=member  # Associate the exercise with the member
            )
            exercises.append(exercise)

        # Set the exercises for the member
        member.exercises = exercises
        members.append(member)

    # Add all members to the session and commit
    db.session.add_all(members)
    db.session.commit()
