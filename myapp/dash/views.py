from flask import render_template
from . import dash


@dash.route('/dash')
def dash():
	return render_template('dash.html')

