import cv2 as cv
import face_recognition

video = cv.VideoCapture(0)

# Load a sample picture and learn how to recognize it
pic = face_recognition.load_image_file("myPic.jpg")
picKo = face_recognition.face_encodings(pic)[0]

nicole = face_recognition.load_image_file("nicole.jpg")
nicolee = face_recognition.face_encodings(nicole)[0]

# Create arrays of known face encodings and their names
known_face_encodings = [
    picKo,
    nicolee
]
known_face_names = [
    "Jodelmar Beltran",
    "Nicole Carlet"
]

process_this_frame = True

# Define a mouse callback function
def mouse_callback(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        # Left button was clicked, so close the video capture
        video.release()



while True:
    ret, frame = video.read()
    cv.imshow("Camera", frame)

    cv.setMouseCallback("Camera", mouse_callback)
    
    small_frame = cv.resize(frame, (0, 0), fx=0.25, fy=0.25)
    # cv.imshow("Small Frame", small_frame)

    rgb_small_frame = small_frame[:, :, ::-1]
    # cv.imshow("RGb Small Frame", rgb_small_frame)

    if process_this_frame:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        for face_encoding in face_encodings:
            # print(face_recognition.compare_faces(known_face_encodings, face_encoding))
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            # print(matches)
            if True in matches:
                # print("test")
                # print(matches.index(True))
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]
                print(name)
                known_face_names.pop(first_match_index)
                known_face_encodings.pop(first_match_index)
            # print("skip")
    
    if cv.waitKey(1) & 0xFF == ord('q'):
        break


video.release()
cv.destroyAllWindows()