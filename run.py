from shortner import app, urls

if __name__ == "__main__":
	print("Starting Server..")
	app.debug = True
	app.run(host=app.config['HOST'], port=app.config['PORT'])