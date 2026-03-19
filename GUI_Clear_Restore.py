import tkinter as tk

class ClearRestoreApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Clear and Restore Demo")
        
        self.original_text = "Python GUI Demo"
        
        self.label = tk.Label(root, text=self.original_text, font=("Arial", 16))
        self.label.pack(pady=20)
        
        self.clear_btn = tk.Button(root, text="Clear", command=self.clear_action)
        self.clear_btn.pack(side=tk.LEFT, padx=20, pady=10)
        
        self.restore_btn = tk.Button(root, text="Restore", state=tk.DISABLED, command=self.restore_action)
        self.restore_btn.pack(side=tk.RIGHT, padx=20, pady=10)
        
    def clear_action(self):
        self.label.config(text="")
        self.clear_btn.config(state=tk.DISABLED)
        self.restore_btn.config(state=tk.NORMAL)
        
    def restore_action(self):
        self.label.config(text=self.original_text)
        self.clear_btn.config(state=tk.NORMAL)
        self.restore_btn.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = ClearRestoreApp(root)
    root.mainloop()
