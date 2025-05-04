from flask import Blueprint, request, redirect, url_for, session, flash, render_template
from werkzeug.security import check_password_hash, generate_password_hash
from db import get_db_connection
from functools import wraps

auth_bp = Blueprint('auth', __name__)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('auth.login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM User WHERE username = ?", (username,))
            user = cursor.fetchone()
            
            if user and check_password_hash(user['password_hash'], password):
                session['user_id'] = user['user_id']
                session['username'] = user['username']
                session['role'] = user['role']
                flash('Login successful!', 'success')
                next_page = request.args.get('next') or url_for('dashboard'))
                return redirect(next_page)
            else:
                flash('Invalid username or password', 'danger')
    
    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('auth.login'))

@auth_bp.route('/change-password', methods=['POST'])
@login_required
def change_password():
    old_password = request.form['old_password']
    new_password = request.form['new_password']
    
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT password_hash FROM User WHERE user_id = ?", (session['user_id'],))
        user = cursor.fetchone()
        
        if user and check_password_hash(user['password_hash'], old_password):
            cursor.execute(
                "UPDATE User SET password_hash = ? WHERE user_id = ?",
                (generate_password_hash(new_password), session['user_id'])
            )
            conn.commit()
            flash('Password changed successfully!', 'success')
        else:
            flash('Old password is incorrect', 'danger')
    
    return redirect(url_for('dashboard'))