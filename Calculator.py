from tkinter import *
from tkinter import messagebox
expression = ""

calc = Tk()
calc.title("Calculator")
calc.geometry("243x250")
font_format=("Calibri",10,"bold")
calc.configure(background="#202020")

def press(num):
    global expression
    expression+=str(num)
    equation.set(expression)

def back():
    global expression
    expression = expression[:-1]
    equation.set(expression)

def clear():
    global expression
    expression = ""
    equation.set(expression)

def equal():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression=str(total)
    except:
        expression = ""
        equation.set(expression)
        messagebox.showerror("Error!", "Invalid Input!")

equation = StringVar()
input = Entry(calc,textvariable=equation,font=("Comic Sans MS",7,"bold italic"))

one = Button(calc,text="1",fg="white", bg="#3B3B3B",height=2,width=7,command=lambda: press(1))
two = Button(calc,text="2",fg="white", bg="#3B3B3B",height=2,width=7,command=lambda: press(2))
three = Button(calc,text="3",fg="white", bg="#3B3B3B",height=2,width=7,command=lambda: press(3))
four = Button(calc,text="4",fg="white", bg="#3B3B3B",height=2,width=7,command=lambda: press(4))
five = Button(calc,text="5",fg="white", bg="#3B3B3B",height=2,width=7,command=lambda: press(5))
six = Button(calc,text="6",fg="white", bg="#3B3B3B",height=2,width=7,command=lambda: press(6))
seven = Button(calc,text="7",fg="white", bg="#3B3B3B",height=2,width=7,command=lambda: press(7))
eight = Button(calc,text="8",fg="white", bg="#3B3B3B",height=2,width=7,command=lambda: press(8))
nine = Button(calc,text="9",fg="white", bg="#3B3B3B",height=2,width=7,command=lambda: press(9))
zero = Button(calc,text="0",fg="white", bg="#3B3B3B",height=2,width=16,command=lambda: press(0))
dot = Button(calc,text=".",fg="white", bg="#3B3B3B",height=2,width=7,command=lambda: press('.'))

backspace = Button(calc,text="<-",fg="white", bg="#323232",height=2,width=8,command=back)
clear = Button(calc,text="C",fg="white",bg="red",height=2,width=20,font=font_format,command=clear)
plus = Button(calc,text="+",fg="white",bg="#323232",height=2,width=8,font=font_format,command=lambda: press('+'))
equals = Button(calc,text="=",fg="black",bg="#4CC2FF",height=2,width=8,font=font_format,command=equal)
minus = Button(calc,text="-",fg="white",bg="#323232",height=2,width=8,font=font_format,command=lambda: press('-'))
prod = Button(calc,text="x",fg="white",bg="#323232",height=2,width=8,font=font_format,command=lambda: press('*'))
div = Button(calc,text="/",fg="white",bg="#323232",height=2,width=8,font=font_format,command=lambda: press('/'))

input.grid(columnspan=3,ipadx=29,ipady=10)
div.grid(row=2,column=3)
one.grid(row=5,column=0)
two.grid(row=5,column=1)
three.grid(row=5,column=2)
four.grid(row=4,column=0)
five.grid(row=4,column=1)
six.grid(row=4,column=2)
seven.grid(row=3,column=0)
eight.grid(row=3,column=1)
nine.grid(row=3,column=2)
backspace.grid(row=0,column=3)
zero.grid(row=6,columnspan=2)
dot.grid(row=6,column=2)
plus.grid(row=5,column=3)
equals.grid(row=6,column=3)
minus.grid(row=4,column=3)
prod.grid(row=3,column=3)
clear.grid(row=2,columnspan=3)

calc.mainloop()