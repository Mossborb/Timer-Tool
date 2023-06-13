import tkinter as tk

def button_click():
    textField = textBox.get()
    print(textField)

window = tk.Tk()

mainGrid = tk.Frame(window)
mainGrid.grid(row=0, column= 0)

numberGrid = tk.Frame(mainGrid)
numberGrid.grid(row=1, column=0)

textBoxGrid = tk.Frame(mainGrid)
textBoxGrid.grid(row=0, column=0)

button1 = tk.Button(numberGrid, text="1", width="4", height="2")
button2 = tk.Button(numberGrid, text="2", width="4", height="2")
button3 = tk.Button(numberGrid, text="3", width="4", height="2")
button4 = tk.Button(numberGrid, text="4", width="4", height="2")
button5 = tk.Button(numberGrid, text="5", width="4", height="2")
button6 = tk.Button(numberGrid, text="6", width="4", height="2")
button7 = tk.Button(numberGrid, text="7", width="4", height="2")
button8 = tk.Button(numberGrid, text="8", width="4", height="2")
button9 = tk.Button(numberGrid, text="9", width="4", height="2")

textBox = tk.Entry(textBoxGrid)
textBox.grid(row=0, column=0)


button1.grid(row=0, column=0)
button2.grid(row=0, column=1)
button3.grid(row=0, column=2)
button4.grid(row=1, column=0)
button5.grid(row=1, column=1)
button6.grid(row=1, column=2)
button7.grid(row=2, column=0)
button8.grid(row=2, column=1)
button9.grid(row=2, column=2)


window.mainloop()