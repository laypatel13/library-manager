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
        print(f'Title: {self.title} | Author: {self.author} | Year: {self.year} | status: {status}')

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

    def save(self): # To add or dump data in json file
        books_data = []
        for book in self.books:
            book_dict = {
                "title": book.title,
                "author": book.author,
                "year": book.year,
                "is_read": book.is_read
            }
            books_data.append(book_dict)
        with open("books.json", "w") as f:
            json.dump(books_data, f)

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

def main():
    library = Library()     # create a Library object
    library.load()          # load books from file

    while True:
        print("\n--- Library Manager ---")
        print("1. Add book")
        print("2. View all books")
        print("3. View unread books")
        print("4. Mark book as read")
        print("5. Quit")

        choice = input("Enter choice: ")

        if choice == "1":
            library.add_book()
            library.save() # Handled save function by calling it no need to save sapratly.
        elif choice == "2":
            library.view_books()
        elif choice == "3":
            library.view_unread()
        elif choice == "4":
            index_num = int(input("Enter the index number of the Book: ")) - 1
            library.books[index_num].mark_as_read()
            library.save()
        elif choice == "5":
            print("Bye...!")
            break
        else:
            print("Invalid Choice😅")


main()