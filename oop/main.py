# main.py

from book_class import Book
from library_system import EBook, PrintBook, Library

def test_book_class():
    print("Testing Book class with magic methods:")
    # Creating an instance of Book
    my_book = Book("1984", "George Orwell", 1949)

    # Demonstrating the __str__ method
    print(my_book)  # Expected to use __str__

    # Demonstrating the __repr__ method
    print(repr(my_book))  # Expected to use __repr__

    # Deleting a book instance to trigger __del__
    del my_book
    print()

def test_library_system():
    print("Testing Library system with inheritance and composition:")
    # Create a Library instance
    my_library = Library()

    # Create instances of each type of book
    classic_book = Book("Pride and Prejudice", "Jane Austen", 1813)
    digital_novel = EBook("Snow Crash", "Neal Stephenson", 1992, 500)
    paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 1951, 234)

    # Add books to the library
    my_library.add_book(classic_book)
    my_library.add_book(digital_novel)
    my_library.add_book(paper_novel)

    # List all books in the library
    my_library.list_books()

if __name__ == "__main__":
    test_book_class()
    test_library_system()
