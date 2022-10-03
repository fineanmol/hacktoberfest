# LANGUAGE: Python
# AUTHOR: Valeron
# GITHUB: https://github.com/Valeron-T
# OBJECTIVE: Print Hello world diagonally


def get_n_spaces(num):
    word = ""
    for x in range(num):
        word = word + " "
    
    return word

def print_on_newline(text):
    for x, y in enumerate(text):
        formatted_line = get_n_spaces(x) + y
        print(formatted_line)


if __name__ == "__main__":
    print_on_newline("Hello World")
