from flask import *
from flask.ext.sqlalchemy import SQLAlchemy
from flaskext.yamlconfig import AppYAMLConfig

from os import path
import yaml
from config import *

def load_yaml(app, filename):
    filename = path.join(app.root_path, filename)
    with open(filename) as f:
        obj = yaml.load(f)
    return app.config.from_object(obj)

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

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/add', methods=['POST'])
def add():
	return "poop"

@app.route('/get')
def get():
	return "list of the things"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10050, debug=True)
