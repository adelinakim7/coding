import json
import os

class Book:
    def init(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def str(self):
        return f"{self.title} ({self.author}, {self.year})"

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "year": self.year
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["title"], data["author"], data["year"])


class Library:
    def init(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Книга '{book.title}' добавлена.")
        self.save()

    def remove_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print(f"Книга '{title}' удалена.")
                self.save()
                return
        print(f"Книга '{title}' не найдена.")

    def show_all_books(self):
        if self.books:
            print("Список книг:")
            for i, book in enumerate(self.books, 1):
                print(f"{i}. {book}")
        else:
            print("Список книг пуст.")

    def save(self):
        data = [book.to_dict() for book in self.books]
        with open("books.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def load(self):
        if os.path.exists("books.json"):
            with open("books.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                self.books = [Book.from_dict(item) for item in data]


my_library = Library()
my_library.load()

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
