from flask import Blueprint, render_template, send_from_directory, jsonify, current_app, request

import os
import jwt
import datetime

from naginie.models.naginie_user import NaginieUser

root = os.path.dirname(__file__)

#: Serve vue app static
bp = Blueprint(
	'admin', __name__, 
	static_folder=os.path.join('../../naginie_admin', 'dist'),
	static_url_path='/'
)

#: Serve vue app
@bp.route('/admin')
@bp.route('/admin/')
def home():
	return send_from_directory(os.path.join(root, '../../naginie_admin', 'dist'), 'index.html')



