from tkinter import *
from tkinter import filedialog, Text
import os

root = Tk()

apps = []

def addApp():

    for widget in frame.winfo_children():
        widget.destroy()
        
    filename = filedialog.askopenfilename(initialdir="/",title="Select A File",
                                          filetypes=(("executables","*.exe"),("all files", "*.*")))

    apps.append(filename)
    # print(filename)
    for app in apps:
        label = Label(frame, text = app, bg="gray")
        label.pack()
def runApps():
    for app in apps:
        os.startfile(app)
        
canvas = Canvas(root,bg="#263D42")
canvas.pack(fill="both", expand=True)

frame = Frame(root, bg="blue")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = Button(root, text="Open File", padx=10,
                  pady=5, fg="white", bg="#263D42" , command=addApp)

openFile.pack()

runApps = Button(root, text="Run Apps", padx=10,
                  pady=5, fg="white", bg="#263D42",command=runApps)

runApps.pack()

root.mainloop()
