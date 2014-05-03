#!/usr/bin/python3.4
#<-- README
# The first comment line allows UNIX/Linux shells to start the program without the user explicitly invoking Python.
# For TCL/tk colors, see: http://wiki.tcl.tk/16166
# These bitmaps are too large; we must resize them!
#<-- If you're using vim or gvim,
# you'll be less pissed with:
#   :syntax on
#   :set number
#   :set foldmethod=marker     ]_
#   :set foldmarker=#<--,#-->  ]  These combined fold the text sections as defined by the style guide. You'll love it!
#   :set autoindent 
#   :set formatoptions+=rt
#   :set textwidth=120 
#   :help - Displays vim help
#   :help "option" - Explains any of the options above, like formatoptions
#   zM - Closes all folds.
#   zo - Closes the fold at the cursor.
#   zc - Closes the fold at the cursor.
#   za - Toggles folding at the cursor.
# Does vim say "recording" at the bottom-left? You accidentally hit "q" and another key, which makes it record key strokes so you can
# automate sequences of commands and store it to a buffer unique to that key. Press "q" again to turn it of.
# You can enter the above options in your vimrc file (usually /etc/vimrc) so you don't have to type them everytime you
# start vim.
# A fantastic plugin for vim is supertab. I use supertab because I like long variable and function names.
#-->
# I made a style guide at https://github.com/alexanderkjackson/npdm/wiki/Style-guide. I was hoping you'd like it,
#   but it is very thorough and you don't have to use it at all. If you have suggestions that would make it better,
#   add them to the page so I can use them.
# If I make any changes you find disagreeable/stupid/hard-to-use, let me know and revert them if you want.
# I'll try to keep things organized and easy to use.
# The imports use '*', which is dangerous in large software projects because of namespace conflicts. That's
# unlikely to happen here.
#-->
#<-- History class - TODO: NYI: Will be a simple linked list storing moves in chess notation
class History:
   def undo(self):
      print("history.undo: Not yet implemented")
   def redo(self):
      print("history.redo: Not yet implemented")
   def __init__(self):
      print("history.__init__: Not yet implemented")
   def __del__(self):
      print("history.__del__: Not yet implemented")
#-->
#<-- Preferences class - TODO: NYI: A collection of preferences and a GUI to configure them
class Preferences:
   def config_window(self):
      window = Toplevel()
      window.title("Preferences")

      message = Message(window, text="config_window: Not yet implemented, of course")
      message.pack()

      button = Button(window, text="Close", command=window.destroy)
      button.pack()

   def __init__(self):
      self.difficulty = 0
   def __del__(self):
      print("Preferences.__del__: Not yet implemented")
#-->
#<-- Application class - TODO: Resize bitmaps, find the center of squares, place pieces to set the board.
class Application:
#<-- help_window
   def help_window(self):
      messagebox.showinfo(
        "Help",
	"I am error."
	)
#-->
#<-- show_authors
   def show_authors(self):
      messagebox.showinfo(
        "Authors",
        "froman44 and copyright_2014 made this earth-shattering program to fill the void." 
        ) # TODO: I have an incredibly strong desire to put a function here to construct a dependent clause using Google
	  # each time it is called.
#-->
#<-- Chess board constructor SHOULD: This be moved to its own class and given its own interface?
   def createBoard(self,master):
# Creates the canvas on which we render the chessboard.
      self.canvas = Canvas(master, width=198, height=198)

# Draws a "white" rectangle in the canvas.
      self.canvas.create_rectangle(0, 0, 200, 200, fill="deep sky blue")
#<-- Fills every other "square" on the board with "black" to make a grid. Colors changed for visibility of pieces.
      for x in range(0, 200, 25): 
        self.canvas.create_rectangle(x, x, x + 25, x + 25, fill="sienna")
        self.canvas.create_rectangle(x, x + 50, x + 25, x + 75, fill="sienna")
        self.canvas.create_rectangle(x + 50, x, x + 75, x + 25, fill="sienna")
        self.canvas.create_rectangle(x + 100, x, x + 125, x + 25, fill="sienna")
        self.canvas.create_rectangle(x + 150, x, x + 175, x + 25, fill="sienna")
        self.canvas.create_rectangle(x, x + 100, x + 25, x + 125, fill="sienna")
        self.canvas.create_rectangle(x, x + 150, x + 25, x + 175, fill="sienna")
#--> 
#<-- TODO: NYI: Load all bitmaps to the appropriate name. It is also important to have a function that quickly and
     # easily will find the center of a square. I have no idea how to resize these bitmaps, though.
      self.white_queen = BitmapImage(file="./bitmaps/q95o.bm",foreground="black")
      self.image = self.canvas.create_image(100,100,image=self.white_queen)
#-->
#-->
#<-- TODO: NYI
#<-- force_move
   def force_move(self):
      print("force_move: Not yet implemented, and that's cheating.")
#-->
#<-- load_game - Will use tkinter file select, allowing *.chess files
   def load_game(self):
      print("load_game: Not yet implemented.")
#-->
#<-- save_game - Will use tkinter file select
   def save_game(self):
      print("save_game: Not yet implemented.")
#-->
#-->
#<-- Menu constructor
   def make_menu(self,master):
      self.menu_bar = Menu(master)
#<-- Cascading "File" menu
      self.file_menu = Menu(self.menu_bar, tearoff=False)
      self.file_menu.add_command(label="Load game", command=self.load_game)
      self.file_menu.add_command(label="Save game", command=self.save_game)
      self.file_menu.add_separator()
      self.file_menu.add_command(label="Quit", command=master.quit)

      self.menu_bar.add_cascade(label="File", menu=self.file_menu)
#-->
#<-- Cascading "Edit" menu
      self.edit_menu = Menu(self.menu_bar, tearoff=0)
      self.edit_menu.add_command(
        label="Preferences", command=self.preferences.config_window
	)
      self.edit_menu.add_command(label="Undo", command=self.history.undo)
      self.edit_menu.add_command(label="Redo", command=self.history.redo)
      self.edit_menu.add_command(label="Force move", command=self.force_move)

      self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
#-->
#<-- Cascading "About" menu
      self.about_menu = Menu(self.menu_bar, tearoff=0)
      self.about_menu.add_command(label="Authors", command=self.show_authors)
      self.about_menu.add_command(label="Help", command=self.help_window)

      self.menu_bar.add_cascade(label="About", menu=self.about_menu)
#-->
#-->
#<-- Main constructor
   def __init__(self, master):

     self.createBoard(master)
     self.canvas.pack()

     self.history = History()
     self.preferences = Preferences()

     self.make_menu(master)
     master.config(menu=self.menu_bar)
#-->
#-->
#<-- Imports
from tkinter import * 
from tkinter import messagebox
from PIL import *
#-->
#<-- Bootstrapping
root = Tk()

app = Application(root)

root.mainloop()
root.destroy()
#--> 
