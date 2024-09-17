import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        
        self.display = tk.Entry(root, borderwidth=2, relief="solid", font=("Arial", 18), justify="right")
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        
        self.buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', '=', '+'
        ]
        self.create_buttons()
    
    def create_buttons(self):
        row_val = 1
        col_val = 0
        for button in self.buttons:
            tk.Button(self.root, text=button, width=5, height=2, font=("Arial", 18),
                      command=lambda btn=button: self.on_button_click(btn)).grid(row=row_val, column=col_val, padx=5, pady=5)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1
    
    def on_button_click(self, button):
        current_text = self.display.get()
        
        if button == 'C':
            self.display.delete(0, tk.END)
        elif button == '=':
            try:
                result = eval(current_text)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        else:
            self.display.insert(tk.END, button)

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()
