from flask import Blueprint, jsonify, current_app, request
from functools import wraps
import jwt
import os
import datetime

from ..naginie import db
from ..models.naginie_user import NaginieUser, NaginieRole, NaginieStatus, role_required

root = os.path.dirname(__file__)

#: Serve vue app static
bp = Blueprint(
	'api', __name__, url_prefix='/api'
)

### Login ###
@bp.route('/login/', methods=('POST',))
def login():
	data = request.get_json()
	user = NaginieUser.authenticate(**data)

	if not user:
		return jsonify({ 'message': 'Invalid credentials', 'authenticated': False }), 401

	token = jwt.encode({
		'user': user._to_dict(True),
		'iat': datetime.datetime.utcnow(),
		'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=480)
		},
		current_app.config['SECRET_KEY']
	)
	return jsonify({ 'token': token.decode('UTF-8') })


### Users List ###
@bp.route('/users/')
@role_required([NaginieRole.administrator])
def users(user):
	page = request.args.get('page', 1)
	page = int(page)
	users = NaginieUser.query.filter().order_by(NaginieUser.id.desc()).paginate(page, per_page=12)

	result = {
		"items": [],
		"pages": users.pages,
		"page": page,
		"prev": users.prev_num,
		"next": users.next_num,
		"has_next": users.has_next,
		"has_prev": users.has_prev,
	}

	for _user in users.items:
		result["items"].append(_user._to_dict(True))

	return jsonify(result)

### Users Search ###
@bp.route('/users/search/')
@role_required([NaginieRole.administrator])
def users_search(user):
	page = request.args.get('page', 1)
	page = int(page)
	term = request.args.get('term', False)

	if not term:
		return jsonify(empty_list)


	users = NaginieUser.query.filter(
		NaginieUser.email.ilike("%" + term + "%")
		| NaginieUser.firstname.ilike("%" + term + "%")
		| NaginieUser.lastname.ilike("%" + term + "%")
		| NaginieUser.username.ilike("%" + term + "%")
	).order_by(NaginieUser.id.desc()).paginate(page, per_page=12)

	result = {
		"items": [],
		"pages": users.pages,
		"page": page,
		"prev": users.prev_num,
		"next": users.next_num,
		"has_next": users.has_next,
		"has_prev": users.has_prev,
	}

	for _user in users.items:
		result["items"].append(_user._to_dict(True))

	return jsonify(result)

### User profile ###
### Users Search ###
@bp.route('/users/<int:id>')
@role_required([NaginieRole.administrator])
def users_profile(user, id):
	cuser = NaginieUser.query.filter(NaginieUser.id==id).first()
	if cuser:
		return jsonify(cuser._to_dict(True))
	return jsonify({'error': 404}), 404

### User password change ###
@bp.route('/users/pwd/<int:id>', methods=('POST',))
@role_required([NaginieRole.administrator])
def users_password(user, id):
	cuser = NaginieUser.query.filter(NaginieUser.id==id).first()
	data = request.get_json()
	pwd = data.get('password', '')
	check_pwd = NaginieUser.check_password_format(pwd)

	if check_pwd is True:
		if cuser:
			cuser.password = pwd
			cuser.updated = datetime.datetime.now()
			db.session.add(cuser)
			db.session.commit()
			return jsonify({'message': 'success'})
		return jsonify({'error': 404}), 404
	else:
		return jsonify({'error': check_pwd})

### User account change ###
@bp.route('/users/data/<int:id>', methods=('POST',))
@role_required([NaginieRole.administrator])
def users_data(user, id):
	cuser = NaginieUser.query.filter(NaginieUser.id==id).first()
	data = request.get_json()
	email = data.get('email', '')
	firstname = data.get('firstname', '')
	lastname = data.get('lastname', '')
	username = data.get('username', '')

	check_email = NaginieUser.check_email_format(email)

	if check_email is True or email == cuser.email:
		if cuser:
			cuser.email = email
			cuser.firstname = firstname
			cuser.lastname = lastname
			cuser.username = username
			cuser.updated = datetime.datetime.now()
			db.session.add(cuser)
			db.session.commit()
			return jsonify({'message': 'success'})
		return jsonify({'error': 404}), 404
	else:
		return jsonify({'error': check_email})

### Roles ###
@bp.route('/users/roles')
@role_required([NaginieRole.administrator])
def users_roles(user,):
	status = NaginieStatus.query.filter().order_by(NaginieStatus.id.asc()).all()
	result = []
	for _s in status:
		result.append(_s._to_dict())
	return jsonify(result)