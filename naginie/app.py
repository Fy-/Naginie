from flask import Flask

import logging
import sys

from naginie.helpers.misc import teen_hax0rzz_name
from naginie.extensions import (
	db,
	options,
	migrate,
	cors
)
from naginie.ext import ( 
	NWebDirectory,
	NBlogDirectory
)

__version__ = '0.1'

class Naginie(object):
	__directory_ext__ = {}
	__files_ext__ = {}
	__version__ = '0.1'

	@staticmethod 
	def add_ext(ext, *args, **kwargs):
		print('   * Loading %s (%s)' % (ext.__name__, ext))
		Naginie.__directory_ext__[ext.__slug__] = {
			'name': ext.__name__,
			'class': ext
		}
		ext.on_load(*args, **kwargs)

	def __init__(self, name=False):
		self.name = name if name else "naginie_app"

	def create_app(self, theme_directory, config_object="naginie.settings"):
		self.app = Flask(self.name, template_folder=theme_directory)
		self.app.config.from_object(config_object)
		self.register_naginie_directories()
		self.register_extensions()
		self.register_blueprints()
		self.configure_logger()		
		return self.app
		
	def register_extensions(self):
		db.init_app(self.app)
		migrate.init_app(self.app, db, directory='__alembic_%s' % self.name)
		cors.init_app(self.app)

		options.init_app(self.app)

	def register_naginie_directories(self):
		print('\n\n##############################################################################')
		teen_hax0rzz_name(Naginie.__version__)
		Naginie.add_ext(NWebDirectory, naginie=self)
		Naginie.add_ext(NBlogDirectory,  naginie=self)
		print('\n##############################################################################\n\n')

	def register_blueprints(self):
		from naginie.routes import (
			default_bp, admin_bp, api_user_bp, api_directory_bp
		)
		## Front
		self.app.register_blueprint(default_bp)

		## API & Admin
		self.app.register_blueprint(admin_bp)
		self.app.register_blueprint(api_user_bp)
		self.app.register_blueprint(api_directory_bp)

	def configure_logger(self):
		self.handler = logging.StreamHandler(sys.stdout)
		if not self.app.logger.handlers:
			self.app.logger.addHandler(handler)

