import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        root.title("Simple Calculator")

        self.result_var = tk.StringVar()

        self.entry = tk.Entry(root, textvariable=self.result_var, font=('Helvetica', 16), bd=10, insertwidth=2, width=20, justify='right')
        self.entry.grid(row=0, column=0, columnspan=4)

        button_texts = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        self.buttons = []

        row_val = 1
        col_val = 0

        for btn_text in button_texts:
            self.buttons.append(tk.Button(root, text=btn_text, font=('Helvetica', 14), 
                        padx=20, pady=20, command=lambda txt=btn_text: self.button_click(txt)))
            self.buttons[-1].grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def button_click(self, text):
        if text == '=':
            try:
                result = str(eval(self.result_var.get()))
                self.result_var.set(result)
            except:
                self.result_var.set('Error')
        elif text == 'C':
            self.result_var.set('')
        else:
            self.result_var.set(self.result_var.get() + text)

if __name__ == '__main__':
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
