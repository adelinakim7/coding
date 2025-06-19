class Book():
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} ({self.author}, {self.year})"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Книга '{book.title}' добавлена.")

    def remove_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print(f"Книга '{title}' удалена.")
                return
        print(f"Книга '{title}' не найдена.")

    def show_all_books(self):
        if self.books:
            print("Список книг:")
            for i, book in enumerate(self.books, 1):
                print(f"{i}. {book}")
        else:
            print("Список книг пуст.")

my_library = Library()

book1 = Book("Большая книга серийных убийц", "Джек Роузвуд", 2024)
book2 = Book("Ромео и Джульетта", "Уильям Шекспир", 1595)
book3 = Book("Гамлет", "Уильям Шекспир", 1603)

my_library.add_book(book1)
my_library.add_book(book2)
my_library.add_book(book3)

my_library.show_all_books()

my_library.remove_book("Большая книга серийных убийц")

my_library.show_all_books()


while True:
    action = input("\nВыберите действие (добавить/удалить/вывести/выход): ").strip().lower()

    if action == 'добавить':
        title = input("Введите название книги: ").strip()
        author = input("Введите автора книги: ").strip()
        try:
            year = int(input("Введите год издания: ").strip())
        except ValueError:
            print("Некорректный ввод года.")
            continue
        book = Book(title, author, year)
        my_library.add_book(book)

    elif action == 'удалить':
        title = input("Введите название книги для удаления: ").strip()
        my_library.remove_book(title)

    elif action == 'вывести':
        my_library.show_all_books()

    elif action == 'выход':
        print("Выход из программы.")
        break

    else:
        print("Неизвестное действие. Повторите ввод.")
