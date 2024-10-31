class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False
            print(f"El libro {self.title} ha sido prestado")

        else:
            print(f"El libro {self.title} no esta disponible")

    def return_book(self):
        self.available = True
        print(f"El libro {self.title} hasido devuelto")

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_book = []

    def borrow_book(self, book):
        if book.available:
            book.borrow()
            self.borrowed_book.append(book)
        else:
            print(f"El libro {book.title}, No esta disponible")

    def return_book(self, book):
        if book in self.borrowed_book:
            book.return_book()
            self.borrowed_book.remove(book)
        else:
            print(f"El libro {book.title}, no esta en la lista de prestamos.")

class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)
        print(f"El libro {book.title} ha sido agregado")

    def add_user(self,user):
        self.user = user
        print(f"El usuario {user.name} ha sido agregado con exito")

    def show_books(self):
        print(f"Los libros disponibles:")
        for book in self.books:
            if book.available:
                print(f"{book.title} escrito por {book.author}")


#Create Books
book_one = Book("El Principito", "Antoine de Saint-Exupery")
book_two = Book("1984", "George Orwell")

#Create users
user_one = User("Axier", "001")

#Create Library
library = Library()
library.add_book(book_one)
library.add_book(book_two)
library.add_user(user_one)

#Show books
library.show_books()

#Make a borrow
user_one.borrow_book(book_one)

#Show books
library.show_books()

#Return book
user_one.return_book(book_one)

#Show books
library.show_books()
