import pytest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src.app import MyModel


@pytest.fixture
def mock_my_model():
    """ 
    This fixture mocks the database model 'MyModel' which will have the id 'my_mock_id'. 
    This id can be used in the test cases.
    """
    my_model = MyModel(
        id="my_mock_id",
    )
    return my_model


@pytest.fixture
def mock_get_sqlalchemy(mocker):
    """ This fixture will mock the SQLAlchemy query response from the database """
    mock = mocker.patch(
        "flask_sqlalchemy._QueryProperty.__get__").return_value = mocker.Mock()
    return mock


@pytest.fixture
def flask_app_mock():
    """ Flask application mock set up. """
    app_mock = Flask(__name__)
    db = SQLAlchemy(app_mock)
    db.init_app(app_mock)
    return app_mock
