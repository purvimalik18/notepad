from tkinter import *
#to save, read, write, etc
import os

m = Tk()  # to create window
m.geometry("800x600")
m.title('Untitled-Notepad')
m.config(menu=m)
menu = Menu(m)
f = Menu(menu, tearoff=False)

menu.add_cascade(label='File', menu=f)
f.add_command(label='New', accelerator='Ctrl+N', command='f.__newFile')
f.add_command(label='Open', accelerator='Ctrl+O', command='f.__openFile')
f.add_command(label='Save', accelerator='Ctrl+S', command='f.__saveFile')
f.add_separator()
f.add_command(label='Exit', command=m.quit)

e = Menu(menu, tearoff=False)
menu.add_cascade(label='Edit', menu=e)
e.add_command(label='Cut', command='e.__cut')
e.add_command(label='Copy', command='e.__copy')
e.add_command(label='Paste', command='e.__paste')

c = Menu(menu, tearoff=False)
menu.add_cascade(label='Commands', menu=c)
c.add_command(label='About Commands', command='c.__showCommands')

h = Menu(menu, tearoff=False)
menu.add_cascade(label='Help', menu=h)
h.add_command(label='About Notepad')


text_editor = Text(m)
text_editor.config(wrap='word', relief=FLAT)


m.config(menu=menu)  # to view all the cascades
m.mainloop()  # to open and hold




