import os
import sys
import logging

from ariadne import graphql_sync
from ariadne.constants import PLAYGROUND_HTML
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_migrate import Migrate

from .config import Config
from .database import db
from .schema import schema
from .taskmanager import manager as task_manager
from .faces import face_app
from .utils.image import img_arr_to_file
from .utils.logging import get_console_handler


if getattr(sys, "frozen", False):
    static_folder = os.path.join(sys._MEIPASS, "build")
else:
    static_folder = "../build/"

app = Flask(__name__, static_folder=static_folder, static_url_path="/")
CORS(
    app,
    origins=[
        "http://localhost:3000",
        "http://localhost:5000",
    ],
)
app.config.from_object(Config)


# Create loggers and handlers
werkzeug_logger = logging.getLogger("werkzeug")  # grabs underlying WSGI logger
# werkzeug_logger.setLevel(logging.INFO)
werkzeug_logger.addHandler(get_console_handler())

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(get_console_handler())

app.logger.setLevel(logging.DEBUG)

# Setup database
db.init_app(app)

# Setup migration
migrate = Migrate(app, db, directory=app.config["MIGRATION_DIR"])

# Setup task manager
task_manager.init_app(app)

@app.route("/")
def index():
    return "Hello World"

@app.route("/graphql", methods=["GET", "POST"])
def graphql():
    if request.method == "GET":
        return PLAYGROUND_HTML, 200
    else:
        # GraphQL queries are always sent as POST
        data = request.get_json()

        # Note: Passing the request to the context is optional.
        # In Flask, the current request is always accessible as flask.request
        success, result = graphql_sync(
            schema, data, context_value=request, debug=app.debug
        )

        status_code = 200 if success else 400
        return jsonify(result), status_code


from flask import send_file

from .models import Photo


@app.route("/api/image/<int:id>")
def post_image(id):
    """ post image and return the response """
    photo = Photo.query.get(id)
    return send_file("../" + photo.url, mimetype="image/jpeg")

# Register CLI Groups
from .commands import build_cli, data_cli, dev_cli

app.cli.add_command(build_cli)
app.cli.add_command(data_cli)
app.cli.add_command(dev_cli)


@app.shell_context_processor
def make_shell_context():
    return {"db": db}
