from shortner import app
from flask import request, jsonify, redirect
from handlers import url_shortner, get_long_url

@app.route('/')
def hello():
	return "Hello Worlds"


@app.route('/shortner', methods=['POST'])
def url_shortner_api():
	return jsonify(status="success", data=url_shortner(**(request.json or {})))

@app.route('/<short_id>', methods=['GET'])
def url_shortner_redirect_api(short_id):
	data = get_long_url(short_id)
	return redirect(data)
