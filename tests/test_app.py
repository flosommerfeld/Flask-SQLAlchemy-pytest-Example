from src.app import get_value


def test_get_value(flask_app_mock, mock_my_model, mock_get_sqlalchemy):
    """ This test will call the function under test (get_value()) and succeeds if
    get_value() returns the ID of MyModel which shall be 'my_mock_id'."""
    mock_get_sqlalchemy.first.return_value = mock_my_model

    with flask_app_mock.app_context():
        response = get_value() # call the function under test

    # check if we've gotten our mocked model object
    assert response[0].json == "my_mock_id"
