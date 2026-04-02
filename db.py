import sqlite3

def connect_db():
    return sqlite3.connect("app.db", check_same_thread=False)

conn = connect_db()
cursor = conn.cursor()

# Create tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    username TEXT,
    password TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS history (
    username TEXT,
    text TEXT,
    result TEXT,
    confidence REAL
)
""")

conn.commit()


# Add user
def add_user(username, password):
    cursor.execute("INSERT INTO users VALUES (?,?)", (username, password))
    conn.commit()


# Check user
def login_user(username, password):
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    return cursor.fetchone()


# Save history
def save_history(username, text, result, confidence):
    cursor.execute("INSERT INTO history VALUES (?,?,?,?)", (username, text, result, confidence))
    conn.commit()


# Get history
def get_history(username):
    cursor.execute("SELECT * FROM history WHERE username=?", (username,))
    return cursor.fetchall()