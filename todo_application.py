# import required modules

import tkinter as tk
from tkinter import tkk
from tkinter import messagebox
import sqlite3 as sql

# define empty list
tasks = []

# function to add task to list


def add_task():
    # get string from entry field
    task_string = task_field.get()
    # checking if string empty
    if len(task_string) == 0:
        # display msg 'empty field
        messagebox.showinfo('Error', 'Field is Empty.')
    else:
        # add string to the task list
        tasks.append(task_string)
        # using the execute method to execute SQL statement
        the_cursor.execute('insert into tasks values (?)', (task_string,))
        # call function to update list
        list_update()
        # delete entry in entry field
        task_field.delete(0, 'end')
