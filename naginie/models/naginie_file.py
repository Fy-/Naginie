import datetime

from ..naginie import db

class NaginieFile(db.Model):
	__tablename__ = 'naginie_file'

	id	= db.Column(db.Integer, primary_key = True)
	created = db.Column(db.DateTime(), default=datetime.datetime.now)
	updated = db.Column(db.DateTime(), default=datetime.datetime.now)
	slug = db.Column(db.String(128), unique=True)
	title = db.Column(db.String(96))
	description = db.Column(db.String(160))
	content = db.Column(db.Text())
	is_md = db.Column(db.Boolean, default=False)

	def __repr__(self):
		return '<NaginieFile id="%s" title="%s">' % (self.id, self.title)

	def __unicode__(self):
		return '%s' % self.title
		
	def to_dict(self):
		return NaginieFile.to_dict(self)

	@staticmethod
	def to_dict(n_file, content=True):
		return {
			'id': n_file.id,
			'created': n_file.created.isoformat(),
			'updated': n_file.updated.isoformat(),
			'slug': n_file.slug,
			'title': n_file.title,
			'description': n_file.description,
			'content': n_file.content if content else None
		}