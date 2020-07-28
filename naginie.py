import os 
from naginie.app import Naginie
root = os.path.dirname(__file__)

app = Naginie('naginie_demo').create_app(
	os.path.join(root, 'naginie_themes')
)

