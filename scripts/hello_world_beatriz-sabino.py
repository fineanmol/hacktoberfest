
# Changing the above code to class based design.

class Greetings():
    def __init__(self, greetingType) -> None:
        self.type = greetingType

    def testing(self):
        if self.type == 'General':
            return "Hello World"
        elif self.type == "Morning":
            return "Good Morning world!"
        elif self.type == "Evening":
            return "Good Evening World"
        else:
            return "Hello!"



user1 = Greetings("Morning")
print(user1.testing())