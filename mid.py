class Library:
    book_list = []

    @classmethod
    def entry_book(cls, book):
        cls.book_list.append(book)

    @classmethod
    def view_books(cls):
        for book in cls.book_list:
            print(f"ID: {book.id()}, NAME: {book.name()}, Author: {book.writer()}, Availability: {'Available' if book.is_available() else 'Borrowed'}")


class Book:
    def __init__(self, book_id, title, author, availability):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.availability = availability
        Library.entry_book(self)

    def borrow_book(self):
        if self.availability:
            self.availability = False
            print("Successfully borrowed")
        else:
            print("Book is already borrowed")

    def return_book(self):
        if not self.availability:
            self.availability = True
            print("Successfully returned")
        else:
            print("Book is not borrowed")

    def id(self):
        return self.book_id

    def name(self):
        return self.title

    def writer(self):
        return self.author

    def is_available(self):
        return self.availability


# Initialize the library with books
Book(101, 'SCIENCE BOOK', 'H.K', True)
Book(105, 'THERMO DYNAMICS', 'H.K', True)
Book(102, 'DATA STRUCTURES AND ALGORITHMS', 'Mark Allen Weiss', True)
Book(108, 'DATABASE SYSTEMS', 'Ramez Elmasri', False)
Book(104, 'MATHEMATICAL PHYSICS', 'BERJLAL', False)

# Main menu
print("CHOOSE WHAT TO DO")
print("Menu:")
print("1. View books")
print("2. Borrow books")
print("3. Return books")
print("4. Exit")

while True:
    choice = int(input("\nEnter your choice: "))
    
    if choice == 1:
        Library.view_books()

    elif choice == 2:
        bk_id = int(input("Enter book ID to borrow: "))
        for book in Library.book_list:
            if book.id() == bk_id:
                book.borrow_book()
                break
        else:
            print("Invalid ID")

    elif choice == 3:
        bk_id = int(input("Enter book ID to return: "))
        for book in Library.book_list:
            if book.id() == bk_id:
                book.return_book()
                break
        else:
            print("Invalid ID")

    elif choice == 4:
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")
