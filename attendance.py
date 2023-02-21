import cv2
import face_recognition as fr
from datetime import datetime
import os
from logo import addLogo
from voice import sayName

path = "./images/"
known_face_names = []
known_face_encodings = []

def encode_known_faces():
    images = os.listdir(path)
    for item in images:
        image = fr.load_image_file(path + item)
        image_path = path + item
        encoding = fr.face_encodings(image)[0]

        known_face_encodings.append(encoding)
        known_face_names.append(os.path.splitext(os.path.basename(image_path))[0].capitalize())

def recordAttendance():
    result = []
    encode_known_faces()

    video = cv2.VideoCapture(0)
    while True:
        ret, frame = video.read()
        now = datetime.now()
        dt_string = now.strftime("%H:%M")
        face_location = fr.face_locations(frame)

        for top, right, bottom, left in face_location:
            cv2.rectangle(frame, (left, top), (right, bottom), (100,191,105), 2)

        date_and_time = now.strftime("%H:%M:%S")
        addLogo(frame)
        cv2.putText(frame, date_and_time, (80,20), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=1, color=(100,191,105), thickness=1, lineType=cv2.LINE_AA)
        cv2.imshow("Camera", frame)
        # resize the frame
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        # convert to rgb
        rgb_small_frame = small_frame[:, :, ::-1]

        face_locations = fr.face_locations(rgb_small_frame)
        face_encodings = fr.face_encodings(rgb_small_frame, face_locations)

        for face_encoding in face_encodings:
            matches = fr.compare_faces(known_face_encodings, face_encoding)
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]
                sayName(name)
                result.append((name, dt_string))
                known_face_names.pop(first_match_index)
                known_face_encodings.pop(first_match_index)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    video.release()
    cv2.destroyAllWindows()
    return result