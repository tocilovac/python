import sqlite3

# Connect to a database file (or create it)
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Execute SQL command via Python
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

# Save changes and close connection
conn.commit()
conn.close()
