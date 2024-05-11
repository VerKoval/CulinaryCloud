from flask import render_template
from app import app  # Import the Flask app instance

@app.route('/view_menu')  # Adjust the route to remove extra spaces
def view_menu():
    return render_template('view_menu.html')  # Assuming you have a view_menu.html template

