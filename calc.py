from tkinter import *
import numpy as np

def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                print(e)
                value = "Syntax Error"
        scvalue.set(value)
        screen.update()
    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()


root = Tk()
root.geometry("600x900")
root.title("Calculater by Pradnya")
# root.wm_iconbitmap(".ico")                      icon
scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 30 bold")
screen.grid(row=0, ipadx=20, padx=20, pady=28)

arr1 = np.array([["0", "0", "0", "0","0"],
                 ["0", "9", "8", "7", "6"],
                 ["0", "5", "4", "3", "2"],
                 ["0", "1", "0", "-", "*"],
                 ["0", ".", "/", "C", "="]])

f1 = Frame(root, bg="grey")
for i in range(1,5):
    for j in range(1,5):
        b = Button(f1, text=arr1[i][j], padx=28, pady=18, font="lucida 25 bold")
        b.grid(row=i, column=j, padx=10, pady=10)
        b.bind("<Button-1>", click)
f1.grid()
root.mainloop()