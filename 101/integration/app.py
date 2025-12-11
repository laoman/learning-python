from flask import Flask, render_template, request, redirect, url_for
import os
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)
# It is recommended to load the secret key from an environment variable
# and avoid hardcoding it.
app.secret_key = os.environ.get('SECRET_KEY', 'a-secure-random-string-for-development')

def get_db_connection():
		"""Utility function to create a database connection."""
		try:
				conn = mysql.connector.connect(
						host=os.environ.get('DB_HOST'),
						database=os.environ.get('DB_NAME'),
						user=os.environ.get('DB_USER'),
						password=os.environ.get('DB_PASSWORD')
				)
				if conn.is_connected():
						return conn
		except Error as e:
				print(f"Error connecting to MySQL: {e}")
				return None

@app.route('/')
def index():
		"""Main page with input form, database table creation, and message display."""
		messages = []
		conn = get_db_connection()
		if conn:
				try:
						cursor = conn.cursor(dictionary=True)
						# Ensure the table exists with the new columns
						cursor.execute("""
								CREATE TABLE IF NOT EXISTS visitors (
										id INT AUTO_INCREMENT PRIMARY KEY,
										name VARCHAR(255) NOT NULL,
										message TEXT NOT NULL,
										visit_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
								)
						""")
						# Fetch all existing messages to display
						cursor.execute("SELECT name, message, visit_time FROM visitors ORDER BY visit_time DESC")
						messages = cursor.fetchall()
				except Error as e:
						print(f"Database error: {e}")
				finally:
						if conn.is_connected():
								cursor.close()
								conn.close()
		
		return render_template('index.html', messages=messages)

@app.route('/add', methods=['POST'])
def add_message():
		print(1)
		"""Handles form submission and inserts a new message into the database."""
		visitor_name = request.form.get('visitor_name')
		visitor_message = request.form.get('visitor_message')

		if visitor_name and visitor_message:
				print(2)
				conn = get_db_connection()
				if conn:
						try:
								print(3)
								cursor = conn.cursor()
								# Use a parameterized query to prevent SQL injection
								sql = "INSERT INTO visitors (name, message) VALUES (%s, %s)"
								val = (visitor_name, visitor_message)
								cursor.execute(sql, val)
								conn.commit()
						except Error as e:
								print(f"Database error on insert: {e}")
						finally:
								if conn.is_connected():
										cursor.close()
										conn.close()
		
		return redirect(url_for('index'))

if __name__ == '__main__':
		# Get port from environment variable, default to 8000
		port = int(os.environ.get('FLASK_RUN_PORT', 8000))
		host = os.environ.get('FLASK_RUN_HOST', '0.0.0.0')
		debug = os.environ.get('FLASK_DEBUG', 'True').lower() == 'true'

		app.run(debug=debug, host=host, port=port)
