from tkinter import *
import math

root = Tk()
root.title("Calculator")
root.geometry('400x350')
root.configure(bg='#323232')
root.iconbitmap('icon.ico')

# row 0

inp = Entry(root, width=20, borderwidth=5, font=(
    "Helvetica", 24, "bold"), bg="black", fg="white",)
inp.grid(row=0, column=0, columnspan=5, padx=5, pady=5)


# functions

def btn_click(x):
    current = inp.get()
    inp.delete(0, END)
    inp.insert(0, str(current) + str(x))


def btn_add():
    first_number = inp.get()
    inp.delete(0, END)
    global f_num
    global operation
    operation = "addition"
    f_num = float(first_number)
    inp.delete(0, END)


def btn_sub():
    first_number = inp.get()
    global f_num
    global operation
    operation = "substraction"
    f_num = float(first_number)
    inp.delete(0, END)


def btn_mult():
    first_number = inp.get()
    global f_num
    global operation
    operation = "multiplication"
    f_num = float(first_number)
    inp.delete(0, END)


def btn_div():
    first_number = inp.get()
    global f_num
    global operation
    operation = "division"
    f_num = float(first_number)
    inp.delete(0, END)


def btn_equ():
    global operation
    second_number = inp.get()
    inp.delete(0, END)
    if operation == "addition":
        # inp.insert(0, f_num + float(second_number))
        inp.insert(0, float(f_num) + float(second_number))
    elif operation == "substraction":
        inp.insert(0, f_num - float(second_number))
    elif operation == "multiplication":
        inp.insert(0, f_num * float(second_number))
    elif operation == "division":
        try:
            inp.insert(0, f_num / float(second_number))
        except ZeroDivisionError:
            inp.insert(0, "Cannot divide by zero")
    else:
        # inp.delete(0, END)
        inp.insert(0, f_num)


def btn_ce():
    f_num == 0
    inp.delete(0, END)


def btn_c():
    inp.delete(0, END)


def btn_del():
    i = inp.get()
    t = i[:-1]
    inp.delete(0, END)
    inp.insert(0, t)


def pl_ms():
    t = inp.get()
    inp.delete(0, END)
    inp.insert(0, -float(t))


def dot():
    c = str(inp.get())
    inp.delete(0, END)
    s_n = inp.get()
    flt_num = str(c) + '.' + str(s_n)
    inp.insert(0, flt_num)


# row 1
ce = Button(root, text='CE', padx=40, pady=10,
            width=1, command=btn_ce, font=("Helvetica", 14, "bold"), bg="#202020", fg="white")
c = Button(root, text='C', padx=40, pady=10,
           width=1, command=btn_c, font=("Helvetica", 14, "bold"), bg="#202020", fg="white")
d = Button(root, text='⌫', padx=40, pady=10,
           width=1, command=btn_del, font=("Helvetica", 14, "bold"), bg="#202020", fg="white")
div = Button(root, text='÷', padx=40, pady=10,
             width=1, command=btn_div, font=("Helvetica", 14, "bold"), bg="#202020", fg="white")

ce.grid(row=1, column=0)
c.grid(row=1, column=1)
d.grid(row=1, column=2)
div.grid(row=1, column=3)


# row 2

b7 = Button(root, text='7', padx=40, pady=10,
            width=1, command=lambda: btn_click(7), font=("Helvetica", 14, "bold"), bg="black", fg="white")
b8 = Button(root, text='8', padx=40, pady=10,
            width=1, command=lambda: btn_click(8), font=("Helvetica", 14, "bold"), bg="black", fg="white")
b9 = Button(root, text='9', padx=40, pady=10,
            width=1, command=lambda: btn_click(9), font=("Helvetica", 14, "bold"), bg="black", fg="white")
x = Button(root, text='x', padx=40, pady=10,
           width=1, command=btn_mult, font=("Helvetica", 14, "bold"), bg="#202020", fg="white")

b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)
x.grid(row=2, column=3)


# row 3

b4 = Button(root, text='4', padx=40, pady=10,
            width=1, command=lambda: btn_click(4), font=("Helvetica", 14, "bold"), bg="black", fg="white")
b5 = Button(root, text='5', padx=40, pady=10,
            width=1, command=lambda: btn_click(5), font=("Helvetica", 14, "bold"), bg="black", fg="white")
b6 = Button(root, text='6', padx=40, pady=10,
            width=1, command=lambda: btn_click(6), font=("Helvetica", 14, "bold"), bg="black", fg="white")
sub = Button(root, text='-', padx=40, pady=10,
             width=1, command=btn_sub, font=("Helvetica", 14, "bold"), bg="#202020", fg="white")


b4.grid(row=3, column=0)
b5.grid(row=3, column=1)
b6.grid(row=3, column=2)
sub.grid(row=3, column=3)


# row 4

b1 = Button(root, text='1', padx=40, pady=10,
            width=1, command=lambda: btn_click(1), font=("Helvetica", 14, "bold"), bg="black", fg="white")
b2 = Button(root, text='2', padx=40, pady=10,
            width=1, command=lambda: btn_click(2), font=("Helvetica", 14, "bold"), bg="black", fg="white")
b3 = Button(root, text='3', padx=40, pady=10,
            width=1, command=lambda: btn_click(3), font=("Helvetica", 14, "bold"), bg="black", fg="white")
pls = Button(root, text='+', padx=40, pady=10,
             width=1, command=btn_add, font=("Helvetica", 14, "bold"), bg="#202020", fg="white")


b1.grid(row=4, column=0)
b2.grid(row=4, column=1)
b3.grid(row=4, column=2)
pls.grid(row=4, column=3)


# row 5

pl_ms = Button(root, text='+/-', padx=40, pady=10,
               width=1, command=pl_ms, font=("Helvetica", 14, "bold"), bg="black", fg="white")
b0 = Button(root, text='0', padx=40, pady=10,
            width=1, command=lambda: btn_click(0), font=("Helvetica", 14, "bold"), bg="black", fg="white")
dot = Button(root, text='.', padx=40, pady=10,
             width=1, command=dot, font=("Helvetica", 14, "bold"), bg="black", fg="white")
eql = Button(root, text='=', padx=40, pady=10,
             width=1, command=btn_equ, font=("Helvetica", 14, "bold"), bg="#1A7C2F", fg="white")


pl_ms.grid(row=5, column=0)
b0.grid(row=5, column=1)
dot.grid(row=5, column=2)
eql.grid(row=5, column=3)

root.mainloop()
