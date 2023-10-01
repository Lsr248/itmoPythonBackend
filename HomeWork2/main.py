import os
import db
from flask import Flask, request, jsonify, render_template


def create_app():
    app = Flask(__name__)

    @app.route("/hairdressingSalonsSPB")
    def hello_world():
        """
        Get query for main page
        """
        return "Welcome to hairdressingSalonsSPB"

    @app.route("/hairdressingSalonsSPB/salons", methods=["GET"])
    def show_salons():
        """
        Get query for showing all salons
        """
        rating = request.args.get("rating", 0)
        region = request.args.get("region", "")
        result = db.select_salons(rating, region)
        if result:
            return jsonify(result)
        else:
            return render_template("404.html"), 404

    @app.route("/hairdressingSalonsSPB/salons/<id>", methods=["GET"])
    def show_hairdressers(id: int):
        """
        Get query for showing all hairdressers of salon
        """
        result = db.select_hairdressers(id)
        if result:
            return jsonify(result)
        else:
            return render_template("404.html"), 404

    @app.route("/hairdressingSalonsSPB/salons/<id>/<h_id>", methods=["POST"])
    def post_review(id: int, h_id: int):
        """
        Post query for sending review on hairdresser in salon
        """
        text = request.json
        db.insert_review(id, h_id, text["text"])
        return "Success sending review"

    @app.route("/hairdressingSalonsSPB/salons/<id>/<h_id>", methods=["GET"])
    def get_review(id: int, h_id: int):
        """
        Get query for getting all reviews
        """
        result = db.select_reviews(id, h_id)
        if result:
            return jsonify(list(result))
        else:
            return "This hairdresser has no reviews."

    return app


def main():
    db_path = "database.sqlite"
    if not os.path.exists(db_path):
        db.create_db()
        db.insert_data()
    app = create_app()
    app.run(host="0.0.0.0", port=80)


if __name__ == "__main__":
    main()
