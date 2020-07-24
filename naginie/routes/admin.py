from flask import Blueprint, render_template, send_from_directory

import os

root = os.path.dirname(__file__)


bp = Blueprint(
	'admin', __name__, 
	static_folder=os.path.join('../../naginie_themes', 'admin', 'static'),
	static_url_path='/static/admin'
)

@bp.route('/admin')
@bp.route('/admin/')
def home():
	print(os.path.join('../../naginie_themes', 'admin', 'static'))
	return render_template(
		'admin/index.html'
	)
