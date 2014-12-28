from flask import *
from flask.ext.sqlalchemy import SQLAlchemy

from os import path
from config import *

app = Flask(__name__)

connectionString = "mysql+mysqlconnector://%s:%s@%s:3306/%s" % (username, password, hostname, database)
app.config['SQLALCHEMY_DATABASE_URI'] = connectionString
db = SQLAlchemy(app)

class Record(db.Model):
	__tablename__ = "record"

	id = db.Column(db.Integer, primary_key=True)
	longitude = db.Column(db.Text)
	latitude = db.Column(db.Text)
	name = db.Column(db.String(50))

	def __init__(self, longitude, latitude, name):
		self.longitude = longitude
		self.latitude = latitude
		self.name = name

db.create_all()
db.session.commit()

@app.route('/')
def index():
	number = Record.query.all()
	reporting = len(number)
	return render_template("index.html", reporting=reporting)

@app.route('/add', methods=['POST'])
def add():
	new = Record(request.form['longitude'], request.form['latitude'], request.form['name'])
	db.session.add(new)
	db.session.commit()
	return "202 - OK"

@app.route('/get')
def get():
	records = Record.query.all() 
	data = []
	for record in records:
		d = {
			'id' : record.id,
			'name': record.name,
			'longitude' : record.longitude,
			'latitude' : record.latitude
		}
		data.append(d)
	return jsonify(records=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10050, debug=True)
