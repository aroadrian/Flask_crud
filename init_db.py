import os
import psycopg2

# Database connection
def db_connection():
        conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="admin"  
        
        )
        conn.close
        #cur = conn.cursor()
        
        # Delete table if exists
        #cur.execute('DROP TABLE IF EXISTS books;')

        # Create table
        #cur.execute('CREATE TABLE books (id SERIAL PRIMARY KEY,'
        #            'title VARCHAR(150) NOT NULL,'
         #           'author VARCHAR(50) NOT NULL,'
        #            'pages_num integer NOT NULL,'
         #           'review text,'
         #           'date_added date DEFAULT CURRENT_TIMESTAMP);'
         #           )
        
    # Insert data
        #cur.execute('INSERT INTO books (title, author, pages_num, review) VALUES (%s, %s, %s, %s)',
         #   ('The Catcher in the Rye', 'J.D. Salinger', 277, 'A great book!'))
        
        #conn.commit()
        #cur.close()
        #conn.close()