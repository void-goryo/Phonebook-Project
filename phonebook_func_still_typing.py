

import os
from tkinter import *
import tkinter as tk
import sqlite3

import phonebook_main
import ptonebook_gui




def center_window(self, w, h):   #pass in the tkinter frame (master) reference and the w and h
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()

    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo


def ask_quit(self):
    if messagebox.askoncancel('Do you want to exit the program?'):
        #this closes the app 
        self.master.destroy()
        os._exit(0)




def create_db(self):
    conn _ sqlite3.connect('db_phonebook.db')
    with conn:
        cur = conn.cursor() #lets us use commands
        cur.execute('CREATE TABLE IF NOT EXISTS tbl_phonebook(\
                    ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                    col_fname TEXT, \
                    col_lname TEXT, \
                    col_fullname TEXT, \
                    col_phone TEXT,\
                    col_email TEXT);')
        conn.commit()
    conn.close


def first_run(self):
    conn = sqlite3.connect('db_phonebook.db')
    with conn:
        cur = conn.cursor()
        cur,count = count_records(cur)
        if count < 1:
            cur.execute('''INSERT INTO tbl_phonebook (col_fnace, col_lname, col_fullname, col_phone, col_email)\
                        VALUES (?,?,?,?,?)''', ('John', 'Doe', 'John Doe', '111-111-1111', 'jdoe@email.com'))
            conn.commit()
        conn.close




def count_records(cur):
    count = ''
    cur.execute('''SELECT COUNT(*) FROM tbl_phonebook''')
    count = cur.fetchone()[0]
    return cur, count

def onSelect(self, event):
    varList = event.widget
    select = varList.curselection()[0]














































