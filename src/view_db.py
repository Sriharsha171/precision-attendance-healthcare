import sqlite3

# Connect to the database
conn = sqlite3.connect("hospital.db")
cursor = conn.cursor()

# Execute a query to view the doctors
cursor.execute("SELECT * FROM doctors")
doctors = cursor.fetchall()
cursor.execute("SELECT * FROM patients")
patients = cursor.fetchall()

print('Docs')
# Print the doctors
for doctor in doctors:
    print(doctor)

print('Patients')
for patient in patients:
    print(patient)

# Close the connection
conn.close()
