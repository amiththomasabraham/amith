import tkinter as tk
import string

class PasswordStrengthApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Strength Checker")
        
        tk.Label(root, text="Password:").grid(row=0, column=0, padx=10, pady=10)
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.grid(row=0, column=1, padx=10, pady=10)
        
        self.check_btn = tk.Button(root, text="Check Strength", command=self.check_strength)
        self.check_btn.grid(row=1, column=0, columnspan=2, pady=10)
        
        tk.Label(root, text="Strength:").grid(row=2, column=0, padx=10, pady=10)
        self.strength_var = tk.StringVar()
        self.strength_label = tk.Label(root, textvariable=self.strength_var, font=("Arial", 12, "bold"))
        self.strength_label.grid(row=2, column=1, padx=10, pady=10)

    def check_strength(self):
        pwd = self.password_entry.get()
        
        has_len = len(pwd) >= 8
        has_digit = any(char.isdigit() for char in pwd)
        has_special = any(char in string.punctuation for char in pwd)
        
        score = sum([has_len, has_digit, has_special])
        
        if score == 3:
            self.strength_var.set("Strong")
            self.strength_label.config(fg="green")
        elif score == 2:
            self.strength_var.set("Moderate")
            self.strength_label.config(fg="orange")
        else:
            self.strength_var.set("Weak")
            self.strength_label.config(fg="red")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordStrengthApp(root)
    root.mainloop()
