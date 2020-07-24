import os
from flask import Blueprint, render_template

from ..helpers.template import tpl_dir, get_tpl_name

bp = Blueprint(
	"default", __name__,
	static_folder=os.path.join('../../naginie_themes', get_tpl_name(), 'static'),
	static_url_path='/static/default'
)

@bp.route('/')
def home():
	print(os.path.join('../../naginie_themes', get_tpl_name(), 'static'))
	return render_template(
		tpl_dir('index.html')
	)