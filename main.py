#!/usr/bin/python3.4
#<-- README
# The first comment line allows UNIX/Linux shells to start the program without the user explicitly invoking Python.
# For TCL/tk colors, see: http://wiki.tcl.tk/16166
# We may want to use Tix, IF we can figure out how to make it actually draw a pixmap to a canvas.
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
#<-- Piece definitions - This is a rare example of predefined values that may be global. Is there a better way?
# Do not change these definitions. They have been carefully chosen for quick/efficient board weighing.
white_pawn = 21
white_rook = 109
white_knight = 61
white_bishop = 63
white_queen = 191
white_king = 255
black_pawn = 22
black_rook = 110
black_knight = 62
black_bishop = 64
black_queen = 192
black_king = 256
#-->
#<-- Board class
class Board:
   def x(self,n): # Tpls are 4 noobs.
      return (n*50+25)
   def y(self,n):
      return (n*50+25)
#<-- Board functions: board_init/render
   # TODO: I didn't quite have time to make a bitboard, set it up, and use it. 
   def board_init(self):
     for inc_x in range(0,8):
       self.bit_board[inc_x][6] = white_pawn
       self.bit_board[inc_x][1] = black_pawn
     self.bit_board[0][0] = black_rook
     self.bit_board[7][0] = black_rook
     self.bit_board[1][0] = black_knight
     self.bit_board[6][0] = black_knight
     self.bit_board[2][0] = black_bishop
     self.bit_board[5][0] = black_bishop
     self.bit_board[3][0] = black_queen
     self.bit_board[4][0] = black_king
     self.bit_board[0][7] = white_rook
     self.bit_board[7][7] = white_rook
     self.bit_board[1][7] = white_knight
     self.bit_board[6][7] = white_knight
     self.bit_board[2][7] = white_bishop
     self.bit_board[5][7] = white_bishop
     self.bit_board[3][7] = white_queen
     self.bit_board[4][7] = white_king
   def render(self):
      for inc_x in range(0,8):
        for inc_y in range(0,8):
          if self.bit_board[inc_x][inc_y] != 0 :
            self.canvas.create_image(
              self.x(inc_x), self.y(inc_y),
              image=self.decode_piece[self.bit_board[inc_x][inc_y]]
        )
#-->
#<-- constructor
   def __init__(self,master):
# Creates the canvas on which we render the chessboard.
      self.bit_board = [[0 for inc in range(8)] for inc in range(8)]
      self.board_init()
      self.canvas = Canvas(master, width=396, height=396)

# Draws a "black" rectangle in the canvas.
      self.canvas.create_rectangle(0, 0, 400, 400, fill="sienna")
#<-- Fills every other "square" on the board with "white" to make a grid. Colors changed for visibility of pieces aand
# so the white side faces the player 
      for x in range(0, 400, 50): 
        self.canvas.create_rectangle(x, x, x + 50, x + 50, fill="deep sky blue")
        self.canvas.create_rectangle(x, x + 100, x + 50, x + 150, fill="deep sky blue")
        self.canvas.create_rectangle(x + 100, x, x + 150, x + 50, fill="deep sky blue")
        self.canvas.create_rectangle(x + 200, x, x + 250, x + 50, fill="deep sky blue")
        self.canvas.create_rectangle(x + 300, x, x + 350, x + 50, fill="deep sky blue")
        self.canvas.create_rectangle(x, x + 200, x + 50, x + 250, fill="deep sky blue")
        self.canvas.create_rectangle(x, x + 300, x + 50, x + 350, fill="deep sky blue")
#--> 
      self.canvas.pack()
#<-- Bitmap loading and rendering. # TODO: Find not butt-ugly colors.
      self.white_rook = BitmapImage(file="./bitmaps/r49s.bm",foreground="white")
      self.white_knight = BitmapImage(file="./bitmaps/n49s.bm",foreground="white")
      self.white_bishop = BitmapImage(file="./bitmaps/b49s.bm",foreground="white")
      self.white_queen = BitmapImage(file="./bitmaps/q49s.bm",foreground="white")
      self.white_king = BitmapImage(file="./bitmaps/k49s.bm",foreground="white")
      self.white_pawn = BitmapImage(file="./bitmaps/p49s.bm",foreground="white") # My fingers are tired. :(
      self.black_rook = BitmapImage(file="./bitmaps/r49s.bm",foreground="black")
      self.black_knight = BitmapImage(file="./bitmaps/n49s.bm",foreground="black")
      self.black_bishop = BitmapImage(file="./bitmaps/b49s.bm",foreground="black")
      self.black_queen = BitmapImage(file="./bitmaps/q49s.bm",foreground="black")
      self.black_king = BitmapImage(file="./bitmaps/k49s.bm",foreground="black")
      self.black_pawn = BitmapImage(file="./bitmaps/p49s.bm",foreground="black")
#<-- Decodes piece numbers/values to BitmapImage addresses
      self.decode_piece = {
        110 : self.black_rook,
        62 : self.black_knight,
        64 : self.black_bishop,
        192 : self.black_queen,
        256 : self.black_king,
        64 : self.black_bishop,
        62 : self.black_knight,
        110 : self.black_rook,
        22 : self.black_pawn, # Pawn
        109 : self.white_rook,
        61 : self.white_knight,
        63 : self.white_bishop,
        191 : self.white_queen,
        255 : self.white_king,
        63 : self.white_bishop,
        61 : self.white_knight,
        109 : self.white_rook,
        21 : self.white_pawn, # Pawn
      }
#-->
#-->
#-->
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
#<-- Application class
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
      self.board = Board(master)
      self.board.render()

      self.history = History()
      self.preferences = Preferences()

      self.make_menu(master)
      master.config(menu=self.menu_bar)
#-->
#-->
#<-- Imports
from tkinter import * 
from tkinter import messagebox
#-->
#<-- Bootstrapping
root = Tk()
root.wm_title("npdm.chess")

app = Application(root)

root.mainloop()
#root.destroy() # Complains annoyingly, though it's supposedly proper form to put this here.
#--> 
