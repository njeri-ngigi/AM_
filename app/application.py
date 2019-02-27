from flask import Flask
from flask_restplus import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from app.instance.config import app_config

# uses __name__ as a starting point
app = Flask(__name__)

api = Api(app, catch_all_404s=True)

app.url_map.strict_slashes = False
app.config.from_object(app_config['development'])

db = SQLAlchemy()
db.init_app(app)
migrate = Migrate(app, db)

# TODO: setup database properly to create tables and columns

from app import routes
