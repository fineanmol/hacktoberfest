# LANGUAGE: Python 3.0
# AUTHOR: Shlok Chaitanya
# GITHUB: https://github.com/ShlokChaitanya

import turtle

# Set up the Turtle graphics screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a Turtle object for drawing the benzene ring
benzene_ring = turtle.Turtle()
benzene_ring.speed(10)

# Function to draw a colorful semi-circle with a specified radius
def draw_semi_circle(radius, color):
    benzene_ring.fillcolor(color)
    benzene_ring.begin_fill()
    benzene_ring.circle(radius, 180)
    benzene_ring.right(180)
    benzene_ring.forward(10)
    benzene_ring.right(180)
    benzene_ring.circle(radius, 180)
    benzene_ring.end_fill()

# Set the initial position of the benzene ring
benzene_ring.penup()
benzene_ring.goto(0, -100)
benzene_ring.pendown()

# Draw a rainbow benzene ring
ring_colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for color in ring_colors:
    draw_semi_circle(100, color)

# Hide the benzene ring drawing Turtle
benzene_ring.hideturtle()

# Define the Person class
class Person:
    def __init__(self, name='Anonymous', location='USA', age=18, email=None, address=None):
        self.name = name
        self.location = location
        self.age = age
        self.email = email
        self.address = address

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

    def set_address(self, address):
        self.address = address

    def get_address(self):
        return self.address

    def update_info(self, name=None, location=None, age=None, email=None, address=None):
        if name is not None:
            self.name = name
        if location is not None:
            self.location = location
        if age is not None:
            self.set_age(age)

    def greet(self, name=None):
        name = name or self.name
        greeting_str = f"Hello, World! Greetings from {self.location} by {name}"
        print(greeting_str)
        return greeting_str

# Create a Person object
myself = Person(name='Anmol', location='UK', age=25)

# Set and get the email
myself.set_email('anmol@example.com')
print(f"Email: {myself.get_email()}")

# Update personal information
myself.update_info(name='Anmol Agarwal', age=26)

# Get the age
print(f"Age: {myself.get_age()}")

# Display the greeting message
myself.greet()

# Close the Turtle graphics window when clicking
screen.exitonclick()
