
class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    # name property
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value.strip():
            raise Exception("Name must be a non-empty string")
        self._name = value

    # returns all contracts belonging to this author
    def contracts(self):
        return [c for c in Contract.all if c.author == self]

    # returns all books this author has contracts for
    def books(self):
        return [c.book for c in self.contracts()]

    # sign a contract
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    # total royalties
    def total_royalties(self):
        return sum(c.royalties for c in self.contracts())




class Book:
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        """Return all contracts for this book"""
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        """Return all authors for this book (via Contract)"""
        return [contract.author for contract in self.contracts()]





class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    # author property
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("author must be an Author instance")
        self._author = value

    # book property
    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise Exception("book must be a Book instance")
        self._book = value

    # date property
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if not isinstance(value, str) or not value.strip():
            raise Exception("date must be a non-empty string")
        self._date = value

    # royalties property
    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, int) or value < 0:
            raise Exception("royalties must be a non-negative integer")
        self._royalties = value

    # class method to filter by date
    @classmethod
    def contracts_by_date(cls, date):
        return [c for c in cls.all if c.date == date]
