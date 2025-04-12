import mysql.connector
import os

def get_connection():
    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "localhost"),
        user=os.getenv("MYSQL_USER", "root"),
        password=os.getenv("MYSQL_PASSWORD", ""),
        database=os.getenv("MYSQL_DATABASE", "testdb")
    )


# db.py

def create_user(username, email):  # keep argument name as-is
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (username, email))
    conn.commit()
    cursor.close()
    conn.close()

def get_users():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, email FROM users")
    users = [{"id": row[0], "username": row[1], "email": row[2]} for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return users

