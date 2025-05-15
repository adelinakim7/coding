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

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.__account_number = account_number  
        self.__balance = balance            
    
    def deposit(self, amount):
        """Пополнение счёта"""
        if amount > 0:
            self.__balance += amount
            print(f"Пополнение на {amount} руб. Успешно!")
        else:
            print("Ошибка: сумма пополнения должна быть положительной")
    
    def withdraw(self, amount):
        """Снятие средств"""
        if amount <= 0:
            print("Ошибка: сумма снятия должна быть положительной")
        elif amount > self.__balance:
            print("Ошибка: недостаточно средств на счёте")
        else:
            self.__balance -= amount
            print(f"Снятие {amount} руб. Успешно!")
    
    def get_balance(self):
        """Получение текущего баланса"""
        return self.__balance
    
    def get_account_number(self):
        """Получение номера счёта"""
        return self.__account_number


account = BankAccount("987654321", 5000)

try:
    print(account.__balance)
except AttributeError as e:
    print(f"Ошибка доступа: {e}")

print("Номер счёта:", account.get_account_number())
print("Баланс:", account.get_balance(), "руб.")

account.deposit(700)       
account.deposit(-500)      
account.withdraw(400)      
account.withdraw(3000)     
account.withdraw(-100)     

print("Итоговый баланс:", account.get_balance(), "руб.")
