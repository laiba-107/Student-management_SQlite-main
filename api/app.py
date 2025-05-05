from flask import Flask, render_template, request, jsonify, redirect, url_for, session, flash
from flask_cors import CORS
from db import get_db_connection, initialize_database
from auth import auth_bp
from api.router import api_bp
import os
from config import Config

app = Flask(__name__, static_folder='static', template_folder='templates')
app.config.from_object(Config)
CORS(app)

# Register Blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(api_bp, url_prefix='/api')

# Initialize database
@app.before_first_request
def init_db():
    initialize_database()

# Main Dashboard Route
@app.route('/')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    return render_template('dashboard.html')

# Other main routes
@app.route('/students')
def students():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    return render_template('students.html')

@app.route('/courses')
def courses():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    return render_template('courses.html')

@app.route('/departments')
def departments():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    return render_template('departments.html')

@app.route('/instructors')
def instructors():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    return render_template('instructors.html')

@app.route('/enrollments')
def enrollments():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    return render_template('enrollments.html')

@app.route('/analytics')
def analytics():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    return render_template('analytics.html')

if __name__ == '__main__':
    app.run(debug=True)