class Book:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

    def get_info(self):
        print(f'{self.name}, {self.author}, {self.year}')

class Library:
  def __init__(self):
    self.books = []

  def add_book(self, book):
    self.books.append(book)
    print(f"Книга '{book.name}' добавлена в библиотеку")

  def remove_book(self, book_name):
    for book in self.books:
      if book.name == book_name:
        self.books.remove(book)
        print(f"Книга '{book_name}' удалена из библиотеки")
        return
      print(f"Книга '{book_name}' не найдена")

  def show_all_books(self):
    if not self.books:
      print("В библиотеке нет книг")
      return
    print("Список книг в библиотеке:")
    for book in self.books:
      book.get_info()
      
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
