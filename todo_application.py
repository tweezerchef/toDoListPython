# import required modules

import tkinter as tk
from tkinter import ttk
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

# func to delete all tasks


def delete_all_tasks():
    # ask user for confirmation
    message_box = messagebox.askyesno('Delete All', 'Are you sure?')
    # if value true
    if message_box == True:
        # loop till empty
        while (len(tasks) != 0):
            # pop elements
            tasks.pop()
        # execute sql statement
        the_cursor.execute('delete from tasks')
        list_update()

# func to clear list


def clear_list():
    task_listbox.delete(0, 'end')

# func to close app


def close():
    print(tasks)
    # use destroy method to close app
    guiWindow.destroy()


# func to retrieve data from db
def retrieve_database():
    while (len(tasks) != 0):
        # use pop len will reach 0 when all tasks popped
        tasks.pop()
    # iterate through rows in db table
    for row in the_cursor.execute('select title from the tasks'):
        # insert titles from table to list
        tasks.append(row[0])


# main func
if _name_ == "_main_":
    # create obj of tk class
    guiWindow = tk.Tk()
    # set title
    guiWindow.title('To Do List - JavaPoint')
    # set geom of window
    guiWindow.geometry("500x500+750+250")
    # disable resize
    guiWindow.resizable(0, 0)
    # set bg color
    guiWindow.configure(bg="#FAEBD7")

# add DB connection
the_connection = sql.connect('listOfTasks.db')
# create obj of cursor class
the_cursor = the_connection.cursor()
# execute sql statement
the_cursor.execute('create a table of not exists tasks (title text)')

# define frames
header_frame = tk.Frame(guiWindow, bg="#FAEBD7")
functions_frame = tk.Frame(guiWindow, bg="#FAEBD7")
listbox_frame = tk.Frame(guiWindow, bg="#FAEBD7")

# place frames in app using pack
header_frame.pack(fill="both")
functions_frame.pack(side="left", expand=True, fill="both")
listbox_frame.pack(side="right", expand=True, fill="both")
