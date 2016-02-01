from shortner import app
from flask import request, jsonify, redirect
from handlers import *

@app.route('/')
def hello():
	return "Hello World!"

@app.route('/shortner', methods=['POST'])
def url_shortner_api():
	return jsonify(status="success", data=url_shortner(
		**(request.json or request.form or {})))

@app.route('/<short_id>', methods=['GET'])
def url_shortner_redirect_api(short_id):
	data = get_long_url(short_id)
	return redirect(data)

@app.route('/<short_id>/desc', methods=['GET'])
def ur_descriptions(short_id):
	data = get_url_desc(short_id)
	return jsonify(status="success", data=data)

@app.route('/search', methods=['GET'])
def search_url_api():
	return jsonify(status="success",
		data=search_url(**(request.args or {} )))

@app.errorhandler(404)
def page_not_found(error):
	return "<div><h2>Page Not Found </h2></div>", 404

@app.errorhandler(Exception)
def exception_handler(error):
    print "**************************"
    print str(error)
    print "**************************"
    return str(error)
