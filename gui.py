import tkinter as tk
from tkinter import ttk
import mysql.connector
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class BookstoreGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Bookstore GUI")

        # Create GUI components
        self.author_id_label = tk.Label(root, text="Author ID:")
        self.author_id_label.pack()

        self.author_id_entry = tk.Entry(root, width=20)
        self.author_id_entry.pack()

        self.filter_label = tk.Label(root, text="Filter by:")
        self.filter_label.pack()

        self.filter_var = tk.StringVar()
        self.filter_var.set("Title")  # default value

        self.title_radio = tk.Radiobutton(root, text="Title", variable=self.filter_var, value="Title")
        self.title_radio.pack()

        self.author_radio = tk.Radiobutton(root, text="Author", variable=self.filter_var, value="Author")
        self.author_radio.pack()

        self.genre_radio = tk.Radiobutton(root, text="Genre", variable=self.filter_var, value="Genre")
        self.genre_radio.pack()

        self.sort_label = tk.Label(root, text="Sort by:")
        self.sort_label.pack()

        self.sort_var = tk.StringVar()
        self.sort_var.set("Ascending")  # default value

        self.ascending_radio = tk.Radiobutton(root, text="Ascending", variable=self.sort_var, value="Ascending")
        self.ascending_radio.pack()

        self.descending_radio = tk.Radiobutton(root, text="Descending", variable=self.sort_var, value="Descending")
        self.descending_radio.pack()

        self.search_button = tk.Button(root, text="Search", command=self.get_books_by_author)
        self.search_button.pack()

        self.results_text = tk.Text(root, width=40, height=10)
        self.results_text.pack()

        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.axis = self.figure.add_subplot(111)
        self.chart_type = FigureCanvasTkAgg(self.figure, master=root)
        self.chart_type.draw()
        self.chart_type.get_tk_widget().pack()

    def get_books_by_author(self):
        try:
            # Get the author ID from the text input field
            author_id = int(self.author_id_entry.get())

            # Establish a connection to the database
            db = mysql.connector.connect(
                host="localhost",
                user="your_username",
                password="your_password",
                database="bookstore"
            )

            # Create a cursor object to execute SQL queries
            cursor = db.cursor()

            # Query the database to retrieve books by a specific author
            cursor.execute("SELECT title FROM Books WHERE author_id = %s", (author_id,))
            books = cursor.fetchall()

            # Apply filtering and sorting options
            filter_by = self.filter_var.get()
            sort_by = self.sort_var.get()
            if filter_by == "Title":
                books = sorted(books, key=lambda x: x[0])
            elif filter_by == "Author":
                cursor.execute("SELECT author FROM Authors WHERE id = %s", (author_id,))
                author_name = cursor.fetchone()[0]
                books = [book for book in books if author_name in book[0]]
            elif filter_by == "Genre":
                cursor.execute("SELECT genre FROM Books WHERE author_id = %s", (author_id,))
                genres = [row[0] for row in cursor.fetchall()]
                books = [book for book in books if any(genre in book[0] for genre in genres)]
            if sort_by == "Ascending":
                books = sorted(books, key=lambda x: x[0])
            elif sort_by == "Descending":
                books = sorted(books, key=lambda x: x[0], reverse=True)

            # Display the results in the text box
            self.results_text.delete(1.0, tk.END)
            self.results_text.insert(tk.END, f"Books written by author {author_id}: {', '.join([book[0] for book in books])}")

            # Create a bar chart to display the number of books written by each author
            self.axis.clear()
            self.axis.bar(range(len(books)), [1] * len(books))
            self.axis.set_xlabel("Book Title")
            self.axis.set_ylabel("Number of Books")
            self.axis.set_title("Books Written by Author")
            self.chart_type.draw()

        except ValueError:
            # Handle invalid input (e.g., non-numeric characters)
            self.results_text.delete(1.0, tk.END)
            self.results_text.insert(tk.END, "Invalid input. Please enter a valid author ID.")

        except mysql.connector.Error as err:
            # Handle database connection errors
            self.results_text.delete(1.0)
            self.results_text.insert(tk.END, f"Error: {err}")
