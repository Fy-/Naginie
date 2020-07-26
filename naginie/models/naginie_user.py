import datetime
import jwt

from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method
from flask import current_app, jsonify, request

from ..naginie import db
from ..helpers.messages import * 



role_user = db.Table('naginie_role_user',
	db.Column('user_id', db.Integer(), db.ForeignKey('naginie_user.id')),
	db.Column('role_id', db.Integer(), db.ForeignKey('naginie_role.id'))
)

class NaginieRole(db.Model):
	__tablename__ = 'naginie_role'
	id = db.Column(db.Integer(), primary_key=True)
	title = db.Column(db.String(96))
	slug = db.Column(db.String(80), unique=True)
	description = db.Column(db.String(160))

	def __repr__(self):
		return '<NaginieRole id="%s" title="%s">' % (self.id, self.title)

	def __unicode__(self):
		return '%s' % self.name

	def _to_dict(self):
		return NaginieRole.to_dict(self)

	@staticmethod
	def to_dict(n_role):
		return {
			'id': n_role.id,
			'slug': n_role.slug,
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

	def _to_dict(self, roles=False):
		return NaginieUser.to_dict(self, roles)

	@staticmethod
	def to_dict(n_user, roles=False):
		r =  {
			'id': n_user.id,
			'nicename': n_user.nicename,
			'email': n_user.email,
			'username': n_user.username,
			'lastname': n_user.lastname,
			'firstname': n_user.firstname,
			'created': n_user.created.isoformat(),
			'updated': n_user.updated.isoformat(),
			'logged': n_user.logged.isoformat()
		}
		r['roles'] = []
		r['roles_by_slug'] = []
		for _role in n_user.roles:
			r['roles'].append(_role._to_dict())
			r['roles_by_slug'].append(_role.slug)
		return r

	@classmethod
	def authenticate(cls, **kwargs):
		email = kwargs.get('email')
		password = kwargs.get('password')
		if not email or not password:
			return None

		user = NaginieUser.query.filter(NaginieUser.email==email).first()
		if user and user.check_password(password):
			return user
			
		return None

	def check_password(self, password):
		if self.password == None:
			return False
		return check_password_hash(self.password, password)

	@hybrid_property
	def nicename(self):
		if self.username:
			return self.username
		elif self.firstname and self.lastname:
			return '%s %s' % (self.firstname, self.lastname)
		elif self.firstname:
			return self.firstname
		elif self.lastname:
			return self.lastname
		else:
			return self.email.split('@')[0]

class RoleRequired(object):
	__roles_by_slug = {}
	__roles_needs_update = True

	def __init__(self, roles=[]):
		self.roles = roles

	def update_roles(self):
		if RoleRequired.__roles_needs_update:
			_roles = NaginieRole.query.filter().all()
			RoleRequired.__roles_by_slug = {}
			for _role in _roles:
				RoleRequired.__roles_by_slug[_role.slug] = _role

			#RoleRequired.__roles_needs_update = False

	def check_roles(self, user, roles):
		if len(roles) == 0 and user:
			return True
		else:
			for role in roles:
				if role not in RoleRequired.__roles_by_slug:
					print('*** Warning: checking vs an unknown role: %s.' % role)
					continue

				if RoleRequired.__roles_by_slug[role] in user.roles:
					return True
			return False

	def __call__(self, f):
		def wrapped_f(*args, **kwargs):
			auth_headers = request.headers.get('Authorization', '').split()

			if len(auth_headers) != 2:
				return jsonify(auth_invalid_msg), 401
			try:
				token = auth_headers[1]
				data = jwt.decode(token, current_app.config['SECRET_KEY'])
				user = NaginieUser.query.filter(NaginieUser.id==data['user']['id']).first()
				self.update_roles()

				if not user:
					raise RuntimeError('User not found')

				if not self.check_roles(user, self.roles):
					return jsonify(auth_invalid_role), 403
				return f(user, *args, **kwargs)
			except jwt.ExpiredSignatureError:
				return jsonify(auth_expired_msg), 401 # 401 is Unauthorized HTTP status code
			except (jwt.InvalidTokenError, Exception) as e:
				print(e)
				return jsonify(auth_invalid_msg), 401
		return wrapped_f