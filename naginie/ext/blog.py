
class NBlogDirectory(object):
	__name__ = 'Blog Directory'
	__slug__ = 'blog_dir'

	def __init__(self, naginie_directory):
		self.naginie_directory = naginie_directory
		
	@staticmethod
	def on_load(*args, **kwargs):
		pass

	@staticmethod
	def clear_ext(naginie):
		pass