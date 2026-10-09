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

Operations = {
     "Add (+)": add,
     "Subtract (-)": subtract,
     "Multiply (*)": multiply,
     "Divide (/)": divide,
     "Square (x^2)": square,
     "Power (x^y)": power,
}

# This handles events

def calculate (*args):
     func = Operations[operation.get()]

     try:
          x = float(num1.get())
          if func is square:
               answer = func(x)
          else:
               y = float(num2.get())
               answer = func(x,y)
     except ValueError:
          result.set("Please enter numeric values.")
          return
     except OverflowError:
          result.set("Result is too large.")
          return
     result.set(answer)

def on_operation_change(*args):
     if Operations[operation.get()] is square:
          num2_entry.state(["!disabled"])

# Setting up window

root = Tk()
root.title("Calculator")

mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

# This allows the frame to stretch if window is resized

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
mainframe.columnconfigure(2, weight=1)

# Row 1 = First number

ttk.Label(mainframe, text="First number").grid(column=1, row=1, sticky=W)

num1 = StringVar()
num1_entry = ttk.Entry(mainframe, width=7, textvariable=num1)
num1_entry.grid(column=2, row=1, sticky=(W, E))

# Row 2 = Combo box for operations

ttk.Label(mainframe, text="Operation").grid(column=1, row=2, sticky=W)

operation = StringVar()
operation_box = ttk.Combobox(
     mainframe,
     textvariable=operation,
     values=list(Operations.keys()),
     state="readonly" # This makes it so user can only pick from the list, and not type
)

operation_box.grid(column=2, row=2, sticky=(W, E))
operation_box.current(0) # Start on the first item ("Add (+)")
operation_box.bind("<<ComboboxSelected>>", on_operation_change)

# Row 3 = Second number
ttk.Label(mainframe, text="Second number").grid(column=1, row=3, sticky=W)

num2 = StringVar()
num2_entry = ttk.Entry(mainframe, width=7, textvariable=num2)
num2_entry.grid(column=2, row=3, sticky=(W, E))

# Row 4 = Calculate button
ttk.Button(mainframe, text="Calculate").grid(column=2, row=4, sticky=W)

# Row 5 = Result
ttk.Label(mainframe, text="Result").grid(column=1, row=5, sticky=W)

result = StringVar()
ttk.Label(mainframe, textvariable=result).grid(column=2, row=5, sticky=(W, E))

# This adds a little space around every widget in the frame
for child in mainframe.winfo_children():
     child.grid_configure(padx=5, pady=5)

num1_entry.focus() # Cursor starts in the first box
root.bind("<Return>", calculate) # Allows for calculation by pressing enter

# Starts the event loop
root.mainloop()