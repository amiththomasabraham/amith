import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        
        tk.Label(root, text="Number 1:").grid(row=0, column=0, padx=10, pady=10)
        self.num1_entry = tk.Entry(root)
        self.num1_entry.grid(row=0, column=1, padx=10, pady=10, columnspan=3)
        
        tk.Label(root, text="Number 2:").grid(row=1, column=0, padx=10, pady=10)
        self.num2_entry = tk.Entry(root)
        self.num2_entry.grid(row=1, column=1, padx=10, pady=10, columnspan=3)
        
        tk.Label(root, text="Result:").grid(row=2, column=0, padx=10, pady=10)
        self.result_var = tk.StringVar()
        self.result_entry = tk.Entry(root, textvariable=self.result_var, state='readonly')
        self.result_entry.grid(row=2, column=1, padx=10, pady=10, columnspan=3)
        
        tk.Button(root, text="Add", command=lambda: self.calculate("add")).grid(row=3, column=0, pady=10)
        tk.Button(root, text="Subtract", command=lambda: self.calculate("sub")).grid(row=3, column=1, pady=10)
        tk.Button(root, text="Multiply", command=lambda: self.calculate("mul")).grid(row=3, column=2, pady=10)
        tk.Button(root, text="Divide", command=lambda: self.calculate("div")).grid(row=3, column=3, pady=10)

    def calculate(self, operation):
        try:
            num1 = int(self.num1_entry.get())
            num2 = int(self.num2_entry.get())
            
            if operation == "add":
                res = num1 + num2
            elif operation == "sub":
                res = num1 - num2
            elif operation == "mul":
                res = num1 * num2
            elif operation == "div":
                if num2 == 0:
                    raise ZeroDivisionError
                res = num1 / num2
                
            self.result_var.set(str(res))
        except ValueError:
            messagebox.showerror("Error", "Please enter valid integers.")
        except ZeroDivisionError:
            messagebox.showerror("Error", "Division by zero is not allowed.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
