import sys
from robust_division_calculator import safe_divide
from library_management import Book, Library

def division_calculator(args):
    if len(args) != 3:
        print("Usage: python main.py divide <numerator> <denominator>")
        sys.exit(1)

    numerator = args[1]
    denominator = args[2]

    result = safe_divide(numerator, denominator)
    print(result)

def library_management():
    # Setup a small library
    library = Library()
    library.add_book(Book("Brave New World", "Aldous Huxley"))
    library.add_book(Book("1984", "George Orwell"))

    # Initial list of available books
    print("Available books after setup:")
    library.list_available_books()

    # Simulate checking out a book
    library.check_out_book("1984")
    print("\nAvailable books after checking out '1984':")
    library.list_available_books()

    # Simulate returning a book
    library.return_book("1984")
    print("\nAvailable books after returning '1984':")
    library.list_available_books()

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <task> [<args>]")
        print("Tasks: divide, library")
        sys.exit(1)

    task = sys.argv[1]

    if task == "divide":
        division_calculator(sys.argv)
    elif task == "library":
        library_management()
    else:
        print("Invalid task. Use 'divide' or 'library'.")

if __name__ == "__main__":
    main()
