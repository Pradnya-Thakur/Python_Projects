from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)           # dekete from 1st line 0th char to end
def openFile():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + "- Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close
def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                                 filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")] )
        if file=="":
            file = None
        else:
            f=open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()
            root.title(os.path.basename(file) + "- Notepad")
            print("Saved")
    else:
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()
def quitApp():
    root.destroy()
def cut():
    TextArea.event_generate(("<<Cut>>"))
def copy():
    TextArea.event_generate(("<<Copy>>"))
def paste():
    TextArea.event_generate(("<<Paste>>"))
def about():
    showinfo("Notepad", "Notepad by Pradnya", )

if __name__ == '__main__':
    root = Tk()
    root.title("Untitled-Notepad")
    # root.wm_iconbitmap("1.ico")
    root.geometry("600x400")

    # text area
    TextArea = Text(root, font="comicsansns 20")
    file = None
    TextArea.pack(expand=True, fill=BOTH)
    Menubar = Menu(root)
    FileMenu = Menu(Menubar, tearoff=0)
    FileMenu.add_command(label="New", command=newFile)
    FileMenu.add_command(label="open", command=openFile)
    FileMenu.add_command(label="Save", command=saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit", command=quitApp)
    Menubar.add_cascade(label="File", menu=FileMenu)

    EditMenu = Menu(Menubar, tearoff=0)
    EditMenu.add_command(label="Cut", command=cut)
    EditMenu.add_command(label="Copy", command=copy)
    EditMenu.add_command(label="Paste", command=paste)
    Menubar.add_cascade(label="Edit", menu=EditMenu)

    HelpMenu = Menu(Menubar, tearoff=0)
    HelpMenu.add_command(label="About Notepad", command=about)
    Menubar.add_cascade(label="Help", menu=HelpMenu)
    root.config(menu=Menubar)

    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT, fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)

    root.mainloop()