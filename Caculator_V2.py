from tkinter import *

# Create the main window
window = Tk()  # Initialize the main window
window.title("Calculator")  # Set the title of the window
window.geometry("1200x800")  # Set the window size

# Label for the calculator
label = Label(window, text="Calculator App", font=("Arial", 30))  # Create a label for the calculator title
label.pack()  # Place the label at the top using pack()

# Input field for the calculator
InputField = Entry(window)  # Create an entry field for user input
InputField.pack()  # Place the entry field below the title label


# Label to display the result
result_label = Label(window, text="Result: ", font=("Arial", 20))  # Create a label to display results
result_label.pack()  # Place the result label below the input field

# Function to append numbers and operators to the input field
def append_number(number):
    current_text = InputField.get()  # Get current text in the input field
    InputField.delete(0, END)  # Clear the input field
    InputField.insert(0, current_text + str(number))  # Append the new number/operator to the existing text

# Function to calculate and display the result
def calculate():
    try:
        result = eval(InputField.get())  # Evaluate the expression in the input field
        result_label.config(text="Result: " + str(result))  # Update the result label with the calculated result
    except Exception as e:
        result_label.config(text="Error")  # Display an error message if the calculation fails

# Function to clear the input field and result label
def clear():
    InputField.delete(0, END)  # Clear the input field
    result_label.config(text="Result: ")  # Reset the result label text

# Create buttons for numbers 1-9 and operators, and position them using place()
button1 = Button(window, text="1", width=5, height=2, command=lambda: append_number(1))
button1.place(x=50, y=200)
button2 = Button(window, text="2", width=5, height=2, command=lambda: append_number(2))
button2.place(x=100, y=200)
button3 = Button(window, text="3", width=5, height=2, command=lambda: append_number(3))
button3.place(x=150, y=200)
button4 = Button(window, text="4", width=5, height=2, command=lambda: append_number(4))
button4.place(x=50, y=250)
button5 = Button(window, text="5", width=5, height=2, command=lambda: append_number(5))
button5.place(x=100, y=250)
button6 = Button(window, text="6", width=5, height=2, command=lambda: append_number(6))
button6.place(x=150, y=250)
button7 = Button(window, text="7", width=5, height=2, command=lambda: append_number(7))
button7.place(x=50, y=300)
button8 = Button(window, text="8", width=5, height=2, command=lambda: append_number(8))
button8.place(x=100, y=300)
button9 = Button(window, text="9", width=5, height=2, command=lambda: append_number(9))
button9.place(x=150, y=300)

# Operator and action buttons
button_clear = Button(window, text="C", width=5, height=2, command=clear)  # Clear button
button_clear.place(x=50, y=350)
button_equals = Button(window, text="=", width=5, height=2, command=calculate)  # Equals button to calculate result
button_equals.place(x=100, y=350)

button_add = Button(window, text="+", width=5, height=2, command=lambda: append_number("+"))  # Addition button
button_add.place(x=500, y=200)
button_subtract = Button(window, text="-", width=5, height=2, command=lambda: append_number("-"))  # Subtraction button
button_subtract.place(x=550, y=200)
button_divide = Button(window, text="/", width=5, height=2, command=lambda: append_number("/"))  # Division button
button_divide.place(x=500, y=250)
button_multiply = Button(window, text="*", width=5, height=2, command=lambda: append_number("*"))  # Multiplication button
button_multiply.place(x=550, y=250)

# Start the main loop
window.mainloop()  # Start the Tkinter main event loop to run the application
