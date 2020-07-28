#: Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy_mptt import mptt_sessionmaker

#: Naginie
from .helpers.naginie_options import NaginieOptions

class NaginieSQLAlchemy(SQLAlchemy):
	def create_session(self, options):  
		Session = super().create_session(options)
		return mptt_sessionmaker(Session)

db = NaginieSQLAlchemy()
options = NaginieOptions()
migrate = Migrate()
cors = CORS(resources={r"/api/*": {"origins": "*"}})