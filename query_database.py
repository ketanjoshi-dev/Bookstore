import mysql.connector

# Establish a connection to the database
db = mysql.connector.connect(
  host="localhost",
  user="your_username",
  password="your_password",
  database="bookstore"
)

# Create a cursor object to execute SQL queries
cursor = db.cursor()

def get_books_by_author(author_id):
  # Query the database to retrieve books by a specific author
  cursor.execute("SELECT title FROM Books WHERE author_id = %s", (author_id,))
  books = cursor.fetchall()
  return [book[0] for book in books]

# Test the function
author_id = 1
books = get_books_by_author(author_id)
print(f"Books written by author {author_id}: {', '.join(books)}")

# Close the cursor and connection
cursor.close()
db.close()
