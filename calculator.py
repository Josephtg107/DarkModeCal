import tkinter as tk

def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

def toggle_dark_mode():
    global is_dark_mode
    is_dark_mode = not is_dark_mode
    if is_dark_mode:
        root.configure(bg="#1C1C1E")
        entry.configure(bg="#2C2C2E", fg="#FFFFFF")
        dark_mode_btn.configure(bg="#34C759", text="Light Mode", width=8)
        update_button_colors(dark=True)
    else:
        root.configure(bg="#F2F2F7")
        entry.configure(bg="#E5E5EA", fg="#000000")
        dark_mode_btn.configure(bg="#FF9500", text="Dark Mode", width=8)
        update_button_colors(dark=False)


def update_button_colors(dark=False):
    button_bg = "#FFFFFF" if not dark else "#3A3A3C"
    operator_bg = "#FF9500" if not dark else "#FF9F0A"
    equal_bg = "#34C759" if not dark else "#30D158"
    clear_bg = "#FF3B30" if not dark else "#FF453A"

    for b in buttons:
        color = button_bg if b['text'].isdigit() or b['text'] == '0' else operator_bg
        if b['text'] == "=":
            color = equal_bg
        elif b['text'] == "C":
            color = clear_bg
        b.configure(bg=color)

root = tk.Tk()
root.title("DarkMode Calc")
root.geometry("350x540") 
is_dark_mode = False  

entry = tk.Entry(root, font="Arial 24", bd=0, relief=tk.FLAT, justify=tk.RIGHT, bg="#E5E5EA", fg="#000000")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20, ipady=15)

button_texts = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

buttons = [] 

def create_circle_button(root, text, row, col):
    b = tk.Button(root, text=text, font="Arial 18", padx=10, pady=10, width=4, height=2, bg="#FFFFFF", fg="black", bd=0, 
                  relief=tk.FLAT, highlightthickness=0, activebackground="#FFFFFF", activeforeground="white")
    b.grid(row=row, column=col, padx=10, pady=10, ipadx=15, ipady=15, sticky="nsew")
    buttons.append(b) 
    b.bind("<Button-1>", on_click)
    return b

row_val = 1
col_val = 0
for button_text in button_texts:
    create_circle_button(root, button_text, row_val, col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

dark_mode_btn = tk.Button(root, text="Dark Mode", font="Arial 14", padx=10, pady=10, bg="#FF9500", fg="white", bd=0, 
                          relief=tk.FLAT, command=toggle_dark_mode, width=8)
dark_mode_btn.grid(row=6, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)


for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(6):
    root.grid_rowconfigure(i, weight=1)

root.mainloop()
