import os
import sys
from misc_functions import *
from tkinter import *
from tkinter import filedialog

def new(screen, screenWidth, screenHeight, invalid=False):
    newFrame = Frame(screen, width=screenWidth, height=screenHeight)
    newFrame.pack()

    intro = Label(newFrame, text="Please enter the name of the file below:", font=("Courier", 15, "bold"), pady=100)
    cwd = Label(newFrame, text=f"Your current directory is: {os.getcwd()}", font=("Courier", 15, "bold"), pady=10)
    invalidMessage = Label(newFrame, text="That is an ivalid directory!", font=("Courier", 15, "bold"), pady=100, fg="red")

    nameInput = Entry(newFrame, font=("Courier", 12), width=50)
    name = nameInput.get()

    okButton = Button(newFrame, text="OK", width=30, bg="white", command=lambda: [newFrame.destroy(), new(screen, screenWidth, screenHeight, invalidityCheck(name))], font=("Courier", 14, "bold"))

    intro.pack()
    cwd.pack()
    nameInput.pack()
    okButton.pack()

    if invalid:
        invalidMessage.pack()

def load(screen, screenWidth, screenHeight, invalid=False):
    newFrame = Frame(screen, width=screenWidth, height=screenHeight)
    newFrame.pack()

    intro = Label(newFrame, text="Please find the file with the GUI below:", font=("Courier", 15, "bold"), pady=100)
    intro.pack()

    def openFile():
        filepath = filedialog.askopenfilename(initialdir="/saves", title="Load Your Saved Data:", filetypes=[("Where It All Goes Save Files", "*.wiag")])
        file = open(filepath)
        contents = file.readlines()
        file.close()

        for line in contents:
            print(line)

    loadButton = Button(newFrame, text="Load", width=30, bg="white", command=lambda: [openFile(), newFrame.destroy()], font=("Courier", 14, "bold"))
    loadButton.pack()

def loadOrNew(screen, screenWidth, screenHeight):
    newFrame = Frame(screen, width=screenWidth, height=screenHeight)
    newFrame.pack()

    intro = Label(newFrame, text="Would you like to use a saved file, or create a new one?", font=("Courier", 15, "bold"), pady=100)

    newButton = Button(newFrame, text="New", width=50, bg="white", command=lambda: [newFrame.destroy(), new(screen, screenWidth, screenHeight)], font=("Courier", 14, "bold"))
    loadButton = Button(newFrame, text="Load", width=50, bg="white", command=lambda: [newFrame.destroy(), load(screen, screenWidth, screenHeight)], font=("Courier", 14, "bold"))

    intro.pack()
    newButton.pack()
    loadButton.pack()