import os               #to save, read, write, etc
from tkinter import *

def quitApplication(self):
   self.root.destroy()

def showAbout(self):
   showinfo("About Notepad", "Simple text editor like notepad using TKINTER in Python")

def showCommand(self):
   showinfo("Notepad", "Just Another TextPad \n Copyright \n with XYZ license")

def openFile(self):
   self.file = askopenfilename(defaultextension=".txt", filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
   if self.file == "":
      # no file to open
      self.__file = None
   else:
       self.__root.title(os.path.basename(self.__file) + " - Notepad")
       self.__thisTextArea.delete(1.0,END)
       file = open(self.__file,"r")
       self.__thisTextArea.insert(1.0,file.read())
       file.close()
def __newFile(self):
   self.__root.title("Untitled Notepad")
   self.__file = None
   self.__thisTextArea.delete(1.0,END)
def __saveFile(self):
   if self.__file == None:
       self.__file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt", filetypes=[("All Files","*.*"), ("Text Documents","*.txt")])
       if self.__file == "":
           self.__file = None
       else:
           file1 = open(self.file,"w")
           file1.write(self.thisTextArea.get(1.0,END))
           file1.close()
           self.root.title(os.path.basename(self.file) + " - Notepad")
   else:
       file1 = open(self.file,"w")
       file1.write(self.thisTextArea.get(1.0,END))
       file1.close()
   def cut(self):
      self.thisTextArea.event_generate("<<Cut>>")
   def copy(self):
      self.thisTextArea.event_generate("<<Copy>>")
   def paste(self):
      self.thisTextArea.event_generate("<<Paste>>")

#To get the space above the message
from tkinter.messagebox import *

#To get the dialog box to open when required
from tkinter.filedialog import *
class Notepad:
   # Set up the root widget
   root = Tk()
   thisWidth = 500
   thisHeight = 700
   thisTextArea = Text(root)
   thisMenuBar = Menu(root)
   thisFileMenu = Menu(thisMenuBar, tearoff=0)
   thisEditMenu = Menu(thisMenuBar, tearoff=0)
   thisHelpMenu = Menu(thisMenuBar, tearoff=0)
   thisCommandMenu = Menu(thisMenuBar, tearoff=0)

   #To add scrollbar
   thisScrollBar = Scrollbar(thisTextArea)
   file = None
   def __init__(self,**kwargs):
      #icon
      try:
         self.root.wm_iconbitmap("Notepad.ico")
      except:
         pass
   # Set window size as mentioned above (the default is 300x300)
      try:
          self.thisWidth = kwargs['width']
      except KeyError:
          pass
      try:
          self.thisHeight = kwargs['height']
      except KeyError:
          pass
      # the window text
      self.root.title("Untitled-Notepad")
      # Center the window
      screenWidth = self.root.winfo_screenwidth()
      screenHeight = self.root.winfo_screenheight()
      # For left-align
      left = (screenWidth / 2) - (self.thisWidth / 2)
      # For right-align
      top = (screenHeight / 2) - (self.thisHeight /2)
      # For top and bottom
      self.root.geometry('%dx%d+%d+%d' % (self.thisWidth, self.thisHeight, left, top))
      # To make the textarea auto resizable
      self.root.grid_rowconfigure(0, weight=1)
      self.root.grid_columnconfigure(0, weight=1)
      # Add controls (widget)
      self.thisTextArea.grid(sticky = N + E + S + W)
      # To open new file
      self.thisFileMenu.add_command(label="New", command=self.newFile)
      # To open a already existing file
      self.thisFileMenu.add_command(label="Open", command=self.openFile)
      # To save current file
      self.thisFileMenu.add_command(label="Save", command=self.saveFile)
      # To create a line in the dialog
      self.thisFileMenu.add_separator()
      self.thisFileMenu.add_command(label="Exit", command=self.quitApplication)
      self.thisMenuBar.add_cascade(label="File", menu=self.thisFileMenu)
      # To give a feature of cut
      self.thisEditMenu.add_command(label="Cut", command=self.cut)
      # to give a feature of copy
      self.thisEditMenu.add_command(label="Copy", command=self.copy)
      # To give a feature of paste
      self.thisEditMenu.add_command(label="Paste", command=self.paste)
      # To give a feature of editing
      self.thisMenuBar.add_cascade(label="Edit", menu=self.thisEditMenu)


      # To create a feature of description of the notepad
      self.thisHelpMenu.add_command(label="About Notepad", command=self.showAbout)
      self.thisCommandMenu.add_command(label="About Commands", command=self.showCommand)
      self.thisMenuBar.add_cascade(label="Commands", menu=self.thisCommandMenu)
      self.thisMenuBar.add_cascade(label="Help", menu=self.thisHelpMenu)
      self.root.config(menu=self.thisMenuBar)                   # to view all the cascades
      self.thisScrollBar.pack(side=RIGHT,fill=Y)


      # Scrollbar will adjust automatically according to the content
      self.thisScrollBar.config(command=self.thisTextArea.yview)
      self.thisTextArea.config(yscrollcommand=self.thisScrollBar.set)
   def quitApplication(self):
      self.root.destroy()

   def showAbout(self):
      showinfo("About Notepad", "Simple text editor like notepad using Python")
   def showCommand(self):
      showinfo("Notepad", "Just Another TextPad \n Copyright \n with XYZ license you can use it")
   def openFile(self):
      self.file = askopenfilename(defaultextension=".txt", filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
      if self.file == "":
         # no file to open
         self.file = None
      else:
         # Try to open the file
         # set the window title
         self.root.title(os.path.basename(self.__file) + " - Notepad")
         self.thisTextArea.delete(1.0, END)
         file = open(self.file, "r")
         self.thisTextArea.insert(1.0, file.read())
         file.close()
   def newFile(self):
      self.root.title("Untitled Notepad")
      self.file = None
      self.thisTextArea.delete(1.0, END)
   def saveFile(self):
      if self.file == None:
          self.file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt", filetypes=[("All Files","*.*"), ("Text Documents","*.txt")])
          if self.file == "":
              self.file = None
          else:
              file = open(self.file, "w")
              file.write(self.thisTextArea.get(1.0, END))
              file.close()
              self.root.title(os.path.basename(self.file) + " - Notepad")
      else:
          file = open(self.file, "w")
          file.write(self.thisTextArea.get(1.0, END))
          file.close()
   def cut(self):
      self.thisTextArea.event_generate("<<Cut>>")
   def copy(self):
      self.thisTextArea.event_generate("<<Copy>>")
   def paste(self):
      self.thisTextArea.event_generate("<<Paste>>")
   def run(self):
      # Run main application
      self.root.mainloop()


# Run main application
notepad = Notepad(width=600, height=400)
notepad.run()

#To open new file
self.thisFileMenu.add_command(label="New", command=self.newFile, accelerater = 'Ctrl+N')
# To open a already existing file
self.thisFileMenu.add_command(label="Open", command=self.openFile, accelerater = 'Ctrl+O')
# To save current file
self.thisFileMenu.add_command(label="Save", command=self.saveFile, accelerater = 'Ctrl+S')
# To create a line in the dialog
self.thisFileMenu.add_separator()
self.thisFileMenu.add_command(label="Exit", command=self.quitApplication,accelerater = 'Ctrl+E')
self.thisMenuBar.add_cascade(label="File", menu=self.thisFileMenu)
# To give a feature of cut
self.thisEditMenu.add_command(label="Cut", command=self.cut,accelerater = 'Ctrl+X')
# to give a feature of copy
self.thisEditMenu.add_command(label="Copy", command=self.copy, accelerater = 'Ctrl+C')
# To give a feature of paste
self.thisEditMenu.add_command(label="Paste", command=self.paste, accelerater = 'Ctrl+V')
# To give a feature of editing
self.thisMenuBar.add_cascade(label="Edit", menu=self.thisEditMenu)
# To create a feature of description of the notepad
self.thisHelpMenu.add_command(label="About Notepad.....", command=self.showAbout)
self.thisCommandMenu.add_command(label="About Commands.....", command=self.showCommand)
self.thisMenuBar.add_cascade(label="Commands", menu=self.thisCommandMenu)
self.thisMenuBar.add_cascade(label="Help", menu=self.thisHelpMenu)




