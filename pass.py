def processing (text: str, flag: bool, number: float):
    for num in range(0, int(number)):
        square = num ** 2
        if num == 4:
            continue  
        if num == 9:
            break 
        if square > 50:
            print(f"Квадрат числа {num} больше 50")
        print(f"Квадрат числа {num} = {square}")
processing ("sample text", True, 10.0)
processing ("pink", False, 4.4)

