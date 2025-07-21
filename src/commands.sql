-- Create table for Doctors
CREATE TABLE IF NOT EXISTS doctors (
    doctor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    doctor_name TEXT NOT NULL
);

-- Create table for Patients
CREATE TABLE IF NOT EXISTS patients (
    patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_name TEXT NOT NULL,
    doctor_id INTEGER,
    appointment_time TEXT,
    FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id)
);

-- Insert Doctors
INSERT INTO doctors (doctor_name) VALUES ('Dr. Sriharsha');
INSERT INTO doctors (doctor_name) VALUES ('Dr. Chandana');
INSERT INTO doctors (doctor_name) VALUES ('Dr. Harsha');
INSERT INTO doctors (doctor_name) VALUES ('Dr. Pramodh');

-- Insert Patients
INSERT INTO patients (patient_name, doctor_id, appointment_time) VALUES ('Raghavendra Gowda', 1, '09:00 AM'); 
INSERT INTO patients (patient_name, doctor_id, appointment_time) VALUES ('Anusha Patil', 1, '10:30 AM'); 
INSERT INTO patients (patient_name, doctor_id, appointment_time) VALUES ('Mahesh Hegde', 2, '11:00 AM'); 
INSERT INTO patients (patient_name, doctor_id, appointment_time) VALUES ('Suma Kulkarni', 2, '01:00 PM'); 
INSERT INTO patients (patient_name, doctor_id, appointment_time) VALUES ('Chandrashekar Naik', 3, '02:15 PM'); 
INSERT INTO patients (patient_name, doctor_id, appointment_time) VALUES ('Pooja Deshpande', 4, '03:00 PM'); 
INSERT INTO patients (patient_name, doctor_id, appointment_time) VALUES ('Vinayak Joshi', 4, '03:30 PM'); 
INSERT INTO patients (patient_name, doctor_id, appointment_time) VALUES ('Sushma Kattimani', 4, '04:00 PM'); 
INSERT INTO patients (patient_name, doctor_id, appointment_time) VALUES ('Rajeshwari Rao', 4, '04:30 PM'); 
INSERT INTO patients (patient_name, doctor_id, appointment_time) VALUES ('Pradeep Shetty', 3, '05:00 PM'); 
INSERT INTO patients (patient_name, doctor_id, appointment_time) VALUES ('Manjunath Acharya', 3, '05:30 PM'); 
INSERT INTO patients (patient_name, doctor_id, appointment_time) VALUES ('Ramesh Bhat', 3, '06:00 PM'); 
INSERT INTO patients (patient_name, doctor_id, appointment_time) VALUES ('Srilakshmi Kamath', 3, '06:30 PM'); 
INSERT INTO patients (patient_name, doctor_id, appointment_time) VALUES ('Sharath Kumar', 2, '07:00 PM'); 
INSERT INTO patients (patient_name, doctor_id, appointment_time) VALUES ('Deepa Raj', 2, '07:30 PM'); 
INSERT INTO patients (patient_name, doctor_id, appointment_time) VALUES ('Nandish Pai', 2, '08:00 PM'); 
INSERT INTO patients (patient_name, doctor_id, appointment_time) VALUES ('Harish Reddy', 1, '08:30 PM'); 
INSERT INTO patients (patient_name, doctor_id, appointment_time) VALUES ('Veena Narayan', 1, '09:00 PM'); 
INSERT INTO patients (patient_name, doctor_id, appointment_time) VALUES ('Yashwanth Ullal', 1, '09:30 PM'); 
INSERT INTO patients (patient_name, doctor_id, appointment_time) VALUES ('Kavya Bellary', 5, '10:00 PM');
