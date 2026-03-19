import tkinter as tk
from tkinter import messagebox

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        
        tk.Label(root, text="Username:").grid(row=0, column=0, padx=10, pady=10)
        self.username_entry = tk.Entry(root)
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)
        
        tk.Label(root, text="Password:").grid(row=1, column=0, padx=10, pady=10)
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)
        
        self.login_btn = tk.Button(root, text="Login", command=self.login)
        self.login_btn.grid(row=2, column=0, columnspan=2, pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if not username or not password:
            messagebox.showerror("Error", "Username or password cannot be empty.")
        elif username == "admin" and password == "password": # Dummy credentials
            messagebox.showinfo("Success", "Login Successful")
        else:
            messagebox.showerror("Error", "Invalid credentials")

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
