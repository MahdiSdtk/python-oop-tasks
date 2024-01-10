class Library:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.lib = []
        return cls._instance

    books = {}
    class Book:

        #

        def __addBook(self, bid, name, author, genre, pg):
            Library.books[bid] = [name, author, genre, pg] # storing the book id along with its name - gets called when a instance of Book os created

        def __init__(self, bid, name, author, genre, pg): # bid -> book id
            self.bid = bid
            self._name = name
            self._author = author
            self._genre = genre
            self._pg = pg
            self.__addBook(bid, name, author, genre, pg) # adds the book to the library database
            #Library.books[bid] = [name, author, genre, pg] # storing the book id along with its name
        
        def update(self, bid: int, name=None, author=None, genre=None, pg=None):
            if bid in Library.books:
                if name:
                    self._name = name
                    Library.books[bid][0] = name
                if author:
                    self._author = author
                    Library.books[bid][1] = author
                if genre:
                    self._genre = genre
                    Library.books[bid][2] = genre
                if pg:
                    self._pg = pg
                    Library.books[bid][3] = pg
            else: print('the book not found.')

        def delete(self, bid: int):
            if bid:
                del Library.books[bid]
            else: print('you must provide the id of the book.')
        
        def search(self, name=None, author=None, genre=None):
            if name:
                print('search results: ')
                for i in Library.books:
                    if name == Library.books[i][0]: print(Library.books[i])
                    else: print('it didnt found any books.')
            if author:
                print('search results: ')
                for i in Library.books:
                    if author == Library.books[i][1]: print(Library.books[i])
                    else: print('it didnt found any books.')
            if genre:
                print('search results: ')
                for i in Library.books:
                    if genre == Library.books[i][2]: print(Library.books[i])
                    else: print('it didnt found any books.')
            if not name and not author and not genre: print('you need to give atleast one argument')

        def get_name(self):
            return self._name

    def add_book():
        pass



book1 = Library.Book(1, 'Fate', 'Sholokhov', 'social', 112)
book1 = Library.Book(2, 'Poor', 'Solokov', 'social', 160)

print(book1.get_name())
book1.update(1, name='tropo')
print(book1.get_name())
book1.search(author='Fiodor')
book1.search()
book1.delete(1)
print(Library.books)