library = {}


def add_book():
    book_id = input("Enter Book ID: ").strip()
    if book_id in library:
        print("Book ID already exists.")
        return
    title = input("Enter Book Title: ").strip()
    author = input("Enter Author Name: ").strip()
    quantity = int(input("Enter Quantity: "))
    library[book_id] = {
        "title": title.title(),
        "author": author.title(),
        "quantity": quantity,
        "issued": 0,
    }
    print("Book added successfully.")


def display_books():
    if not library:
        print("No books available in the library.")
        return
    print("\n" + "-" * 60)
    print(f"{'ID':<8}{'Title':<22}{'Author':<18}{'Avail':<6}{'Issued':<6}")
    print("-" * 60)
    for book_id, info in library.items():
        available = info["quantity"] - info["issued"]
        print(f"{book_id:<8}{info['title']:<22}{info['author']:<18}{available:<6}{info['issued']:<6}")
    print("-" * 60)


def search_book():
    keyword = input("Enter title or author to search: ").strip().lower()
    found = False
    for book_id, info in library.items():
        if keyword in info["title"].lower() or keyword in info["author"].lower():
            available = info["quantity"] - info["issued"]
            print(f"{book_id} | {info['title']} | {info['author']} | Available: {available}")
            found = True
    if not found:
        print("No matching book found.")


def issue_book():
    book_id = input("Enter Book ID to issue: ").strip()
    if book_id not in library:
        print("Book not found.")
        return
    info = library[book_id]
    if info["quantity"] - info["issued"] > 0:
        info["issued"] += 1
        print(f"'{info['title']}' issued successfully.")
    else:
        print("No copies available to issue.")


def return_book():
    book_id = input("Enter Book ID to return: ").strip()
    if book_id not in library:
        print("Book not found.")
        return
    info = library[book_id]
    if info["issued"] > 0:
        info["issued"] -= 1
        print(f"'{info['title']}' returned successfully.")
    else:
        print("No copies of this book are currently issued.")


def remove_book():
    book_id = input("Enter Book ID to remove: ").strip()
    if book_id in library:
        removed = library.pop(book_id)
        print(f"'{removed['title']}' removed successfully.")
    else:
        print("Book not found.")


def menu():
    while True:
        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Add Book")
        print("2. Display All Books")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Remove Book")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ").strip()
        if choice == "1":
            add_book()
        elif choice == "2":
            display_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            issue_book()
        elif choice == "5":
            return_book()
        elif choice == "6":
            remove_book()
        elif choice == "7":
            print("Exiting Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")


menu()
