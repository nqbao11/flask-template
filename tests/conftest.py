import os
import sys

import pytest
from sqlalchemy.orm import scoped_session

from main import app as _app
from main import db
from main.libs.log import get_logger
from main.models.base import BaseModel

logger = get_logger(__name__)

if os.getenv("ENVIRONMENT") != "test":
    logger.error('Tests should be run with "ENVIRONMENT=test"')
    sys.exit(1)


@pytest.fixture(scope="session", autouse=True)
def app():
    ctx = _app.test_request_context()
    ctx.push()

    yield _app

    ctx.pop()


@pytest.fixture(scope="session", autouse=True)
def create_database(app):
    engine = db.session.bind.engine

    BaseModel.metadata.drop_all(engine)
    BaseModel.metadata.create_all(engine)


@pytest.fixture(scope="function", autouse=True)
def session():
    from sqlalchemy.orm import sessionmaker

    connection = db.session.bind.engine.connect()
    transaction = connection.begin()

    session_factory = sessionmaker(bind=connection)
    db.session = scoped_session(session_factory)

    yield

    transaction.rollback()
    connection.close()
    db.session.close()


@pytest.fixture(scope="function", autouse=True)
def client(app):
    return app.test_client()
