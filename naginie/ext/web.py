
class NWebDirectory(object):
	__name__ = 'Web Directory'
	__slug__ = 'web_dir'

	def __init__(self, naginie_directory):
		self.naginie_directory = naginie_directory

	@staticmethod
	def on_load(*args, **kwargs):
		naginie = kwargs.get('naginie')
		pass

	@staticmethod
	def clear_ext(naginie):
		pass