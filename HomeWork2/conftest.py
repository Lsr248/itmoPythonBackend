import os
import tempfile

import pytest
from creator import create_app
from db import init_db, insert_data


@pytest.fixture
def app():
    db_fd, db_path = tempfile.mkstemp()

    app = app = create_app(
        {
            "TESTING": True,
            "DATABASE": db_path,
        }
    )

    with app.app_context():
        init_db(db_path)
        insert_data(db_path)

    yield app

    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()
