class Book:
    def __init__(self, isbn, author, title):
        self.__isbn = isbn
        self.__author = author
        self.__title = title

    def __str__(self):
        return self.__title + " by " + self.__author + " ISBN: " + self.__isbn

    def get_isbn(self):
        return self.__isbn

    def get_author(self):
        return self.__author

    def get_title(self):
        return self.__title

