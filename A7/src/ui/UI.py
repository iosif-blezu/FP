from src.domain.book import Book
from src.services.book_service import BookService


class Ui:
    def menu(self):
        while True:
            books = BookService()
            print("1. MemoryRepository")
            print("2. TextFileRepository")
            print("3. BinaryFileRepository")
            print("0. Exit")
            rtype = int(input("Choose: "))
            if rtype in [1, 2, 3]:
                books.add_the_books(rtype)
            elif rtype == 0:
                exit()
            else:
                print("Invalid input")

            while True:
                print("1. Add book")
                print("2. Display books")
                print("3. Filter books")
                print("4. Undo")
                print("5. Use another method.")
                print("0. Exit")
                choice = int(input("Choose: "))
                if choice == 1:
                    isbn = input("ISBN: ")
                    author = input("Author: ")
                    title = input("Title: ")
                    try:
                        books.add_book(Book(isbn, author, title), rtype)
                    except ValueError as error:
                        print(str(error))
                elif choice == 2:
                    print(str(books))
                elif choice == 3:
                    word = input("Delete books starting with: ")
                    books.filter_books(word, rtype)
                elif choice == 4:
                    try:
                        books.undo(rtype)
                    except ValueError as error:
                        print(str(error))
                elif choice == 5:
                    break
                elif choice == 0:
                    exit()
                else:
                    print("Invalid input")


if __name__ == '__main__':
    ui = Ui()
    ui.menu()
