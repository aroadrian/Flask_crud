from flask import Flask, jsonify
from init_db import db_connection
import psycopg2

app = Flask(__name__)

db_connection()

# Database connection
def db_conn():
 
        conn = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="admin"  
        )
        return conn
db_conn()
   
@app.route("/books", methods=["GET"])
def get_book():
    try:    
        conn = db_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books")
        rows = cursor.fetchall()
        
        books = []
        for row in rows:
            book = {
                'id': row[0],
                'title': row[1],
                'author': row[2],
                'page_num': row[3],
                'review': row[4],
                'date_added': row[5]
            }
            books.append(book)
    
    
    except Exception as e:
        # Handle any exceptions (e.g., connection issues, query errors)
        return jsonify({'error': str(e)}), 50
print(app.url_map) 
if __name__ == "__main__":
    app.run(debug=True)
   