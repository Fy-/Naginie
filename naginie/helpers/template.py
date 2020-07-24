import os 

from ..naginie import options

__tpl_dir__ = False

def tpl_dir(page):
	return '%s/%s' % (options.get('theme'), page)
	
def get_tpl_name():
	return options.get('theme')