import db
from flask import Flask, jsonify, render_template, request


def create_app(test_config=None):
    app = Flask(__name__)

    app.config.from_mapping(
        DATABASE="database.sqlite",
    )
    if test_config is not None:
        app.config.from_mapping(test_config)

    @app.route("/hairdressingSalonsSPB")
    def hello_world():
        """
        Get query for main page
        """
        return "Welcome to hairdressingSalonsSPB!"

    @app.route("/hairdressingSalonsSPB/salons", methods=["GET"])
    def show_salons():
        """
        Get query for showing all salons
        """
        rating = request.args.get("rating", 0)
        region = request.args.get("region", "")
        result = db.select_salons(rating, region, app.config["DATABASE"])
        if result:
            return jsonify(result)
        else:
            return "Sorry, salons not found."

    @app.route("/hairdressingSalonsSPB/salons/<id>", methods=["GET"])
    def show_hairdressers(id: int):
        """
        Get query for showing all hairdressers of salon
        """
        result = db.select_hairdressers(id, app.config["DATABASE"])
        if result:
            return jsonify(result)
        else:
            return "Server error"

    @app.route("/hairdressingSalonsSPB/salons/<id>/<h_id>", methods=["POST"])
    def post_review(id: int, h_id: int):
        """
        Post query for sending review on hairdresser in salon
        """
        text = request.json
        db.insert_review(id, h_id, text["text"], app.config["DATABASE"])
        return "Success sending review"

    @app.route("/hairdressingSalonsSPB/salons/<id>/<h_id>", methods=["GET"])
    def get_review(id: int, h_id: int):
        """
        Get query for getting all reviews
        """
        result = db.select_reviews(id, h_id, app.config["DATABASE"])
        if result:
            return jsonify(result)
        else:
            return jsonify(["This hairdresser has no reviews."])

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("404.html", title="404"), 404

    return app
