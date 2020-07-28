from flask import Blueprint, jsonify, current_app, request
from functools import wraps
import jwt
import os
import datetime

from naginie.extensions import db
from naginie.models import NaginieRole, role_required, NaginieDirectory
                                                                
root = os.path.dirname(__file__)

bp = Blueprint(
	'api_directory', __name__, url_prefix='/api'
)

@bp.route('/directories/list', methods=('GET',))
@role_required([NaginieRole.administrator])
def directory_list(user):
	directories = NaginieDirectory.query.all()
	result = []
	for directory in directories:
		result.append(directory.drilldown_tree(json=True, json_fields=NaginieDirectory.to_dict)[0])
	return jsonify(result)

@bp.route('/directories/del/<int:id>', methods=('GET',))
@role_required([NaginieRole.administrator])
def directory_del(user):
	pass

@bp.route('/directories/edit/<int:id>', methods=('POST',))
@role_required([NaginieRole.administrator])
def directory_edit(user):
	pass

@bp.route('/directories/add', methods=('POST',))
@role_required([NaginieRole.administrator])
def directory_add(user):
	pass
