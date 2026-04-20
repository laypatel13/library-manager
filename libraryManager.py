import json
import os

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.is_read = False

    def display(self):
        status = "Read" if self.is_read else "Unread"  # Display the list of Books.
        print(f'Title: {self.title} | Author: {self.author} | Year: {self.year}')

    def mark_as_read(self):  # To change status of book
        self.is_read = True

class Library:
    def __init__(self):
        self.books = []

    def add_book(self):  # To add Book to list
        title = input("Enter the title of the Book: ")
        author = input("Enter the author of the Book: ")
        year = input("Enter the year of the Book: ")
        book = Book(title, author, year)
        self.books.append(book)
        print("Book added!")

    def view_books(self):  # to read the book list
        if not self.books:
            print("No books in library!")
            return
        for index, book in enumerate(self.books, start=1):
            print(f'{index}.', end=' ')
            book.display()

    def view_unread(self):  # To read only inread books by fetching them into a seprate list
        if not self.books:
            print("No books in library!")
            return
        for index, book in enumerate(self.books, start=1):
            print(f'{index}.', end=' ')
            book.display()

    def save(self):
        pass

    def load(self):  # To load the json file in a list to handle them
        if os.path.exists("books.json"):
            with open("books.json", "r") as f:
                content = f.read()
                if content.strip() == "":
                    return
                books_data = json.loads(content)
                for book_dict in books_data:
                    book = Book(book_dict["title"], book_dict["author"], book_dict["year"])
                    book.is_read = book_dict["is_read"]
                    self.books.append(book)