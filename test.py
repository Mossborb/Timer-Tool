import tkinter as tk

def show_button_text():
    text = button.cget("text")
    entry.delete(0, tk.END)
    entry.insert(tk.END, text)

window = tk.Tk()

# Create the button
button = tk.Button(window, text="Click Me", command=show_button_text)
button.pack()

# Create the entry widget
entry = tk.Entry(window)
entry.pack()

window.mainloop()