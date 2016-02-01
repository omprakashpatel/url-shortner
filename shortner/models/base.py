from shortner import app

from mongoengine import *

# Mongo DB instance
connect("url_shortner", host="127.0.0.1", port=27017)
# connect(app.config['MONGODB_SETTINGS'])

class UrlShortner(Document):
	""" docstring for UrlShortner """
	id = IntField(primary_key=True, required=True)
	long_url = StringField(required=True, max_length=2048, unique=True)
	short_url = StringField(unique=True)
	title = StringField()
	hits = IntField(default=0)

	meta = {
		'indexes': [
			{'fields': ['$long_url', '$title'],
			'default_language': 'english'}
		]
	}

	# meta = {
	# 	'indexes': [
	# 		{'fields': ['$long_url', '$title'],
	# 		'default_language': 'english',
	# 		'weights': {'long_url': 10, 'title': 2}}
	# 	]
	# }
