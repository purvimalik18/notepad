from tkinter import *
m = Tk()
m.title('Untitled-Notepad')
menu = Menu(m)
m.config(menu=menu)
f = Menu(menu)

menu.__Filemenu.add_command(label='File', menu='f')
f.__Filemenu.add_cascade(label='New', command='f.__newFile')
f.__Filemenu.add_cascade(label='Open', command='f.__openFile')
f.__Filemenu.add_cascade(label='Save', command='f.__saveFile')
f.__Filemenu.add_separator()
f.__Filemenu.add_cascade(label='Exit', command=m.quit)

menu.__Editmenu.add_command(label='Edit', menu='f')
f.__Editmenu.add_cascade(label='Cut', command='f.__cut')
f.__Editmenu.add_cascade(label='Copy', command='f.__copy')
f.__Editmenu.add_cascade(label='Paste', command='f.__paste')

menu.__Commandmenu.add_command(label='Commands', menu='f')
f.__Commandmenu.add_command(label='About Commands', command='f.__showCommands')

menu.__Helpmenu.add_command(label='Help', menu='f')
f.__Helpmenu.add_command(label='About Notepad')
mainloop()


