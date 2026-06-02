import json
import os
from colorama import init, Fore, Back, Style
from tabulate import tabulate

init(autoreset=True)

books = []


def load_books():
    if os.path.exists("books.json"):
        try:
            with open("books.json", "r") as f:
                content = f.read()
                if content.strip() == "":
                    return []
                return json.loads(content)
        except (json.JSONDecodeError, IOError) as e:
            print(Fore.WHITE + Back.RED + f"Fatal Error: Failed To Load Books. {e}" + Style.RESET_ALL)
            return []
    return []


def save_books():
    try:
        with open("books.json", "w") as f:
            json.dump(books, f)
    except IOError as e:
        print(Fore.WHITE + Back.RED + f"Fatal Error: Failed To Save Books. {e}" + Style.RESET_ALL)


def add_book():
    while True:
        title = input(
            Fore.WHITE + Style.NORMAL + "Enter Book Title (or 'quit' to finish): " + Style.RESET_ALL)
        if title.lower() == "quit":
            break
        author = input(Fore.WHITE + Style.NORMAL + "Enter Author Name: " + Style.RESET_ALL)

        year = input(Fore.WHITE + Style.NORMAL + "Enter Publication Year: " + Style.RESET_ALL)

        new_book = {
            "title": title,
            "author": author,
            "year": year,
            "is_read": False
        }

        books.append(new_book)

        print(Fore.GREEN + Back.BLACK + Style.BRIGHT + "Book Added Successfully!" + Style.RESET_ALL + "\n")


def view_books():
    if not books:
        print(Fore.WHITE + Back.BLACK + Style.BRIGHT + "No Books In Library." + Style.RESET_ALL)
        return

    print("\n" + Fore.BLACK + Back.WHITE + "--- Library Books ---" + Style.RESET_ALL)

    table_data = []

    for index, book in enumerate(books, start=1):

        status = "Read" if book["is_read"] else "Unread"

        table_data.append([index, book["title"], book["author"], book["year"], status])

    headers = ["Index", "Title", "Author", "Year", "Status"]

    print(tabulate(table_data, headers=headers, tablefmt="pretty", disable_numparse=True))


def view_unread_books():
    unread_books = []

    for book in books:
        if not book["is_read"]:
            unread_books.append(book)

    if not unread_books:
        print(Fore.WHITE + Back.BLACK + Style.BRIGHT + "No Unread Books Found." + Style.RESET_ALL)
        return

    print("\n" + Fore.BLACK + Back.WHITE + "--- Unread Books ---" + Style.RESET_ALL)

    table_data = []

    for index, book in enumerate(unread_books, start=1):
        table_data.append([index, book["title"], book["author"], book["year"]])

    headers = ["Index", "Title", "Author", "Year"]

    print(tabulate(table_data, headers=headers, tablefmt="pretty", disable_numparse=True))


def mark_book_as_read():
    if not books:
        print(Fore.WHITE + Back.BLACK + Style.BRIGHT + "No Books Available." + Style.RESET_ALL)
        return

    view_books()

    try:
        index_num = int(
            input("\n" + Fore.CYAN + Style.BRIGHT + "Enter Book Index To Mark As Read: " + Style.RESET_ALL))

        if index_num < 1 or index_num > len(books):
            print(Fore.RED + Style.BRIGHT + "Invalid Index!" + Style.RESET_ALL)
            return

        books[index_num - 1]["is_read"] = True

        save_books()

        print(Fore.GREEN + Back.BLACK + Style.BRIGHT + "Book Marked As Read!" + Style.RESET_ALL)

    except ValueError:
        print(Fore.RED + Style.BRIGHT + "Please Enter A Valid Number." + Style.RESET_ALL)


def reset_library():
    global books

    confirm = input(Fore.RED + Style.BRIGHT + "Are You Sure You Want To Delete All Books? (yes/no): " + Style.RESET_ALL
    )

    if confirm.lower() == "yes":
        books = []
        save_books()

        print(Fore.GREEN + Back.BLACK + "Library Reset Successfully!" + Style.RESET_ALL)

    else:
        print(Fore.RED + "Reset Cancelled." + Style.RESET_ALL)


def main():
    global books

    books = load_books()

    while True:

        print("\n" +  Fore.BLACK + Back.WHITE + "--- Library Manager ---" + Style.RESET_ALL)

        print(Fore.YELLOW + "(1) Add New Book" + Style.RESET_ALL)
        print(Fore.YELLOW + "(2) View All Books" + Style.RESET_ALL)
        print(Fore.YELLOW + "(3) View Unread Books" + Style.RESET_ALL)
        print(Fore.YELLOW + "(4) Mark Book As Read" + Style.RESET_ALL)
        print(Fore.YELLOW + "(5) Quit Library Manager" + Style.RESET_ALL)
        print(Fore.YELLOW + "(6) Reset Library" + Style.RESET_ALL)

        choice = input("\n" + Fore.CYAN + Style.BRIGHT + "Enter Your Choice: " + Style.RESET_ALL)

        if choice == "1":
            add_book()
            save_books()

        elif choice == "2":
            view_books()

        elif choice == "3":
            view_unread_books()

        elif choice == "4":
            mark_book_as_read()

        elif choice == "5":
            print(Fore.WHITE + Style.BRIGHT + "Bye! Thanks For Using The Library Manager!" + Style.RESET_ALL)
            break

        elif choice == "6":
            reset_library()

        else:
            print(Fore.RED + Style.BRIGHT + "Invalid Choice, Try Again!" + Style.RESET_ALL)


if __name__ == "__main__":
    main()