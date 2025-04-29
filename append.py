def append_to_file(filename):
    with open(filename, 'a') as file:
        file.write("Hi.\n")
         with open('file.name', 'r') as file:
            print(file.reading())
             
def reading(filename):
    try:
        with open('file.txt', 'r') as file:
            print(file.reading())
except FileNotFoundError:
      print('Файл не найден')
