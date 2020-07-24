from flask import Blueprint, render_template, send_from_directory

import os

root = os.path.dirname(__file__)


bp = Blueprint(
	'admin', __name__, 
	static_folder=os.path.join('../../naginie_adm', 'admin', 'dist'),
	static_url_path='/'
)

@bp.route('/admin')
@bp.route('/admin/')
def home():
	print(os.path.join(root, '../../naginie_adm', 'admin', 'dist', 'static'))
	return send_from_directory(os.path.join(root, '../../naginie_adm', 'admin', 'dist'), 'index.html')

