from naginie import Naginie

def create_app(naginie_config=None, **kwargs):
	naginie = Naginie(
		naginie_config,
		'naginie_demo'
	)

	return naginie.app

