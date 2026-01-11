from server.app import create_app
from server.config import db
from server.models import Episode, Guest, Appearance

app = create_app()

with app.app_context():
    db.create_all()

    e1 = Episode(date="1/11/99", number=1)
    g1 = Guest(name="Michael J. Fox")

    db.session.add_all([e1, g1])
    db.session.commit()

    a1 = Appearance(rating=5, episode_id=e1.id, guest_id=g1.id)
    db.session.add(a1)
    db.session.commit()

    print("Seed complete.")
