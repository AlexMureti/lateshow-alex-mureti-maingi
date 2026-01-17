from server.app import create_app
from server.config import db
from server.models import Episode, Guest, Appearance

app = create_app()

with app.app_context():
    # Clear existing data
    db.drop_all()
    db.create_all()

    # Create episodes
    episodes = [
        Episode(date="1/11/99", number=1),
        Episode(date="1/12/99", number=2),
        Episode(date="1/13/99", number=3),
    ]
    
    # Create guests
    guests = [
        Guest(name="Michael J. Fox", occupation="actor"),
        Guest(name="Sandra Bernhard", occupation="Comedian"),
        Guest(name="Tracey Ullman", occupation="television actress"),
    ]
    
    db.session.add_all(episodes)
    db.session.add_all(guests)
    db.session.commit()

    # Create appearances
    appearances = [
        Appearance(rating=4, episode_id=1, guest_id=1),
        Appearance(rating=5, episode_id=2, guest_id=2),
        Appearance(rating=5, episode_id=3, guest_id=3),
    ]
    
    db.session.add_all(appearances)
    db.session.commit()

    print("Seed complete.")
