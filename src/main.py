import os
import sys
from tkinter import *

screenWidth = 800
screenHeight = 500

screen = Tk()

monitorWidth = screen.winfo_screenwidth()
monitorHeight = screen.winfo_screenheight()

xLeft = int((monitorWidth/2) - (screenWidth/2))
yTop = int((monitorHeight/2) - (screenHeight/2))

screen.title("Where It All Goes")
screen.geometry(f"{screenWidth}x{screenHeight}+{xLeft}+{yTop}")

startFrame = Frame(screen, width=screenWidth, height=screenHeight)
startFrame.pack()

def exit():
    sys.exit(1)

def invalidityCheck(directory):
    if os.access(directory, os.R_OK):
        return False
    else:
        return True

def new(invalid=False):
    newFrame = Frame(screen, width=screenWidth, height=screenHeight)
    newFrame.pack()

    intro = Label(newFrame, text="Please enter the directory of the file below:", font=("Courier", 15, "bold"), pady=100)
    invalidMessage = Label(newFrame, text="That is an ivalid directory!", font=("Courier", 15, "bold"), pady=100, fg="red")

    nameInput = Entry(newFrame, font=("Courier", 12), width=50)
    directory = nameInput.get()

    okButton = Button(newFrame, text="OK", width=30, bg="white", command=lambda: [newFrame.destroy(), new(invalidityCheck(directory))], font=("Courier", 14, "bold"))

    intro.pack()
    nameInput.pack()
    okButton.pack()

    if invalid:
        invalidMessage.pack()

def load(invalid=False):
    newFrame = Frame(screen, width=screenWidth, height=screenHeight)
    newFrame.pack()

    intro = Label(newFrame, text="Please enter the directory and name of the file below:", font=("Courier", 15, "bold"), pady=100)
    invalidMessage = Label(newFrame, text="That is an ivalid directory!", font=("Courier", 15, "bold"), pady=100, fg="red")

    nameInput = Entry(newFrame, font=("Courier", 12), width=50)
    directory = nameInput.get()

    okButton = Button(newFrame, text="OK", width=30, bg="white", command=lambda: [newFrame.destroy(), load(invalidityCheck(directory))], font=("Courier", 14, "bold"))

    intro.pack()
    nameInput.pack()
    okButton.pack()

    if invalid:
        invalidMessage.pack()

def loadOrNew():
    newFrame = Frame(screen, width=screenWidth, height=screenHeight)
    newFrame.pack()

    intro = Label(newFrame, text="Would you like to use a saved file, or create a new one?", font=("Courier", 15, "bold"), pady=100)

    newButton = Button(newFrame, text="New", width=50, bg="white", command=lambda: [newFrame.destroy(), new()], font=("Courier", 14, "bold"))
    loadButton = Button(newFrame, text="Load", width=50, bg="white", command=lambda: [newFrame.destroy(), load()], font=("Courier", 14, "bold"))

    intro.pack()
    newButton.pack()
    loadButton.pack()

def start():
    intro = Label(startFrame, text="Money or Where It All Goes", font=("Courier", 25, "bold"), pady=100)

    startButton = Button(startFrame, text="Start", width=50, bg="green", command=lambda: [startFrame.destroy(), loadOrNew()], font=("Courier", 14, "bold"))
    endButton = Button(startFrame, text="Exit", width=50, bg="red", command=exit, font=("Courier", 14, "bold"))

    intro.pack()
    startButton.pack()
    endButton.pack()

start()

screen.mainloop()
