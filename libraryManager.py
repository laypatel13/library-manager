import json
import os

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.is_read = False

    def display(self):
        status = "Read" if self.is_read else "Unread"
        print(f'Title: {self.title} | Author: {self.author} | Year: {self.year}')

    def mark_as_read(self):
        self.is_read = True

class Library:
    def __init__(self):
        self.books = []

    def add_book(self):
        title = input("Enter the title of the Book: ")
        author = input("Enter the author of the Book: ")
        year = input("Enter the year of the Book: ")
        book = Book(title, author, year)
        self.books.append(book)
        print("Book added!")

    def view_books(self):
        pass

    def view_unread(self):
        pass

    def save(self):
        pass

    def load(self):
        pass