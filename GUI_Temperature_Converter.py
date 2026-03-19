import tkinter as tk
from tkinter import messagebox

class TemperatureConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Temperature Converter")
        
        tk.Label(root, text="Celsius:").grid(row=0, column=0, padx=10, pady=10)
        self.celsius_entry = tk.Entry(root)
        self.celsius_entry.grid(row=0, column=1, padx=10, pady=10)
        
        tk.Label(root, text="Fahrenheit:").grid(row=1, column=0, padx=10, pady=10)
        self.fahrenheit_var = tk.StringVar()
        self.fahrenheit_entry = tk.Entry(root, textvariable=self.fahrenheit_var, state='readonly')
        self.fahrenheit_entry.grid(row=1, column=1, padx=10, pady=10)
        
        self.convert_btn = tk.Button(root, text="Convert to Fahrenheit", command=self.convert)
        self.convert_btn.grid(row=2, column=0, columnspan=2, pady=10)

    def convert(self):
        try:
            celsius = float(self.celsius_entry.get())
            fahrenheit = (celsius * 9/5) + 32
            self.fahrenheit_var.set(f"{fahrenheit:.2f}")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid numeric temperature.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TemperatureConverterApp(root)
    root.mainloop()
