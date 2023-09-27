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

# define function to update list


def list_update():
    # call function to clear list
    clear_list()
    # iterate through strings in list
    for task in tasks:
        # using insert method to insert tasks
        task_listbox.insert('end', task)

# def function to delete task


def delete_task():
    # try/accept method
    try:
        # get selected entry
        the_value = task_listbox.get(task_listbox.curselection())
        # check if stored value is present in list
        if the_value in tasks:
            # remove task from list
            tasks.remove(the_value)
            # call func to update list
            list_update()
            # use execute method to execute sql statement
            the_cursor.execute(
                'delete from tasks where title = ?', (the_value,))
    except:
        # display msg box w/ msg for exception
        messagebox.showinfo('Error', 'No Task Selected, Can Not Delete')
