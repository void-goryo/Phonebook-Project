




from tkinter import *
import tkinter as tk

import phonebook_main
import phonebook_func




def load_gui(self):
    
    #First name
    self.lblFname = tk.Label(self.master, text='First Name:')
    self.lblFname.grid(row = 0, column = 0, padx = (27,0), pady = (10,0), sticky = N+W)
    
    #Last name
    self.lblLname = tk.Label(self.master, text='Last Name:')
    self.lblLname.grid(row = 2, column = 0, padx = (27,0), pady = (10,0), sticky = N+W)

    #Phone number
    self.lblPhone = tk.Label(self.master, text='Phone Number:')
    self.lblPhone.grid(row = 4, column = 0, padx = (27,0), pady = (10,0), sticky = N+W)

    #Email
    self.lblEmail = tk.Label(self.master, text='Email:')
    self.lblEmail.grid(row = 6, column = 0, padx = (27,0), pady = (10,0), sticky = N+W)

    #User
    self.lblUser = tk.Label(self.master, text='User:')
    self.lblUser.grid(row = 0, column = 2, padx = (0,0), pady = (10,0), sticky = N+W)


    #define the listbox with a scrollbar
    self.scrollbar1 = Scrollbar(self.master, orient=VERTICAL)
    self.scrollbar1 = config(command = self.lstList1.yview)
    self.scrollbar1.grid(row = 1, column = 5, rowspan = 7, columnspan = 1, padx = (0,0), pady = (0,0), sticky = N+E+S)

    self.lstList = Listbox(self.master, exportselection = 0, yscrollcommand = self.scrollbar1.set)
    self.lstList1.bind('<<ListboxSelect>>',lambda event: phonebook_func.onSelect(self,event))
    self.lstList1.grid(row = 1, column = 2, rowspan = 7, columnspan = 3, padx = (0,0), pady(0,0), sticky = N+E+S+W)

    self.btn_add = tk.Button(self.master, width = 12, height = 2, text = 'Add', command = lambda:\
                             phonebook_func.addToList(self))
    self.btn_add.grid(row = 8, column = 0, padx = (25,0), pady = (45,10), sticky=W)


    self.btn_add = tk.Button(self.master, width = 12, height = 2, text = 'Update', command = lambda:\
                             phonebook_func.onUpdate(self))
    self.btn_add.grid(row = 8, column = 0, padx = (15,0), pady = (45,10), sticky=W)


    self.btn_add = tk.Button(self.master, width = 12, height = 2, text = 'Delete', command = lambda:\
                             phonebook_func.onDelete(self))
    self.btn_add.grid(row = 8, column = 0, padx = (15,0), pady = (45,10), sticky=W)


    self.btn_add = tk.Button(self.master, width = 12, height = 2, text = 'Close', command = lambda:\
                             phonebook_func.ask_quit(self))
    self.btn_add.grid(row = 8, column = 0, padx = (15,0), pady = (45,10), sticky=E)


    phonebook_func.create_db(self)
    phonebook_func.onRefresh(self)



if __name__ == '__main__':
    pass
    
