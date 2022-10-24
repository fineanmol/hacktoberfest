## LANGUAGE: Python
## AUTHOR: Satya
## GITHUB: https://github.com/sposada3

import turtle
screen = turtle.Screen().bgcolor("Black")
t = turtle.Turtle()

t.pencolor("steelblue")

# write
font = ("courier", 50, "bold")
t.write("Hello World!", font=font, align="center")
t.hideturtle()
turtle.exitonclick()