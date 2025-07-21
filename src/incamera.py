import cv2
import pickle
import face_recognition
import datetime
import sqlite3 
import time
import numpy

conn = sqlite3.connect('doctor.db') 
  
# Creating a cursor object using the  
# cursor() method 
cursor = conn.cursor() 

def predict(rgb_frame, knn_clf=None, model_path=None, distance_threshold=0.5):

    if knn_clf is None and model_path is None:
        raise Exception("Must supply knn classifier either thourgh knn_clf or model_path")

    # Load a trained KNN model (if one was passed in)
    if knn_clf is None:
        with open(model_path, 'rb') as f:
            knn_clf = pickle.load(f)

    # Load image file and find face locations
    # X_img = face_recognition.load_image_file(X_img_path)
    X_face_locations = face_recognition.face_locations(rgb_frame, number_of_times_to_upsample=2)

    # If no faces are found in the image, return an empty result.
    if len(X_face_locations) == 0:
        return []

    # Find encodings for faces in the test iamge
    faces_encodings = face_recognition.face_encodings(rgb_frame, known_face_locations=X_face_locations)

    # Use the KNN model to find the best matches for the test face
    closest_distances = knn_clf.kneighbors(faces_encodings, n_neighbors=1)
    are_matches = [closest_distances[0][i][0] <= distance_threshold for i in range(len(X_face_locations))]
    # print(closest_distances)
    # Predict classes and remove classifications that aren't within the threshold
    return [(pred, loc) if rec else ("unknown", loc) for pred, loc, rec in zip(knn_clf.predict(faces_encodings), X_face_locations, are_matches)]



def identify_faces(video_capture):
    buf_length = 10
    known_conf = 5
    buf = [[]] * buf_length
    i = 0
    process_this_frame = True
    recognized_name = None  # Variable to store the recognized name

    while True:
        ret, frame = video_capture.read()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_frame = numpy.ascontiguousarray(small_frame[:, :, ::-1])

        if process_this_frame:
            predictions = predict(rgb_frame, model_path="/home/pi/Desktop/DoctorAttendance/models/trained_model.clf")

        process_this_frame = not process_this_frame
        face_names = []
        current_date = datetime.datetime.today().strftime('%Y-%m-%d')

        for name, (top, right, bottom, left) in predictions:
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

            if name.lower() not in ["unknown", "unKnown"]:
                recognized_name = name  # Store the recognized name
                currentDateAndTime = datetime.datetime.now()
                currentTime = currentDateAndTime.strftime("%H:%M:%S")
                query = "SELECT name FROM attendance WHERE dat = ?"
                data = cursor.execute(query, (current_date,))
                row = data.fetchall()

                if row:
                    for item in row:
                        dname = item[0]
                        if dname == name:
                            break
                        else:
                            query1 = "SELECT * FROM attendance WHERE name = ?"
                            data1 = cursor.execute(query1, (name,))
                            row1 = data1.fetchone()
                            if row1:
                                continue
                            else:
                                query = "INSERT INTO attendance (name, dat, intime) VALUES (?, ?, ?)"
                                cursor.execute(query, (name, current_date, currentTime))
                                conn.commit()
                else:
                    query = "INSERT INTO attendance (name, dat, intime) VALUES (?, ?, ?)"
                    cursor.execute(query, (name, current_date, currentTime))
                    conn.commit()

            face_names.append(name)

        buf[i] = face_names
        i = (i + 1) % buf_length

        cv2.imshow('In Camera', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()
    return recognized_name  # Return the recognized name