
def read_file(file_path):
    with open(file_path, "r") as file:
        return file.read()


data = read_file("example.txt")
print(data)
