import tkinter as tk
def press(key):
    entry_text.set(entry_text.get() + str(key))

def clear():
    entry_text.set("")

def equal():
    try:
        result = str(eval(entry_text.get()))
        entry_text.set(result)
    except:
        entry_text.set("Error")
def percentage():
    try:
        current_value = float(entry_text.get())
        entry_text.set(current_value / 100)
    except:
        entry_text.set("Error")
def reciprocal():
    try:
        current_value = float(entry_text.get())
        entry_text.set(1 / current_value)
    except:
        entry_text.set("Error")
def square():
    try:
        current_value = float(entry_text.get())
        entry_text.set(current_value ** 2)
    except:
        entry_text.set("Error")
def sqrt():
    try:
        current_value = float(entry_text.get())
        entry_text.set(current_value ** 0.5)
    except:
        entry_text.set("Error")

# Function for toggle sign (+/-)
def toggle_sign():
    try:
        current_value = float(entry_text.get())
        entry_text.set(-current_value)
    except:
        entry_text.set("Error")

root = tk.Tk()
root.title("Calculator")
root.geometry("350x500")
root.resizable(True, True)
root.configure(bg="black")

entry_text = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_text, font=('Arial', 24), bd=10, insertwidth=2, width=14, borderwidth=4, justify='right', bg='black', fg='white')
entry.grid(row=0, column=0, columnspan=4, pady=20, sticky="nsew")

buttons = [
    ['%', 'CE', 'C', '⌫'],
    ['1/x', 'x²', '√x', '/'],
    ['7', '8', '9', '*'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '+'],
    ['+/-', '0', '.', '=']
]


for i, row in enumerate(buttons):
    for j, btn in enumerate(row):
        if btn == '%':
            action = percentage
        elif btn == '1/x':
            action = reciprocal
        elif btn == 'x²':
            action = square
        elif btn == '√x':
            action = sqrt
        elif btn == '+/-':
            action = toggle_sign
        else:
            action = lambda x=btn: press(x) if x not in ['C', '⌫', '='] else (
                clear() if x == 'C' else entry_text.set(entry_text.get()[:-1]) if x == '⌫' else equal()
            )
        
        tk.Button(root, text=btn, padx=20, pady=20, font=('Arial', 14),
                  command=action, bg='#323232' if btn != '=' else '#00bfff',
                  fg='white' if btn != '=' else 'black', relief='flat').grid(row=i+1, column=j, sticky="nsew", padx=1, pady=1)

for i in range(1, 7):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
