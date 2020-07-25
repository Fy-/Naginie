from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import os

from .helpers.naginie_sqlalchemy import NaginieSQLAlchemy
from .helpers.naginie_options import NaginieOptions
from .helpers.misc import teen_hax0rzz_name

db = NaginieSQLAlchemy()
options = NaginieOptions()

__version__ = '0.1'

class Naginie(object):
	def __init__(self, config, name=False):
		_name = name if name else "naginie_app"
		teen_hax0rzz_name(__version__)
		self.app = Flask(_name, template_folder=config.THEMES_DIRECTORY)
		self.app.config.from_object(config)

		db.init_app(self.app)

		self.app.migrate = Migrate(self.app, db, directory='__alembic_%s' % _name)

		options.init_app(self.app)
		cors = CORS(self.app, resources={r"/api/*": {"origins": "*"}})
		
		from .routes import default_bp, admin_bp, api_bp
		self.app.register_blueprint(default_bp)
		self.app.register_blueprint(admin_bp)
		self.app.register_blueprint(api_bp)
