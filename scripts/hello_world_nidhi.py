# LANGUAGE: Python 3.11
# AUTHOR: Nidhi Nishad
# GITHUB: https://github.com/nidhi-2619

class Greet:
    def __init__(self, name):
        self.name = name

    def greet(self):
        """prints your name with hello world."""
        print(f"Hello World, I'm {self.name}")

if __name__ == '__main__':
    greet = Greet('Nidhi Nishad')
    greet.greet()