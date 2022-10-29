from tkinter import *

root = Tk()
root.title("calculator")
root.geometry("700x500")
root.resizable(False, False)
# functions-----------------------------------
france = []


def com():
    history.clear()
    dr.configure(text="HISTORY:" + "  ".join(france), font="verdana 14 bold")


def red():
    w = len(q.get())
    qw = list(q.get())
    π = 22 / 7
    if qw[w - 1] == "+":
        q.insert(w, "π")
    elif qw[w - 1] == "-":
        q.insert(w, "π")
    elif qw[w - 1] == "*":
        q.insert(w, "π")
    elif qw[w - 1] == "/":
        q.insert(w, "π")
    elif q.get() == "0":
        q.delete(0, "end")
        q.insert(w, "π")
    else:
        q.insert(w, "*π")


def repo(x):
    if q.get() == "0":
        q.delete(0, "end")
        q.insert(0, str(x))
    else:
        wa = len(q.get())
        q.insert(wa, str(x))


def bst(x):
    if q.get() != "0":
        wa = len(q.get())
        q.insert(wa, str(x))


def dele():
    q.delete(0, "end")
    q.insert(0, "0")


history = []


def wer():
    q.insert(len(q.get()), "**")


def back():
    l = len(q.get())
    if l == 1:
        q.delete(0, "end")
        q.insert(0, "0")
    else:
        q.delete(l - 1, l)


history = []


def result():
    r = q.get()
    try:
        global result
        result = eval(r)
    except:
        print("error")
        result = "error"
    q.delete(0, "end")
    q.insert(0, str(result))
    history.append(r + "=" + str(result))
    history.reverse()

    dr.configure(text="HISTORY:" + "|||".join(history[0:5]), font="verdana 14 bold")


history = []


def eng():
    r = q.get()
    try:
        global result
        result = eval(r)
    except:
        print("error")
        result = "error"
    d = result ** (1 / 2)
    q.delete(0, "end")
    q.insert(0, d)
    history.append(r + "=" + str(d))
    history.reverse()

    dr.configure(text="HISTORY:" + "|||".join(history[0:5]), font="verdana 14 bold")


# ------------------------------------------canvas
d = Canvas(root, bg="white", width="700", height="500")
d.place(x=0, y=0)

# =------------------------------------------------

# developer =Label(root,text="Developed by - M.B. Sai Aditya",font=("CALIBRI",16),fg="blue").place(x=420,y=2)

# entry box----------------
q = Entry(root, width=40, bd=6, justify=RIGHT, bg="#e6e6fa")
q.insert(0, "0")
q.place(x=30, y=30)
q.config(font=("Helvetica", 22))
# number buttons--------------------------
g = Button(root, text="1", width=10, bg="#e6e6fa", command=lambda x=1: repo(x))
g.place(x=30, y=100)
g.config(font=("Helvetica", 12))

m = Button(root, text="4", width=10, bg="#e6e6fa", command=lambda x=4: repo(x))
m.place(x=30, y=160)
m.config(font=("Helvetica", 12))

n = Button(root, text="7", width=10, bg="#e6e6fa", command=lambda x=7: repo(x))
n.place(x=30, y=220)
n.config(font=("Helvetica", 12))

p = Button(root, text="2", width=10, bg="#e6e6fa", command=lambda x=2: repo(x))
p.place(x=140, y=100)
p.config(font=("Helvetica", 12))

t = Button(root, text="5", width=10, bg="#e6e6fa", command=lambda x=5: repo(x))
t.place(x=140, y=160)
t.config(font=("Helvetica", 12))

r = Button(root, text="8", width=10, bg="#e6e6fa", command=lambda x=8: repo(x))
r.place(x=140, y=220)
r.config(font=("Helvetica", 12))

e = Button(root, text="3", width=10, bg="#e6e6fa", command=lambda x=3: repo(x))
e.place(x=250, y=100)
e.config(font=("Helvetica", 12))

w = Button(root, text="6", width=10, bg="#e6e6fa", command=lambda x=6: repo(x))
w.place(x=250, y=160)
w.config(font=("Helvetica", 12))

a = Button(root, text="9", width=10, bg="#e6e6fa", command=lambda x=9: repo(x))
a.place(x=250, y=220)
a.config(font=("Helvetica", 12))

k = Button(root, text="0", width=10, bg="#e6e6fa", command=lambda x=0: repo(x))
k.place(x=30, y=280)
k.config(font=("Helvetica", 12))

k = Button(root, text="CLEAR", width=10, bg="#e6e6fa", command=dele)
k.place(x=140, y=280)
k.config(font=("verdana 20 bold", 12))

k = Button(root, text="=", width=10, bg="#e6e6fa", command=result)
k.place(x=250, y=325)
k.config(font=("verdana 20 bold", 12))

k = Button(root, text=".", width=10, bg="#e6e6fa", command=lambda x=".": repo(x))
k.place(x=140, y=325)
k.config(font=("verdana 20 bold", 12))

k = Button(root, text="BACK", width=10, bg="#e6e6fa", command=back)
k.place(x=250, y=280)
k.config(font=("verdana 20 bold", 12))
π = 22 / 7
k = Button(root, text="π", width=10, bg="#e6e6fa", command=red)
k.place(x=30, y=325)
k.config(font=("verdana 20 bold", 12))

# number buttons over---------------------------------------------
de = d.create_line(370, 90, 370, 375, fill="black", width=9)
rt = d.create_line(0, 370, 370, 370, fill="black", width=9)
re = d.create_line(0, 90, 375, 90, fill="black", width=9)
we = d.create_line(0, 90, 0, 375, fill="black", width=15)

# operator buttons-------=-=-=------------------------------------

ee = Button(root, text="+", width=8, bg="#e6e6fa", command=lambda x="+": bst(x), bd=5)
ee.place(x=400, y=100)
ee.config(font=("verdana 20 bold", 15))

ww = Button(root, text="-", width=8, bg="#e6e6fa", command=lambda x="-": bst(x), bd=5)
ww.place(x=550, y=100)
ww.config(font=("verdana 40 bold", 15))

aa = Button(root, text="*", width=8, bg="#e6e6fa", command=lambda x="*": bst(x), bd=5)
aa.place(x=400, y=160)
aa.config(font=("verdana 14 bold", 15))

kk = Button(root, text="/", width=8, bg="#e6e6fa", command=lambda x="/": bst(x), bd=5)
kk.place(x=550, y=160)
kk.config(font=("verdana 14 bold", 15))

ii = Button(root, text="√x", width=10, bg="#e6e6fa", command=eng, bd=5)
ii.place(x=450, y=220)
ii.config(font=("verdana 14 bold", 17))

ii = Button(root, text="X", width=10, bg="#e6e6fa", command=wer, bd=5)
ii.place(x=450, y=280)
ii.config(font=("verdana 14 bold", 17))

ii = Button(root, text="Clear History", width=10, bg="#e6e6fa", command=com, bd=5)
ii.place(x=590, y=340)
ii.config(font=("verdana 14 bold", 12))
# =================--------------------------------------------------------
# ==============-----------------history====--------------
dr = Label(root, text="HISTORY:", anchor=W, font="verdana 14 bold", height=5)
dr.pack(side=BOTTOM, fill=X)
we = Label(root, text="a", font="Courier", height=1, bg="#e6e6fa")
we.place(x=530, y=283)

root.mainloop()
