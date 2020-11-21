import os
from flask import Flask, render_template, jsonify
from flask_cors import CORS
from api.models import setup_db
from requests import request
from api import blueprint
from error_handlers import AuthError, ApiError


def create_app(test_config=None):

    template_dir = os.path.abspath("client/dist")
    app = Flask(
        __name__,
        static_url_path="",
        template_folder=template_dir,
        static_folder=template_dir,
    )
    CORS(app)

    app.db = setup_db(app)

    @app.route("/", defaults={"path": ""})
    @app.route("/<path:path>")
    def catch_all(path):
        return render_template("index.html")

    @app.errorhandler(422)
    def unprocessable(error):
        return (
            jsonify(
                {"success": False, "error": 422, "message": "unprocessable"}
            ),
            422,
        )

    @app.errorhandler(AuthError)
    def auth_error(error):
        return (
            jsonify({"success": False, "message": error.message}),
            error.status_code or 401,
        )

    @app.errorhandler(ApiError)
    def api_error(error):
        return (
            jsonify({"success": False, "message": error.message}),
            error.status_code or 400,
        )

    app.register_blueprint(blueprint)
    return app


app = create_app()

if __name__ == "__main__":
    app.run()