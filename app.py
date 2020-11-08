import os
from flask import Flask, render_template
from flask_cors import CORS
from api.models import setup_db


def create_app(test_config=None):

    template_dir = os.path.abspath("client/dist")
    app = Flask(
        __name__,
        static_url_path='',
        template_folder=template_dir,
        static_folder=template_dir,
    )
    setup_db(app)
    CORS(app)

    @app.route("/", defaults={"path": ""})
    @app.route("/<path:path>")
    def catch_all(path):
        return render_template("index.html")

    return app


app = create_app()

if __name__ == "__main__":
    app.run()