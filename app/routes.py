from app import my_obj, db
from flask import render_template, flash, redirect
from app.forms import TopCities
from app.models import City

@my_obj.route('/', methods=['GET', 'POST'])
def home():
	form = TopCities()
	if form.validate_on_submit():
		flash(f'Added City: {form.city_name.data}, visited = {form.is_visited.data}')
		city = City(city_name = form.city_name.data, city_rank = form.city_rank.data, is_visited = form.is_visited.data)
		db.session.add(city)
		db.session.commit()
		return redirect('/')
	top_cities = City.query.order_by(City.city_rank).all()
	return render_template('home.html', title='Top Cities', name='Joel', top_cities=top_cities, form=form)
