
# ============================================
# Library Book Usage & Reading Pattern Analysis
# app.py - Flask Web Application
# ============================================

from flask import Flask, render_template, redirect, url_for, request, session
from analysis import generate_all_charts, load_data, get_stats
import os

app = Flask(__name__)
app.secret_key = 'library_secret_key_2024'

# ── Home / Dashboard ─────────────────────────
@app.route('/')
def index():
    if 'logged_in' not in session:
        return redirect(url_for('login'))
    df    = load_data()
    stats = get_stats(df)
    generate_all_charts()
    return render_template('index.html', stats=stats)

# ── Login ─────────────────────────────────────
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'admin' and password == 'admin123':
            session['logged_in'] = True
            session['username']  = username
            return redirect(url_for('index'))
        else:
            error = 'Invalid username or password!'
    return render_template('login.html', error=error)

# ── Logout ────────────────────────────────────
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

# ── Analysis Page ────────────────────────────
@app.route('/analysis')
def analysis():
    if 'logged_in' not in session:
        return redirect(url_for('login'))
    df    = load_data()
    stats = get_stats(df)
    # Top 5 books
    top_books = df['book_title'].value_counts().head(5).to_dict()
    # Dept counts
    dept_data = df['department'].value_counts().to_dict()
    return render_template('analysis.html', stats=stats,
                           top_books=top_books, dept_data=dept_data)

# ── Records Page ─────────────────────────────
@app.route('/records')
def records():
    if 'logged_in' not in session:
        return redirect(url_for('login'))
    df      = load_data()
    records = df[['record_id','student_name','department',
                  'book_title','genre','borrow_date',
                  'return_date','hold_days','status']].head(30).to_dict('records')
    return render_template('records.html', records=records)

if __name__ == '__main__':
    port = int(os.environ.get("PORT",5000))
    app.run(host="0.0.0.0.",port=port)
