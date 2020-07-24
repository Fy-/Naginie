import datetime

from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method

from ..naginie import db

role_user = db.Table('naginie_role_user',
	db.Column('user_id', db.Integer(), db.ForeignKey('naginie_user.id')),
	db.Column('role_id', db.Integer(), db.ForeignKey('naginie_role.id'))
)

class NaginieRole(db.Model):
	__tablename__ = 'naginie_role'
	id = db.Column(db.Integer(), primary_key=True)
	title = db.Column(db.String(96))
	description = db.Column(db.String(160))

	def __repr__(self):
		return '<NaginieRole id="%s" title="%s">' % (self.id, self.title)

	def __unicode__(self):
		return '%s' % self.name

	def to_dict(self):
		return NaginieRole.to_dict(self)

	@staticmethod
	def to_dict(n_role):
		return {
			'id': n_role.id,
			'title': n_role.title,
			'description': n_role.description,
		}


class NaginieUser(db.Model):
	__tablename__ = 'naginie_user'

	id	= db.Column(db.Integer, primary_key = True)
	created = db.Column(db.DateTime(), default=datetime.datetime.now)
	updated = db.Column(db.DateTime(), default=datetime.datetime.now)
	logged = db.Column(db.DateTime(), default=datetime.datetime.now)

	email = db.Column(db.String(120), unique=True, index=True, nullable=False)
	username = db.Column(db.String(80), nullable=True)
	lastname = db.Column(db.String(80), nullable=True)
	firstname = db.Column(db.String(80), nullable=True)
	_password = db.Column("password", db.String(120), nullable=False)
	roles = db.relationship(
		'NaginieRole', secondary=role_user, lazy='subquery',
		backref=db.backref('naginie_user', lazy=True)
	)

	def _get_password(self):
		return self._password

	def _set_password(self, password):
		if not password:
			return

		self._password = generate_password_hash(password)

	password = db.synonym("_password", descriptor=property(_get_password, _set_password))

	email_verified = db.Column(db.Boolean, default=False)
	tmp_hash = db.Column(db.String(80), index=True, unique=True, nullable=True)

	def __repr__(self):
		return '<NaginieRole id="%s" nicename="%s">' % (self.id, self.nicename)

	def __unicode__(self):
		return '%s' % self.nicename

	def to_dict(self):
		return NaginieUser.to_dict(self)

	@staticmethod
	def to_dict(n_user):
		return {
			'id': n_user.id,
			'nicename': self.nicename,
			'email': self.email,
			'username': self.username,
			'lastname': self.lastname,
			'firstname': self.firstname,
			'created': self.created.isoformat(),
			'updated': self.updated.isoformat(),
			'logged': self.logged.isoformat()
		}

	def check_password(self, password):
		if self.password == None:
			return False
		return check_password_hash(self.password, password)

	@hybrid_property
	def nicename(self):
		if self.username:
			return self.username
		elif self.firstname and self.lastname:
			return '%s %s' % (self.fistname, self.lastname)
		elif self.firstname:
			return self.firstname
		elif self.lastname:
			return self.lastname
		else:
			return self.email.split('@')[0]
