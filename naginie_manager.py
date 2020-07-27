from flask_migrate import MigrateCommand
from flask_script import Manager
import pprint, csv

from naginie_demo import create_app
from config import Config
from naginie.naginie import db
from naginie.models import *

pp = pprint.PrettyPrinter(indent=4)
app = create_app(Config)
migrate = app.migrate
manager = Manager(app)
manager.add_command('db', MigrateCommand)

@manager.command
def clear_db():
	db.drop_all()
	db.create_all()
	db.session.commit()

@manager.command
def init_naginie():
	db.drop_all()
	db.create_all()
	db.session.commit()
	print('*** Adding root directory')
	db.session.add(NaginieDirectory(title="Naginie", slug="/", description="My Naginie Website")) 

	print('*** Setting options')
	NaginieOption.set('theme', 'ron')

	print('*** Adding default roles')
	db.session.add(NaginieStatus(title='Administrator', role=NaginieRole.administrator, description='Somebody who needs to be aware of the Peter Parker principle: With great power comes great responsibility.'))
	db.session.add(NaginieStatus(title='Editor', role=NaginieRole.editor, description='Somebody who can publish and manage posts including the posts of other users.'))
	db.session.add(NaginieStatus(title='Author', role=NaginieRole.author, description='Somebody who can publish and manage their own posts.'))
	db.session.add(NaginieStatus(title='Contributor', role=NaginieRole.contributor, description='Somebody who can write and manage their own posts but cannot publish them.'))
	db.session.add(NaginieStatus(title='Subscriber', role=NaginieRole.subscriber, description='Your VIP club /o/'))

	db.session.commit()
	admin_role = NaginieStatus.query.filter(NaginieStatus.id==1).first()

	print('*** Adding first user')
	db.session.add(NaginieUser(email='m@fy.to', password='stay', username='Fy', id_status=admin_role.id))
	db.session.commit()

### TESTS ###
@manager.command
def test_users():
	with open('./naginie_tests/datas/users.csv', "r") as f:
		reader = csv.reader(f)
		for row in reader:
			db.session.add(NaginieUser(
					email=row[0], 
					password='test', 
					firstname=row[1],
	                lastname=row[2]
                )
			)
		db.session.commit()
"""
@manager.command
def show_directories():
	directories = NaginieDirectory.query.all()
	for item in directories:
	    #pp.pprint(item.drilldown_tree(json=True, json_fields=NaginieDirectory.to_dict))
	    pp.pprint(item.path_to_root().all())

@manager.command
def fill_directories():
	db.session.add(NaginieDirectory(title="root", slug="root", description="root desc")) 
	db.session.add_all(
	    [
	        NaginieDirectory(title="foo", slug="foo", description="foo desc", parent_id=1),
	        NaginieDirectory(title="bar", slug="bar", description="bar desc", parent_id=2),
	        NaginieDirectory(title="baz", slug="baz", description="baz desc", parent_id=3),
	    ]
	)
	db.session.add_all( 
	    [
	        NaginieDirectory(title="foo1", slug="foo1", description="foo1 desc", parent_id=1),
	        NaginieDirectory(title="bar1", slug="bar1", description="bar1 desc", parent_id=5),
	        NaginieDirectory(title="baz1", slug="baz1", description="baz1 desc", parent_id=5),
	    ]
	)
	db.session.commit()

@manager.command
def test_directories():
	fd = NaginieDirectory.query.filter(NaginieDirectory.id==1).first()
	print(fd)
	 
	r = NaginieDirectory.get_tree(fd, {})
	print(r)
"""

if __name__ == '__main__':
	manager.run()

