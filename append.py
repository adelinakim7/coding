def append_to_file(filename):
    with open(filename, 'a') as file:
        file.write("Hi.\n")
