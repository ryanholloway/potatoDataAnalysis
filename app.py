from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

app = Flask(__name__)
auth = HTTPBasicAuth()

users={
    "admin": generate_password_hash("MonikaNusi16")
}

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username), password):
        return username

def init_db():
    conn = sqlite3.connect('potato_data.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS potato_plants (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            plant_id TEXT,
            disease_type TEXT,
            test_result TEXT,
            field_location TEXT,
            date_logged TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_entry', methods=['POST'])
def add_entry():
    data = request.json
    plant_id = data['plant_id']
    disease_type = data['disease_type']
    test_result = data['test_result']
    field_location = data['field_location']
    date_logged = data['date_logged']
    
    conn = sqlite3.connect('potato_data.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO potato_plants (plant_id, disease_type, test_result, field_location, date_logged)
        VALUES (?, ?, ?, ?, ?)
    ''', (plant_id, disease_type, test_result, field_location, date_logged))
    conn.commit()
    conn.close()
    
    return jsonify({'status': 'success'})

@app.route('/get_entries', methods=['GET'])
def get_entries():
    conn = sqlite3.connect('potato_data.db')
    c = conn.cursor()
    c.execute('SELECT * FROM potato_plants')
    rows = c.fetchall()
    conn.close()
    
    return jsonify(rows)

@app.route('/admin')
@auth.login_required
def admin():
    conn = sqlite3.connect('potato_data.db')
    c = conn.cursor()
    c.execute('SELECT * FROM potato_plants')
    rows = c.fetchall()
    conn.close()
    
    return render_template('admin.html', data=rows)

if __name__ == '__main__':
    app.run(debug=True)
