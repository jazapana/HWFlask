from app import db

class City(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	city_name = db.Column(db.String(64), index=True, unique=True)
	city_rank = db.Column(db.Integer(), index=True, unique=True)
	is_visited = db.Column(db.Boolean)

	def __repr__(self):
		return f'{self.city_name}'
