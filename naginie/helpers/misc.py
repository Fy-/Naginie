def enum_to_select(C):
	r = []
	for k, v in enumerate(C):
		r.append((str(v).split(".")[1], str(v).split(".")[1].capitalize()))

	return r
	
def get_enum_value_from_str(c, s):
	s = s.lower()
	for k, v in enumerate(c):
		if s == str(v).split(".")[1]:
			return v
	return -1

def teen_hax0rzz_name(version='0.1'):
	#: Memories from chimdhood.
	print(
'''
  ███    ██  █████   ██████  ██ ███    ██ ██ ███████ 
  ████   ██ ██   ██ ██       ██ ████   ██ ██ ██      
  ██ ██  ██ ███████ ██   ███ ██ ██ ██  ██ ██ █████   
  ██  ██ ██ ██   ██ ██    ██ ██ ██  ██ ██ ██ ██      
  ██   ████ ██   ██  ██████  ██ ██   ████ ██ ███████ 
			
  Version: %s                                      
  A python/flask/sqlalchemy/vuejs CMS
  By Florian "Fy" Gasquez (m@fy.to)
''' % version
	)

