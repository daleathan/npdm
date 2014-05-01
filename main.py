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

root = Tk()

app = Application(root)

root.mainloop()
root.destroy()
