from sqlalchemy_mptt import mptt_sessionmaker
from flask_sqlalchemy import SQLAlchemy

class NaginieSQLAlchemy(SQLAlchemy):
	def create_session(self, options):	
		Session = super().create_session(options)
		return mptt_sessionmaker(Session)