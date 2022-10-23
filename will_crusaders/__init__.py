import flask


def create_app():
    return flask.Flask(__name__)
#    app = flask.Flask(__name__)
#    app.run(host="0.0.0.0", port=5000, debug=True, threaded=True)
#    return app
