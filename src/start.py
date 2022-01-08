from load_or_new import *
from tkinter import *

def start(screen, screenWidth, screenHeight):
    startFrame = Frame(screen, width=screenWidth, height=screenHeight)
    startFrame.pack()

    intro = Label(startFrame, text="Money or Where It All Goes", font=("Courier", 25, "bold"), pady=100)

    startButton = Button(startFrame, text="Start", width=50, bg="green", command=lambda: [startFrame.destroy(), loadOrNew(screen, screenWidth, screenHeight)], font=("Courier", 14, "bold"))
    endButton = Button(startFrame, text="Exit", width=50, bg="red", command=exit, font=("Courier", 14, "bold"))

    intro.pack()
    startButton.pack()
    endButton.pack()
