import pytest
import file_uploader


@pytest.fixture(scope="module")
def test_client():
    """ Defines a pytest fixture for Flask web application. """
    flask_app = file_uploader.app

    # Flask provides a way to test your application by exposing the Werkzeug test Client
    # and handling the context locals for you.
    testing_client = flask_app.test_client()

    # Establish an application context before running the tests.
    ctx = flask_app.app_context()
    ctx.push()

    yield testing_client  # start testing

    ctx.pop()
