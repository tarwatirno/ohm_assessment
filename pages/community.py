from flask import jsonify, render_template, request, Response
from flask.ext.login import current_user, login_user

from flask_table import Table, Col

from functions import app
from models import User

class CommunityTable(Table):
    table_id = "community-table"
    display_name = Col("Name")
    tier = Col("Tier")
    point_balance = Col("Point Balance")

@app.route('/community', methods=['GET'])
def community():
    login_user(User.query.get(1))
    table = CommunityTable(User.query.all())
    return render_template("community.html", table=table)
