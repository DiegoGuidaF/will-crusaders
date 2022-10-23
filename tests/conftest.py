#import flask
#import pytest
from fastapi.testclient import TestClient

#@pytest.fixture()
#def app():
#    #app = flask.Flask(__name__)
#    app.config.update({
#        "TESTING": True,
#    })
#
#    # other setup can go here
#
#    yield app
#
#    # clean up / reset resources here
#
#
#@pytest.fixture()
#def client(app):
#    return app.test_client()
#
#
#@pytest.fixture()
#def runner(app):
#    return app.test_cli_runner()