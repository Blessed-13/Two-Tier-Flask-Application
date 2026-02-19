import os
import time
import mysql.connector
from flask import Flask

app = Flask(__name__)

# Read DB credentials from environment variables
DB_HOST = os.getenv('DB_HOST', 'db')
DB_USER = os.getenv('DB_USER', 'root')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'password')
DB_NAME = os.getenv('DB_NAME', 'test_db')

def get_db_connection():
    # Retry logic: Wait for MySQL to be ready
    for i in range(10):
        try:
            conn = mysql.connector.connect(
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASSWORD,
                database=DB_NAME
            )
            return conn
        except mysql.connector.Error:
            time.sleep(2)
    return None

@app.route('/')
def index():
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        # Create table if not exists
        cursor.execute("CREATE TABLE IF NOT EXISTS logs (id INT AUTO_INCREMENT PRIMARY KEY, info VARCHAR(255))")
        # Insert test row
        cursor.execute("INSERT INTO logs (info) VALUES ('Connection test successful')")
        conn.commit()
        
        cursor.close()
        conn.close()
        return "Database connected successfully"
    else:
        return "Database connection failed", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
