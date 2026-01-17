from flask import Blueprint, request, jsonify
from . import db
from .models import Episode, Guest, Appearance

bp = Blueprint('main', __name__)


@bp.route("/episodes", methods=["GET"])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([e.to_dict() for e in episodes])


@bp.route("/episodes/<int:id>", methods=["GET"])
def get_episode(id):
    episode = Episode.query.get(id)
    if not episode:
        return jsonify({"error": "Episode not found"}), 404
    return jsonify(episode.to_dict(include_appearances=True))


@bp.route("/guests", methods=["GET"])
def get_guests():
    guests = Guest.query.all()
    return jsonify([g.to_dict() for g in guests])


@bp.route("/appearances", methods=["POST"])
def create_appearance():
    data = request.get_json()
    try:
        new_appearance = Appearance(
            rating=data.get("rating"),
            episode_id=data.get("episode_id"),
            guest_id=data.get("guest_id")
        )
        db.session.add(new_appearance)
        db.session.commit()
        return jsonify(new_appearance.to_dict()), 201
    except ValueError as e:
        db.session.rollback()
        return jsonify({"errors": [str(e)]}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"errors": [str(e)]}), 400