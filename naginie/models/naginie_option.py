import datetime

from ..naginie import db
from .crud import CRUDMixin

class NaginieOption(db.Model, CRUDMixin):
	__tablename__ = 'naginie_option'

	key	= db.Column(db.String(64), primary_key = True)
	value = db.Column(db.String(128))

	created = db.Column(db.DateTime(), default=datetime.datetime.now)
	updated = db.Column(db.DateTime(), default=datetime.datetime.now)

	def __repr__(self):
		return '<NaginieOption key="%s" value="%s">' % (self.key, self.value)

	@staticmethod
	def set(key, value):
		foption = NaginieOption.query.filter(NaginieOption.key==key).first()
		if foption:
			foption.value = value
			foption.updated = datetime.datetime.now()

		foption = NaginieOption(key=key, value=value)
		db.session.add(foption)
		db.session.commit()

	@staticmethod
	def rm(key):
		foption = NaginieOption.query.filter(NaginieOption.key==key).first()
		if foption:
			db.session.delete(foption)
			db.session.commmit()