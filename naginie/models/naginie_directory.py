from sqlalchemy_mptt.mixins import BaseNestedSets
import datetime

from naginie.extensions import db
from naginie.database import CRUDMixin

class NaginieDirectory(db.Model, BaseNestedSets, CRUDMixin):
	__tablename__ = 'naginie_directory'

	id	= db.Column(db.Integer, primary_key = True)
	created = db.Column(db.DateTime(), default=datetime.datetime.now)
	updated = db.Column(db.DateTime(), default=datetime.datetime.now)
	slug = db.Column(db.String(128), unique=True)
	title = db.Column(db.String(96))
	description = db.Column(db.String(160))
	is_blog = db.Column(db.Boolean, default=False)
	is_public = db.Column(db.Boolean, default=False)

	def __repr__(self):
		return '<NaginieDirectory id="%s" title="%s">' % (self.id, self.title)

	def __unicode__(self):
		return '%s' % self.title

	def _to_dict(self):
		return NaginieDirectory.to_dict(self)

	@staticmethod
	def to_dict(n_directory):
		return {
			'id': n_directory.id,
			'parent_id': n_directory.parent_id,
			'created': n_directory.created.isoformat(),
			'updated': n_directory.updated.isoformat(),
			'slug': n_directory.slug,
			'title': n_directory.title,
			'description': n_directory.description,
			'is_blog': n_directory.is_blog
		}