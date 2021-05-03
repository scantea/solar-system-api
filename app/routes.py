

from app import db
from app.models.planet import Planet
from flask import request, Blueprint, make_response, jsonify

planet_bp = Blueprint("planet", __name__, url_prefix="/planets")


@planet_bp.route("", methods=["GET", "POST"])
def handle_planets():
    if request.method == "GET":
        planets = Planet.query.all()
        planets_response = []
        for planet in planets:
            planets_response.append({
                "id": planet.id,
                "name": planet.name,
                "description": planet.description
            })
        return jsonify(planets_response)
    elif request.method == "POST":
        request_body = request.get_json()
        new_planet = Planet(name=request_body["name"],
                            description=request_body["description"])

        db.session.add(new_planet)
        db.session.commit()

        return make_response(
            f"Planet {new_planet.name} successfully created", 201)


@planet_bp.route("/<planet_id>", methods=["GET", "PUT", "DELETE"])
def handle_planet(planet_id):

    planet = Planet.query.get(planet_id)

    if planet is None:
        return make_response(f"Planet with id {planet_id} is not found", 404)

    elif request.method == "GET":
        return {
            "id": planet.id,
            "name": planet.name,
            "description": planet.description
        }

    elif request.method == "PUT":
        form_data = request.get_json()
        planet.name = form_data["name"]
        planet.description = form_data["description"]
        db.session.commit()
        return make_response(f"Planet #{planet.id} successfully updated")

    elif request.method == "DELETE":
        db.session.delete(planet)
        db.session.commit()
        return make_response(f"Planet #{planet.id} successfully deleted")

        # try:

        #     planet = Planet.query.get(planet_id)

        #     return {
        #         "id": planet.id,
        #         "name": planet.name,
        #         "description": planet.description
        #     }
        # except BaseException:
        #     return {
        #         "error": True,
        #         "description": "Error, planet ID not found"
        #     }, 404
