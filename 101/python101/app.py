from flask import Flask, render_template
import os

app = Flask(__name__)
# It is recommended to load the secret key from an environment variable
# and avoid hardcoding it.
app.secret_key = os.environ.get('SECRET_KEY', 'a-secure-random-string-for-development')

@app.route('/')
def index():
	"""Main page with input form"""
	# This route requires a 'templates/index.html' file to exist.
	return render_template('index.html')

if __name__ == '__main__':
	# Get port from environment variable, default to 8000
	port = int(os.environ.get('FLASK_RUN_PORT', 8000))
	host = os.environ.get('FLASK_RUN_HOST', '0.0.0.0')
	debug = os.environ.get('FLASK_DEBUG', 'True').lower() == 'true'

	app.run(debug=debug, host=host, port=port)
