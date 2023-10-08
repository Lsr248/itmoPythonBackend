import db as db
from creator import create_app


def main():
    app = create_app()
    db.init_db(app.config["DATABASE"])
    db.insert_data(app.config["DATABASE"])
    app.run(host="0.0.0.0", port=80)


if __name__ == "__main__":
    main()
