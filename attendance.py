import face_recognition
import cv2

# Get a reference to the webcam
video_capture = cv2.VideoCapture(0)

# Load a sample picture and learn how to recognize it
obama_image = face_recognition.load_image_file("5.jpg")
obama_face_encoding = face_recognition.face_encodings(obama_image)[0]

# Create arrays of known face encodings and their names
known_face_encodings = [
    obama_face_encoding
]
known_face_names = [
    "Nicole Carlet"
]

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()
    cv2.imshow("Frame", frame)

    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    cv2.imshow("Small Frame", small_frame)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]
    cv2.imshow("RGb Small Frame", rgb_small_frame)

    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            # If a match was found in known_face_encodings, just use the first one.
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]

            face_names.append(name)

    # process_this_frame = not process_this_frame


    # Display the results
    # for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        # top *= 4
        # right *= 4
        # bottom *= 4
        # left *= 4