import cv2 as cv

video = cv.VideoCapture(0)

while True:
    ret, frame = video.read()
    cv.imshow("Camera", frame)

    if cv.waitKey(1) & 0xFF == ord('c'):
        cv.imwrite("output.jpg", frame)
    
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv.destroyAllWindows()