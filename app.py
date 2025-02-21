from flask import Flask, request, jsonify
from init_db import db_connection
import psycopg2

app = Flask(__name__)

#para matawag pala yung function na db_connect sa init_db.py
db_connection()


#Database connection
def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="admin"  )
    return conn


get_db_connection()

#SELECT all data from the database

@app.route('/', methods=['GET'])
def get_book():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM books;')
    books = cur.fetchall()
    cur.close()
    conn.close()
    return books

@app.route("/books", methods=['POST'])
def post_book():
    # Check if request contains JSON
    if request.is_json:
        book = request.get_json()  # Parse the incoming JSON data
        title = book.get('title')
        author = book.get('author')
        pages_num = book.get('pages_num')
        review = book.get('review')

        # Validate if all necessary fields are provided
        if not title or not author or not pages_num or not review:
            return jsonify({"error": "Missing required fields"}), 400
        
        # Insert the new book into the database
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            'INSERT INTO books (title, author, pages_num, review) '
            'VALUES (%s, %s, %s, %s)',
            (title, author, pages_num, review)
        )
        conn.commit()
        cur.close()
        conn.close()
        
        # Return success message as JSON
        return jsonify({"message": "Book added successfully"}), 201
    else:
        return jsonify({"error": "Invalid JSON format"}), 400

if __name__ == "__main__":
    app.run(debug=True)
   

#error here cant understand
# @app.route("/books/", methods=('POST'))
# def post_book():
#     if request.method == 'POST':
#         book = request.get_json()
#         title = book['title']
#         author = book['author'] 
#         pages_num = book['pages_num']
#         review = book['review']
        

#         conn = get_db_connection()
#         cur = conn.cursor()
#         cur.execute('INSERT INTO books (title, author, pages_num, review)'
#                     'VALUES (%s, %s, %s, %s)',
#                     (title, author, pages_num, review))
#         conn.commit()
#         cur.close()
#         conn.close()
