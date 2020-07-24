from flask_sqlalchemy import sqlalchemy

class NaginieOptions(object):
	def __init__(self):
		self.options = {}

	def init_app(self, app):
		from ..models.naginie_option import NaginieOption
		try:
			result = {}
			with app.app_context():
				_options = NaginieOption.query.filter().all()
			
				for opt in _options:
					result[opt.key] = opt.value

				self.options = result

		except sqlalchemy.exc.ProgrammingError:
			print()
			print('*** WARNING: Empty DB run: python naginie_manager.py init_naginie.')
			print()
				
	def get(self, key):
		if key in self.options:
			return self.options[key]
		return '__not_loaded__'