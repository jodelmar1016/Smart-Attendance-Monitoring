import cv2

def take_a_pic():
    result = ""
    video = cv2.VideoCapture(0)

    while True:
        ret, frame = video.read()
        cv2.imshow("Camera", frame)

        if cv2.waitKey(1) & 0xFF == ord('c'):
            result = "Successfully Registered"
            break
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()
    return result