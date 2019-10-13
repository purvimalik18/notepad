from tkinter import *
m = Tk()
m.title('Untitled-Notepad')
menu = Menu(m)
m.config(menu=menu)
f = Menu(menu)

menu.Filemenu.add_cascade(label='File', menu='f')
f.Filemenu.add_command(label='New', command='f.__newFile')
f.Filemenu.add_command(label='Open', command='f.__openFile')
f.Filemenu.add_command(label='Save', command='f.__saveFile')
f.Filemenu.add_separator()
f.Filemenu.add_command(label='Exit', command=m.quit)

menu.Editmenu.add_cascade(label='Edit', menu='f')
f.Editmenu.add_command(label='Cut', command='f.__cut')
f.Editmenu.add_command(label='Copy', command='f.__copy')
f.Editmenu.add_command(label='Paste', command='f.__paste')

menu.Commandmenu.add_cascade(label='Commands', menu='f')
f.Commandmenu.add_command(label='About Commands', command='f.__showCommands')

menu.Helpmenu.add_cascade(label='Help', menu='f')
f.Helpmenu.add_command(label='About Notepad')


mainloop()


