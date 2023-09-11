import tkinter as tk

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == "Addition":
            result.set(num1 + num2)
        elif operation == "Subtraction":
            result.set(num1 - num2)
        elif operation == "Multiplication":
            result.set(num1 * num2)
        elif operation == "Division":
            if num2 == 0:
                result.set("Error: Division by zero")
            else:
                result.set(num1 / num2)
    except ValueError:
        result.set("Error: Invalid input")

root = tk.Tk()
root.title("Simple Calculator")

label_num1 = tk.Label(root, text="Enter first number:")
label_num1.pack()
entry_num1 = tk.Entry(root)
entry_num1.pack()
label_num2 = tk.Label(root, text="Enter second number:")
label_num2.pack()
entry_num2 = tk.Entry(root)
entry_num2.pack()

operation_var = tk.StringVar()
operation_var.set("Addition")
label_operation = tk.Label(root, text="Select operation:")
label_operation.pack()
operation_menu = tk.OptionMenu(root, operation_var, "Addition", "Subtraction", "Multiplication", "Division")
operation_menu.pack()

calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack()

result = tk.StringVar()
result.set("Result will be shown here")
label_result = tk.Label(root, textvariable=result)
label_result.pack()

root.mainloop()
