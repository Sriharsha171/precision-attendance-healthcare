import sqlite3
 
# Connecting to sqlite
# connection object
connection_obj = sqlite3.connect('doctor.db')
 
# cursor object
cursor_obj = connection_obj.cursor()
 
# Drop the GEEK table if already exists.
cursor_obj.execute("DROP TABLE IF EXISTS attendance")
 
# Creating table
table = '''CREATE TABLE attendance (
                                       ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                       name TEXT NOT NULL,
                                       dat TEXT NOT NULL,
                                       intime TEXT NOT NULL,
                                       outtime TEXT,
                                       workhours INTEGER
                                       );'''
 
cursor_obj.execute(table)
 
print("Table is Ready")
 
# Close the connection
connection_obj.close()