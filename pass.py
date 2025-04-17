def processing (text: str, flag: bool, number: float):
    try:
        if text == "":
            raise valueError("Строка не может быть пустой")
    except:
        pass
    spisok = []
    for num in range(0, int(number)):
        square = num ** 2
        if num == 4:
            continue  
        if num == 9:
            break 
        if square > 50:
            print(f"Квадрат числа {num} больше 50")
        if 20 <= square <= 50:
            print(f"Квадрат числа {num} больше или равен 20 и меньше или равен 50")
        else:
            print(f"Квадрат числа {num} меньше 20")
        print(f"Квадрат числа {num} = {square}")
        spisok.append(square) 
        return spisok
processing ("sample text", True, 10.0)
processing ("pink", False, 4.4)
