# LANGUAGE: Python 2.7
# AUTHOR: Shlok Chaitanya
# GITHUB: https://github.com/ShlokChaitanya

class Person:
    def __init__(self, name='Anonymous', location='USA', age=18):
        self.name = name
        self.place = location
        self.age = age
        self.email = None

    def set_email(self, email):
        self.email = email

    def get_email(self):
        return self.email

    def set_age(self, age):
        if age >= 0:
            self.age = age
        else:
            print("Age cannot be negative.")

    def get_age(self):
        return self.age

    def update_info(self, name=None, location=None, age=None, email=None):
        if name is not None:
            self.name = name
        if location is not None:
            self.place = location
        if age is not None:
            self.set_age(age)
        if email is not None:
            self.set_email(email)

    def greeting(self, name=None):
        name = name or self.name
        greeting_str = f"Hello, World! by {name}"
        print(greeting_str)
        return greeting_str

# Create a Person object
myself = Person('Anmol', 'UK', 25)

# Set and get email
myself.set_email('anmol@example.com')
print(f"Email: {myself.get_email()}")

# Update information
myself.update_info(name='Anmol Agarwal', age=26)

# Get age
print(f"Age: {myself.get_age()}")

# Display greeting
myself.greeting()
