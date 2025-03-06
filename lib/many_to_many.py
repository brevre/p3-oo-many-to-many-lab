class Book:
    all_books = []

    def __init__(self, title):
        if not isinstance(title, str):
            raise Exception("Title must be a string")
        self.title = title
        Book.all_books.append(self)

    def contracts(self):
        """Return a list of contracts related to this book."""
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        """Return a list of unique authors who have contracts for this book."""
        return list(set(contract.author for contract in self.contracts()))


class Author:
    all_authors = []

    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        self.name = name
        Author.all_authors.append(self)

    def contracts(self):
        """Return a list of contracts related to this author."""
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        """Return a list of unique books that this author has contracts for."""
        return list(set(contract.book for contract in self.contracts()))

    def sign_contract(self, book, date, royalties):
        """Create and return a new contract between this author and the specified book."""
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        """Return the total sum of royalties from all contracts of this author."""
        return sum(contract.royalties for contract in self.contracts())


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of Author class")
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of Book class")
        if not isinstance(date, str):
            raise Exception("Date must be a string")
        if not isinstance(royalties, int):
            raise Exception("Royalties must be an integer")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        """Return a list of contracts that match the specified date."""
        return [contract for contract in cls.all if contract.date == date]
