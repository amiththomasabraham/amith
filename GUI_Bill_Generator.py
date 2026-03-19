import tkinter as tk
from tkinter import messagebox

class BillGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bill Generator")
        
        tk.Label(root, text="Item Price:").grid(row=0, column=0, padx=10, pady=10)
        self.price_entry = tk.Entry(root)
        self.price_entry.grid(row=0, column=1, padx=10, pady=10)
        
        tk.Label(root, text="Quantity:").grid(row=1, column=0, padx=10, pady=10)
        self.quantity_entry = tk.Entry(root)
        self.quantity_entry.grid(row=1, column=1, padx=10, pady=10)
        
        self.generate_btn = tk.Button(root, text="Generate Bill", command=self.generate_bill)
        self.generate_btn.grid(row=2, column=0, columnspan=2, pady=10)
        
        tk.Label(root, text="Final Amount:").grid(row=3, column=0, padx=10, pady=10)
        self.amount_var = tk.StringVar()
        self.amount_entry = tk.Entry(root, textvariable=self.amount_var, state='readonly')
        self.amount_entry.grid(row=3, column=1, padx=10, pady=10)

    def generate_bill(self):
        try:
            price = float(self.price_entry.get())
            quantity = int(self.quantity_entry.get())
            
            if price < 0 or quantity < 0:
                raise ValueError("Values cannot be negative")
                
            total = price * quantity
            
            if total > 1000:
                total *= 0.90 # 10% discount
                messagebox.showinfo("Discount Applied", "A 10% discount has been applied!")
                
            self.amount_var.set(f"{total:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric values for price and quantity.")

if __name__ == "__main__":
    root = tk.Tk()
    app = BillGeneratorApp(root)
    root.mainloop()
