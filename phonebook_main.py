'''====================================================================

    Python ver: 3.10.2

    Author: Gabriel Jones

    Purpose: Phonebook demo. This is to dementrate OOP, Tkinter GUI module,
                and using Tkinter Parent and Child relationships

    Tested OS: Windows 10

===================================================================='''


from tkinter import *
import tkinter as tk

#make sure to import other modules that we will be using
import phonebook_gui
import phonebook_func


#Tkinter Frame
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        #define master frame config
        self.master = master
        self.master.minsize(500, 300)  #width x height
        self.master.maxsize(500, 300)
        #this will center the window
        phonebook_func.center_window(self, 500, 300)
        self.master.configure(bg='#f0f0f0')
        #this catches the user when they try to click the X in the top right
        #of the window
        self.master.protocol('WM_DELETE_WINDOW', lambda: phonebook_func.ask_quit(self))
        arg = self.master

        #load GUI from seperate module to make the code look nice
        phonebook_gui.load_gui(self)



if __name__ == '__main__':
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
