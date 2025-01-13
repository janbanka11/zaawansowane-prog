class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        return self.marks > 50

    def __str__(self):
        return f"Student: {self.name}, Marks: {self.marks}\n"


class Library:
    def __init__(self, city, street, zip_code, phone, open_hours: str):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone
        self.open_hours = open_hours

    def __str__(self):
        return f"Library: {self.city}, {self.street}, {self.zip_code}, {self.phone}, Hours: {self.open_hours}\n"


class Employee:
    def __init__(
        self,
        first_name,
        last_name,
        hire_date,
        birth_date,
        city,
        street,
        zip_code,
        phone,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return (
            f"Employee: {self.first_name} {self.last_name}, Hired: {self.hire_date}, "
            f"Birth: {self.birth_date}, Address: {self.city}, {self.street}, {self.zip_code}, {self.phone}\n"
        )


class Book:
    def __init__(
        self, library, publication_date, author_name, author_surname, number_of_pages
    ):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return (
            f"Book: {self.author_name} {self.author_surname}, Published: {self.publication_date}, "
            f"Pages: {self.number_of_pages}, Library: {self.library}\n"
        )


class Order:
    def __init__(self, employee, student, order_date, books: list):
        self.employee = employee
        self.student = student
        self.order_date = order_date
        self.books = books

    def __str__(self):
        books_str = "\n    ".join(str(book).strip() for book in self.books)
        return (
            f"Order Date: {self.order_date}\n"
            f"{self.employee}\n{self.student}\nBooks:\n    {books_str}\n"
        )


# Tworzenie obiektów
lib1 = Library("Katowice", "Sezamkowa 15", "40-200", "111222333", "12")
lib2 = Library("Katowice", "Rozana 32", "40-102", "121242383", "22")

book1 = Book("Example1", "12-12-24", "Robert", "Lewandowski", 55)
book2 = Book("Example1", "17-12-24", "Anna", "Pazdan", 244)
book3 = Book("Example2", "15-12-24", "Ryszard", "Grosicki", 321)

employee1 = Employee(
    "Adam",
    "Malysz",
    "01-01-24",
    "01-02-97",
    "Gliwice",
    "Wspaniala 43",
    "44-100",
    "0123456789",
)
employee2 = Employee(
    "Bronislaw",
    "Komorowski",
    "15-04-10",
    "30-12-46",
    "Pruszkow",
    "Wiejska 2",
    "23-133",
    "12343456678",
)

student1 = Student("Jan", 60)
student2 = Student("Juan", 33)

order1 = Order(employee1, student1, "2023-12-01", [book1, book2])
order2 = Order(employee2, student2, "2023-12-02", [book3])

# Wypisanie danych
print(order1)
print("==================\n")
print(order2)
