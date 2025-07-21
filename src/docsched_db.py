import tkinter as tk
from tkinter import *
import sqlite3

def proc(doctor_name):
    my_w = tk.Tk()
    my_w.geometry("450x350")
    my_w.title(f"Patients of {doctor_name}")
    
    # Connect to the database
    my_conn = sqlite3.connect('hospital.db')

    def display():
        # Query to retrieve patients and appointment times for the specified doctor
        my_cursor = my_conn.execute("""
            SELECT patients.patient_name, patients.appointment_time 
            FROM patients
            JOIN doctors ON patients.doctor_id = doctors.doctor_id
            WHERE doctors.doctor_name = ?;
        """, (doctor_name,))

        global i
        i = 0
        
        # Update the header to include appointment time
        header = ["Patient Name", "Appointment Time"]
        for j, col_name in enumerate(header):
            e = Label(my_w, width=20, text=col_name, relief='ridge', anchor="w", font=('bold', 12))
            e.grid(row=i, column=j)

        i += 1  # Move to the next row for data

        for patient_name, appointment_time in my_cursor:
            e1 = Label(my_w, width=20, text=patient_name, relief='ridge', anchor="w")
            e1.grid(row=i, column=0)

            e2 = Label(my_w, width=20, text=appointment_time, relief='ridge', anchor="w")
            e2.grid(row=i, column=1)

            i += 1  # Move to the next row for the next patient

    display()
    my_w.mainloop()