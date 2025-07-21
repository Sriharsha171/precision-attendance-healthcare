import tkinter as tk
from tkinter import *
import sqlite3

def process(dname=None):  # Allow dname to be optional
    my_w = tk.Tk()
    my_w.geometry("550x350")  # Adjusted width for better visibility
    
    my_conn = sqlite3.connect('doctor.db')

    def display():
        if dname:  # If a doctor name is provided, filter by name
            query = """SELECT ID, name, dat, intime, 
                              CASE 
                                  WHEN outtime LIKE '1900-01-01%' THEN SUBSTR(outtime, 12, 8) 
                                  ELSE outtime 
                              END AS outtime,
                              workhours 
                       FROM attendance WHERE name = ?"""
            my_cursor = my_conn.execute(query, (dname,))
        else:  # If no name is provided, fetch all records
            query = """SELECT ID, name, dat, intime, 
                              CASE 
                                  WHEN outtime LIKE '1900-01-01%' THEN SUBSTR(outtime, 12, 8) 
                                  ELSE outtime 
                              END AS outtime,
                              workhours 
                       FROM attendance"""
            my_cursor = my_conn.execute(query)

        global i
        i = 0

        headers = ["ID", "Name", "Date", "In Time", "Out Time", "Work Hours"]
        
        # Display headers
        for j, header in enumerate(headers):
            e = Label(my_w, width=12, text=header, relief='ridge', anchor="w", font=('bold', 10))
            e.grid(row=i, column=j)

        i += 1  # Move to the next row for data

        # Display data
        for student in my_cursor:
            for j in range(len(student)):
                e = Label(my_w, width=12, text=student[j], relief='ridge', anchor="w")
                e.grid(row=i, column=j)
            i += 1

    display()
    my_w.mainloop()