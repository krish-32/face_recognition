import cv2
import face_recognition
import numpy
from .models import *
from datetime import datetime
def main():
    cap = cv2.VideoCapture(1)
    images=hod.objects.all()
    person_face_names = []
    person_face_encodings = []
    time=[]

    for image in images:
        img = face_recognition.load_image_file(image.photo)
        try:
            person_face_encodings.append(face_recognition.face_encodings(img)[0])
            person_face_names.append(image.name)
        except IndexError as e:
            print(e,"So,Please Re-Upload the image:",image.name)
    data_locations = []
    data_names = []
    frameProcess = True
    while True:
        ret, frame = cap.read()
        resizing = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_resizing = numpy.ascontiguousarray(resizing[:, :, ::-1])

        if frameProcess:
            data_locations = face_recognition.face_locations(rgb_resizing)
            data_encodings = face_recognition.face_encodings(rgb_resizing, data_locations)
            for dc in data_encodings:
                matches = face_recognition.compare_faces(person_face_encodings, dc)
                name = "UNKNOWN"
                if True in matches:
                    face_distances = face_recognition.face_distance(person_face_encodings ,dc)
                    best_match_index = face_distances.argmin()
                    name = person_face_names[best_match_index]


                print(data_names.append(name))
                time.append(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

        frameProcess = not frameProcess
        for (top, right, bottom, left), name in zip(data_locations, data_names):
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4
            cv2.rectangle(frame, (left, top), (right, bottom), (255, 0, 0), 2)
            cv2.rectangle(frame, (left, bottom - 20), (right, bottom), (255, 0, 0), cv2.FILLED)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.7, (255, 255, 255), 2)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    print(data_names)
    return data_names,time