from shortner import app

from mongoengine import *

# Mongo DB instance
connect("url_shortner", host="127.0.0.1", port=27017)
# connect(app.config['MONGODB_SETTINGS'])

class UrlShortner(Document):
	""" docstring for UrlShortner """
	id = IntField(primary_key=True, required=True)
	long_url = StringField(required=True, max_length=1000, unique=True)
	short_url = StringField(unique=True)
	hits = IntField(default=0)
