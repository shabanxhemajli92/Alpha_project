import tkinter as tk
from tkinter import filedialog,Text
import os

root=tk.Tk()
apps=[]

def addApp():
    for widget in frame.winfo_children():
        widget.destroy()
    filename=filedialog.askopenfilename(initialdir="/",title="Select file",
    filetypes=(("executables" , "*.exe"),("all files","*.*")))
    apps.append(filename)
    print(filename)
    for app in apps:
        label=tk.Label(frame,text=app,bg="gray")
        label.pack()
def runApps():
    for app in apps:
        os.startfile(app)
canvas=tk.Canvas(root,height=500,width=700,bg="#163D42")
canvas.pack()
frame=tk.Frame(root,bg="orange")
frame.place(relwidth=0.8,height=0.8,relx=0.1,rely=0.1)
openFile=tk.Button(root,text="Open",padx=10,pady=5,fg="white",bg="#163D42",command=addApp)
openFile.pack()
Runnapps=tk.Button(root,text="Run",padx=10,pady=5,fg="white",bg="#163D42",command=runApps)
Runnapps.pack()

root.mainloop()
