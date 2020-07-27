import datetime
import jwt
import re
import enum

from functools import wraps

from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method
from flask import current_app, jsonify, request

from ..naginie import db
from ..helpers.messages import * 


"""
role_user = db.Table('naginie_role_user',
	db.Column('user_id', db.Integer(), db.ForeignKey('naginie_user.id')),
	db.Column('role_id', db.Integer(), db.ForeignKey('naginie_role.id'))
)
"""

class NaginieRole(enum.Enum):
	administrator = 1
	editor = 2
	author = 3
	contributor = 4
	subscriber = 5

class NaginieStatus(db.Model):
	__tablename__ = 'naginie_status'
	id = db.Column(db.Integer(), primary_key=True)
	title = db.Column(db.String(96))
	description = db.Column(db.String(160))
	role = db.Column(db.Enum(NaginieRole), index=True, nullable=False, default='member')
	users = db.relationship("NaginieUser", back_populates="status", lazy="joined", order_by="desc(NaginieUser.id)")

	def __repr__(self):
		return '<NaginieStatus id="%s" title="%s" role="%s">' % (self.id, self.title, self.role_str)

	def __unicode__(self):
		return '%s' % self.name

	@hybrid_property
	def role_str(self):
		return str(self.role).replace("NaginieRole.", "").capitalize()

	def _to_dict(self):
		return NaginieStatus.to_dict(self)

	@staticmethod
	def to_dict(n_status):
		return {
			'id': n_status.id,
			'title': n_status.title,
			'role': n_status.role_str,
			'description': n_status.description,
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

	id_status = db.Column(db.Integer, db.ForeignKey("naginie_status.id"))
	status = db.relationship(
		"NaginieStatus", back_populates="users", lazy="joined", uselist=False
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
		return '<NaginieStatus id="%s" nicename="%s">' % (self.id, self.nicename)

	def __unicode__(self):
		return '%s' % self.nicename

	def _to_dict(self, prev_next=False):
		return NaginieUser.to_dict(self, prev_next)

	@staticmethod
	def to_dict(n_user, prev_next=False):
		r =  {
			'id': n_user.id,
			'nicename': n_user.nicename,
			'email': n_user.email,
			'username': n_user.username,
			'lastname': n_user.lastname,
			'firstname': n_user.firstname,
			'created': n_user.created.isoformat(),
			'updated': n_user.updated.isoformat(),
			'logged': n_user.logged.isoformat(),
			'status': n_user.status._to_dict()
		}


		if prev_next:
			r['prev_next'] = n_user.prev_next

		return r

	@classmethod
	def authenticate(cls, **kwargs):
		email = kwargs.get('email')
		password = kwargs.get('password')
		if not email or not password:
			return None

		user = NaginieUser.query.filter(NaginieUser.email==email).first()
		if user and user.check_password(password):
			user.logged = datetime.datetime.now()
			db.session.add(user)
			db.session.commit()
			return user
			
		return None

	def check_password(self, password):
		if self.password == None:
			return False
		return check_password_hash(self.password, password)


	@hybrid_property
	def prev_next(self):
		_n = NaginieUser.query.filter(NaginieUser.id > self.id).order_by(NaginieUser.id.asc()).first()
		_p = NaginieUser.query.filter(NaginieUser.id < self.id).order_by(NaginieUser.id.desc()).first()

		r = {
			'next' : _n.id if _n else False,
			'prev' : _p.id if _p else False,
		}

		return r

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

	@staticmethod
	def check_password_format(pwd):
		if not pwd or pwd == "":
			return 'Password can\'t be empty.'
		elif len(pwd) > 32 or len(pwd) < 4:
			return 'Password must be between 4 and 32 characters.'
		return True


	@staticmethod
	def check_email_format(email):
		if not email or email == "":
			return 'E-mail can\'t be empty.'
		elif "@" not in email or not re.search( r'(\w+[.|\w])*@(\w+[.])*\w+', email):
			return 'Incorrect e-mail.'
		exist = NaginieUser.query.filter(NaginieUser.email==email).first()
		if exist: 
			return 'E-mail already in use.'

		return True

"""
__roles_by_slug = {}
__roles_needs_update = True

def update_roles():
	global __roles_by_slug, __roles_needs_update

	if __roles_needs_update:
		_roles = NaginieStatus.query.filter().all()
		__roles_by_slug = {}
		for _role in _roles:
			__roles_by_slug[_role.slug] = _role

		#__roles_needs_update = False

def check_roles( user, roles):
	global __roles_by_slug, __roles_needs_update

	if len(roles) == 0 and user:
		return True
	else:
		for role in roles:
			if role not in __roles_by_slug:
				print('*** Warning: checking vs an unknown role: %s.' % role)
				continue

			if __roles_by_slug[role] in user.roles:
				return True
		return False
"""

def role_required(roles=[]):
	def decorator(f):
		@wraps(f)
		def decorated_function(*args, **kwargs):
			auth_headers = request.headers.get('Authorization', '').split()

			if len(auth_headers) != 2:
				return jsonify(auth_invalid_msg), 401
			try:
				token = auth_headers[1]
				data = jwt.decode(token, current_app.config['SECRET_KEY'])
				user = NaginieUser.query.filter(NaginieUser.id==data['user']['id']).first()

				if not user:
					raise RuntimeError('User not found')

				if not user.status.role in roles:
					return jsonify(auth_invalid_role), 403
				return f(user, *args, **kwargs)
			except jwt.ExpiredSignatureError:
				return jsonify(auth_expired_msg), 401 # 401 is Unauthorized HTTP status code
			except jwt.InvalidTokenError:
				return jsonify(auth_invalid_msg), 401

		return decorated_function
	return decorator
