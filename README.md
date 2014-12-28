## remote

remote is a small plugin-ish app that lets you visually represent where your remote team members are located throughout the world. This is done using the Google Maps API. 

### Requirements

* Python2
* MySQL Server
* Flask
* Flask-SQLAlchemy

### Installation

1. Install the requirements.
2. Create a database for remote, add a user with all privileges for said database. 
3. Copy config.py.example to config.py in the directory you'll be running remote from.
3. Start remote - you can use the built in Flask server if you like using `python remote.py` however this isn't recommended. 

### Use

Visit the IP or URL you set remote to listen on. Make a new marker by filling out the small form, include a name so you know who owns each pin. 

