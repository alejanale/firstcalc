# importing tkinter
from tkinter import *
from tkinter import ttk

# this function adds 2 numbers
def add(x, y):
    return x + y

# this function subtracts 2 numbers
def subtract(x, y):
    return x - y

# this function multiplies 2 numbers
def multiply(x, y):
    return x * y

# this function divides 2 numbers
def divide(x, y):
    return x / y

# This function squares a number
def square(x):
      return x ** 2      

# This function multiplies to the power of
def power(x, y):
      return x ** y

root=Tk()

root.title("Calculator")

mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

num1 = StringVar()
num1_entry = ttk.Entry(mainframe, width=7, textvariable=num1)
num1_entry.grid(column=2, row=1, sticky=(W, E))

num2 = StringVar()
num2_entry = ttk.Entry(mainframe, width=7, textvariable=num2)
num2_entry.grid(column=2, row=2, sticky=(W, E))

answer = StringVar()
answer.Label(mainframe, textvariable=answer).grid(column=3, row=3, sticky=(W, E))

ttk.Button(mainframe, text="Calculate", command=answer).grid(column=3, row=3, sticky=W)

ttk.Combobox['values'] = ('Add', 'Subtract', 'Multiply', 'Divide', 'Square', 'Power')
