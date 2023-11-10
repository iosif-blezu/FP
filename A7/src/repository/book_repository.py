from src.domain.book import Book
import pickle


class MemoryRepository:
    def __init__(self):
        self.__books = [Book("617-212", "J.R.R. Tolkien", "The Fellowship of the Ring"),
                        Book("271-444", "J.R.R. Tolkien", "The Two Towers"),
                        Book("323-122", "J.R.R. Tolkien", "The Return of the King "),
                        Book("777-777", "J.R.R. Tolkien", "The Militarisation"),
                        Book("623-134", "J.R.R. Tolkien", "The Hobbit"),
                        Book("311-631", "G.R.R. Martin", "A Game of Thrones"),
                        Book("321-212", "G.R.R. Martin", "A Clash of Kings"),
                        Book("561-872", "G.R.R. Martin", "A Storm of Swords"),
                        Book("551-998", "G.R.R. Martin", "A Feast for Crows"),
                        Book("412-189", "G.R.R. Martin", "A Dance with Dragons")]

    def get_books(self):
        return self.__books


class TextFileRepository:
    def __init__(self):
        self.__books = []

    def _read_file(self):
        f = open("../repository/text_file.txt", "r")
        while True:
            line = f.readline()
            if not line:
                break
            title, rest = line.split(" by ")
            author, isbn = rest.split(" ISBN: ")
            isbn, _ = isbn.split('\n')
            self.__books.append(Book(isbn, author, title))
        f.close()

    def get_books(self):
        self._read_file()
        return self.__books

    def update_file(self, books: list):
        string = ""
        for book in books:
            string += str(book) + '\n'
        f = open("../repository/text_file.txt", "w")
        f.write(string)
        f.close()


class BinaryFileRepository:
    def __init__(self):
        self.__books = []

    def get_books(self):
        self._read_file()
        return self.__books

    def update_file(self, books: list):
        f = open("../repository/binary_file.bin", "wb")
        pickle.dump(books, f)
        f.close()

    def _read_file(self):
        f = open("../repository/binary_file.bin", "rb")
        obj = pickle.load(f)

        for book in obj:
            self.__books.append(book)

        f.close()


