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
    pass