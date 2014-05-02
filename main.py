# REMEMBER - VERY IMPORTANT - Since the move to Python3, many parts of tkinter have been stupidly renamed. Case in point: tKinter is now tkinter. Getting it wrong throws an error and halts the program. I will try to update the wiki with this.
# Remember to over-comment the source code because we are Python noobs.
# Remember to use Python3.4
# Read up on how tkinter actually works
# Indent properly; it's required in Python
# I'm sure you'll at least do as well as I am, which is terribly.
# Oh god how do i orient objects iv been using c too long shit

from tkinter import * # We're not going to have any namespace conflict here. I refuse to obey good and overly-strict methodology for a program that shouldn't be more than a few thousand lines.
from tkinter import messagebox

class Application:
	def __init__(self, master):
		frame = Frame(master)
		frame.pack()

		self.quitButton = Button(
		  frame, text="Quit", command=frame.quit
		  )
		self.quitButton.pack(side=RIGHT)

		self.aboutButton = Button(
		  frame, text="Authors", command=self.aboutWindow
		  )
		self.aboutButton.pack(side=LEFT)

	def aboutWindow(self):
		messagebox.showinfo(
		  "Authors",
		  "FireproVoltron and copyright_2014 made this earth-shattering program.\nIt was a labor of love."
		  )

#Function to create the 8x8 chess board
def createBoard():
    #creates the window
    w = Canvas(master, width=198, height=198)
    w.pack()

    #Makes the whole window white to later allow for alternating black and white
    #squares
    w.create_rectangle(0, 0, 200, 200, fill="white")

    #Fills every other "square" on the board with black to make a grid.
    for x in range(0, 200, 25):
        w.create_rectangle(x, x, x + 25, x + 25, fill="black")
        w.create_rectangle(x, x + 50, x + 25, x + 75, fill="black")
        w.create_rectangle(x + 50, x, x + 75, x + 25, fill="black")
        w.create_rectangle(x + 100, x, x + 125, x + 25, fill="black")
        w.create_rectangle(x + 150, x, x + 175, x + 25, fill="black")
        w.create_rectangle(x, x + 100, x + 25, x + 125, fill="black")
        w.create_rectangle(x, x + 150, x + 25, x + 175, fill="black")

root = Tk()

app = Application(root)

root.mainloop()
root.destroy()
