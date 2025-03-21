"""Blueprint module for the API routes of the application."""

from flask import Blueprint, jsonify
from api.routes.quiz_gen_api import core_quiz_gen_bp

api_blueprint = Blueprint("API", __name__, url_prefix="/api/")
api_blueprint.register_blueprint(core_quiz_gen_bp)


@api_blueprint.route("/", methods=["GET"])
def get_data():
    """Return a simple JSON response to indicate the API is running."""
    return jsonify({"message": "Quizzatron API is up and running!🚀"})
