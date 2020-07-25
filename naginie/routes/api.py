from flask import Blueprint, jsonify, current_app, request
from functools import wraps
import jwt
import os
import datetime
from ..models.naginie_user import NaginieUser, NaginieRole, RoleRequired

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
@RoleRequired(['administrator'])
def users(user):
	page = 1
	users = NaginieUser.query.filter().order_by(NaginieUser.id.desc()).paginate(page, per_page=15)

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