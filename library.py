class LibraryCatalog:
    def __init__(self, name):
      self.name = name
      self.books = []
    
    def __str__(self):
        if len(self.books) == 0:
            return "The catalog '" + self.name + "' is empty."
        else:
            tempStr = "Catalog '" + self.name + "':\n"
            for book in self.books:
                tempStr += "Title: " + str(book["title"]) + ", Author: " + str(book["author"]) + ", Year: " + str(book["year"]) + "\n"
            return tempStr
        
    
    def add_book(self, title, author, year):
        book = {"title": title, "author": author, "year":year}
        self.books.append(book)
        print("Added book '" + title + "' to the catalog '" + self.name + "'.")
    
    def remove_book(self, title):
        for book in self.books:
            if book["title"] == title:
                self.books.remove(book)
                print("Removed book '" + title + "' from the catalog '" + self.name + "'.")
                return
        print("Book '" + title + "' not found in the catalog '" + self.name + "'.")
    
    def search_book(self, title):
        for book in self.books:
            if book["title"] == title:
                return "Book found: Title: " + str(book["title"]) + ", Author: " + str(book["author"]) + ", Year: " + str(book["year"]) + "\n"
        return "Book '" + title + "' not found in the catalog."
    
    def compare_catalogs(self, other_catalog):
        commonBookList = []
        for book in self.books:
            if book in other_catalog.books:
                commonBookList.append(book)
        return commonBookList
    
    def group_by_year(self):
        yearDict = {}
        for book in self.books:
            if book["year"] in yearDict:
                yearDict[book["year"]].append(book)
            else:
                yearDict[book["year"]] = [book]
        return yearDict
    
    def search_by_author(self, author):
        bookList = []
        for book in self.books:
            if book["author"] == author:
                bookList.append(book["title"])
        if len(bookList) == 0:
            return "No books found by " + author + "."
        else:
            return bookList
    

# Testing the LibraryCatalog class
catalog = LibraryCatalog("Computer Science")
print(catalog)
# Add some books
catalog.add_book("Python Programming", "John Smith", 2019)
catalog.add_book("Introduction to Algorithms", "Thomas Cormen", 2009)
catalog.add_book("Data Science for Beginners", "Emily Davis", 2021)
catalog.add_book("Web Development Basics", "John Smith", 2021)
catalog.add_book("Data Structures and Algorithms", "Jane Doe", 2009)
print(catalog)
# Test searching for a book
print(catalog.search_book("Python Programming"))
print(catalog.search_book("Introduction to Coding"))
# Test removing a book
catalog.remove_book("Introduction to Algorithms")
catalog.remove_book("Introduction to Coding")
print(catalog)
# Create a second instance of the LibraryCatalog class
print("Creating a second catalog:")
catalog2 = LibraryCatalog("Programming")
catalog2.add_book("Python Programming", "John Smith", 2019)
catalog2.add_book("Introduction to Programming", "Jane Doe", 2020)
catalog2.add_book("Data Science for Beginners", "Emily Davis", 2021)
# Compare two catalogs
print("Comparing catalogs:")
common_books = catalog.compare_catalogs(catalog2)
print(common_books)
# Group books by year
print("Grouping books by year:")
books_by_year = catalog.group_by_year()
print(books_by_year)
# Search for books by author
print("Searching for books by author:")
author = "John Smith"
books_by_author = catalog.search_by_author(author)
print(books_by_author)
author2 = "Fyodor Dostoevsky"
books_by_author = catalog.search_by_author(author2)
print(books_by_author)
