from shortner.models.base import UrlShortner
from shortner import app
from utils import id_to_string, string_to_id, generate_id

def url_shortner(url, **kwargs):
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
	short_url = "{}{}".format(app.config['DOMAIN'], short_id)
	try:
		_us = UrlShortner.objects.get(short_url=short_url)
	except Exception, e:
		raise e
	return _us.long_url