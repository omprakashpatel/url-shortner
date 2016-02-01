from shortner.models.base import UrlShortner
from shortner import app
from utils import id_to_string, string_to_id, generate_id
import requests
from bs4 import BeautifulSoup

# ==============================
import thread
def get_page_title(id, url):
	print " ********************* thread Started ******************************"
	try:
		r = requests.get(url)
		if r.status_code == 200:
			soup = BeautifulSoup(r.text, "html.parser")
			title = soup.title.string

			# update in db
			_us = UrlShortner.objects.get(id=id)
			_us.title = title
			_us.save()
	except Exception, e:
		print str(e)
		raise e

	print " ********************* thread Finishied ****************************"

# ==============================

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
		# task to get url title and store back to DB
		thread.start_new_thread(get_page_title, (id, url))

	print "--------- Existing Handler ----------------------"
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


def get_url_desc(short_id, **kwargs):
	"""
	"""
	id = string_to_id(short_id)
	try:
		_us = UrlShortner.objects.get(id=id)
	except Exception, e:
		raise e

	return {'id': _us.id, 'short_url': _us.short_url, 'long_url': _us.long_url,
			'hits': _us.hits, 'title': _us.title}


def search_url(word, **kwargs):
	if isinstance(word, list):
		word = word[0]

	_us_obj = UrlShortner.objects.search_text(word)

	ret = []
	for _us in _us_obj:
		ret.append({ 'id': _us.id, 'short_url': _us.short_url,
	 				'long_url': _us.long_url, 'hits': _us.hits,
	 				'title': _us.title})
	return ret
