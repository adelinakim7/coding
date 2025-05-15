class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return f'"{self.title}" - {self.author}, published in {self.year}.'

book1 = Book("Romeo and Juliet" , " William Shakespeare", 1623)
book2 = Book("Serial killers", "Jack Rosewood", 2023)
book3 = Book("The Science of Influence", "Brian Tracy, Dan Stratzel", 2019)

print(book1.get_info())
print(book2.get_info())
print(book3.get_info())
