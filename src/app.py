from flask import Flask, render_template
import os

# Set the absolute path to the project root
project_root = os.path.dirname(os.path.abspath(__file__))

# Set the absolute paths to the static and templates folders
static_dir = os.path.join(project_root, '..', 'static')
template_dir = os.path.join(project_root, '..', 'templates')

app = Flask(__name__, static_folder=static_dir, template_folder=template_dir)

@app.route('/')
def home():
    return render_template('front_page.html')

if __name__ == '__main__':
    app.run(debug=True, port=5002)  # Run on port 5002
