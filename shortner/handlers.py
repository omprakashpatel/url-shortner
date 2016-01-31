from shortner.models.base import UrlShortner
from shortner import app
from utils import id_to_string, string_to_id, generate_id

def url_shortner(url, **kwargs):
	"""
		Fun will generate short url and store in the DB
		and will return short_url

		url: Input URL to Short
	"""
	if isinstance(url, list):
		url = url[0]
	_us = None
	try:
		_us = UrlShortner.objects.get(long_url=url)
	except Exception, e:
		print(str(e))
		pass

	if not _us:
		id = generate_id()
		short_url = "{}{}".format(app.config['DOMAIN'], id_to_string(id))
		try:
			_us = UrlShortner(id=id, short_url=short_url, long_url=url)
			_us.save()
		except Exception, e:
			raise e

	return _us.short_url

def get_long_url(short_id, **kwargs):
	"""
		map short url to long_url with help of DB
		and redirct to Original long_url page
	"""
	id = string_to_id(short_id)
	try:
		_us = UrlShortner.objects.get(id=id)
		_us.hits += 1
		_us.save()
	except Exception, e:
		raise e
	return _us.long_url

def get_long_url_2(short_id, **kwargs):
	"""
		DOC
	"""
	short_url = "{}{}".format(app.config['DOMAIN'], short_id)
	try:
		_us = UrlShortner.objects.get(short_url=short_url)
		_us.hits += 1
		_us.save()
	except Exception, e:
		raise e
	return _us.long_url

