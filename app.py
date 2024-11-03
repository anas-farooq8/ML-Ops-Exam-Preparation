from flask import Flask, render_template
import mysql.connector
import os

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv('MYSQL_HOST', 'mysql-service'),  # service name defined in the MySQL service YAML
        user=os.getenv('MYSQL_USER', 'testuser'),
        password=os.getenv('MYSQL_PASSWORD', 'testpass'),
        database=os.getenv('MYSQL_DATABASE', 'testdb')
    )

@app.route('/', methods=['GET'])
def get_cars():
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM car")
        rows = cursor.fetchall()
        cursor.close()
        connection.close()
        return render_template('cars.html', cars=rows)
    except mysql.connector.Error as err:
        # Log error details for debugging (optional)
        print(f"Database error: {err}")
        # Render a custom error page with a friendly message
        return render_template('error.html', error_message="Unable to connect to the database. Please try again later.")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
