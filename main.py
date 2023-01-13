from tkinter import *

root = Tk()
root.title("Calculator")

# Functions

def buttonCLICK(int):
    prev = mainEntry.get()
    mainEntry.delete(0, END)
    mainEntry.insert(0, str(prev) + str(int))

def clearENRTY():
    mainEntry.delete(0, END)

def addition():
    global current_number
    global current_function
    current_function = "add"
    current_number = mainEntry.get()
    int(current_number)
    mainEntry.delete(0, END)

def subtraction():
    global current_number
    global current_function
    current_function = "sub"
    current_number = mainEntry.get()
    int(current_number)
    mainEntry.delete(0, END)

def multiplication():
    global current_number
    global current_function
    current_function = "mult"
    current_number = mainEntry.get()
    int(current_number)
    mainEntry.delete(0, END)

def division():
    global current_number
    global current_function
    current_function = "div"
    current_number = mainEntry.get()
    int(current_number)
    mainEntry.delete(0, END)

def equals():
    total = 0
    new_current_number = mainEntry.get()
    mainEntry.delete(0, END)
    if(current_function == "add"):
        total = int(current_number) + int(new_current_number)
    elif(current_function == "sub"):
        total = int(current_number) - int(new_current_number)
    elif(current_function == "mult"):
        total = int(current_number) * int(new_current_number)
    elif(current_function == "div"):
        total = int(current_number) / int(new_current_number)
    else:
        return
    mainEntry.insert(0, str(total))




# Grid System
mainEntry = Entry(root, width = 50, borderwidth= 5, justify='right', )
mainEntry.grid(row = 0, column=0, columnspan= 4)

# Defining buttons

# NUMBERS
button1 = Button(root, text="1", padx = 40, pady = 20, command= lambda: buttonCLICK(1)).grid(row = 3, column= 0)
button2 = Button(root, text="2", padx = 40, pady = 20, command= lambda: buttonCLICK(2)).grid(row = 3, column= 1)
button3 = Button(root, text="3", padx = 40, pady = 20, command= lambda: buttonCLICK(3)).grid(row = 3, column= 2)
button4 = Button(root, text="4", padx = 40, pady = 20, command= lambda: buttonCLICK(4)).grid(row = 2, column= 0)
button5 = Button(root, text="5", padx = 40, pady = 20, command= lambda: buttonCLICK(5)).grid(row = 2, column= 1)
button6 = Button(root, text="6", padx = 40, pady = 20, command= lambda: buttonCLICK(6)).grid(row = 2, column= 2)
button7 = Button(root, text="7", padx = 40, pady = 20, command= lambda: buttonCLICK(7)).grid(row = 1, column= 0)
button8 = Button(root, text="8", padx = 40, pady = 20, command= lambda: buttonCLICK(8)).grid(row = 1, column= 1)
button9 = Button(root, text="9", padx = 40, pady = 20, command= lambda: buttonCLICK(9)).grid(row = 1, column= 2)
button0 = Button(root, text="0", padx = 40, pady = 20, command= lambda: buttonCLICK(0)).grid(row = 4, column= 1)

# BASIC FUNCTIONS
button_clear = Button(root, text="CLR", padx = 33, pady = 20, command= clearENRTY).grid(row = 4, column= 0)
button_equal = Button(root, text="=", padx = 40, pady = 20, command = equals).grid(row = 4, column= 2)

# ALGEBRA
button_addition = Button(root, text="+", padx = 40, pady = 20, command= addition).grid(row=1, column=3)
button_subtraction = Button(root, text="-", padx = 40, pady = 20, command= subtraction).grid(row=2, column=3)
button_multiplication = Button(root, text="x", padx = 40, pady = 20, command= multiplication).grid(row=3, column=3)
button_division = Button(root, text="/", padx = 40, pady = 20, command= division).grid(row=4, column=3)


# EVENT LOOP
root.mainloop()