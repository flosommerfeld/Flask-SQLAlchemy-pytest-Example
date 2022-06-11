# Flask-SQLAlchemy-pytest-Example
Example for unit testing Flask applications with pytest when the function under test uses SQLAlchemy. Adapted from https://medium.com/analytics-vidhya/pytest-mocking-cheatsheet-dcebd84876e3 

## Example
### Flask application
```
app = Flask(__name__) # instantiate app
app.config.from_object("config.TestingConfig") # load testing config from config.py
db = SQLAlchemy() # instantiate sqlalchemy
db.init_app(app) # link sqlalchemy to app

# Example for a database model
class MyModel(db.Model):
    id = db.Column("id", VARCHAR, primary_key=True, unique=True, nullable=False)

# Example route
@app.route("/", methods=['GET'])
def get_value():
    mod = MyModel.query.first()
    return jsonify(mod.id), 200
```

### Testing
#### Test case
```
def test_get_value(flask_app_mock, mock_my_model, mock_get_sqlalchemy):
    """ This test will call the function under test (get_value()) and succeeds if
    get_value() returns the ID of MyModel which shall be 'my_mock_id'."""
    mock_get_sqlalchemy.first.return_value = mock_my_model

    with flask_app_mock.app_context():
        response = get_value() # call the function under test

    # check if we've gotten our mocked model object
    assert response[0].json == "my_mock_id"

```

#### Test configuration
```
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

```


## Requirements
Make sure that
- [Python](https://www.python.org/),
- [pipenv](https://pipenv.pypa.io/en/latest/)

are installed on your system.

## Quick Start
- Run `make install` to install the projects dependencies.
- Run `make run` to run the server.
- Run `make test` to run the tests.
