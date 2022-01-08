import os
import sys
from start import *
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

start(screen, screenWidth, screenHeight)

screen.mainloop()
