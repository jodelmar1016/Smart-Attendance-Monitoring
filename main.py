import cv2 as cv
import numpy as np

cv.namedWindow("ATTENDANCE MONITORING SYSTEM")

def register():
    print("Register")

# window = np.zeros((800,800,3), dtype='uint8')

cv.createButton("Click me!", register)
# cv.createButton("Back",register,None,cv.QT_PUSH_BUTTON,1)

image = cv.imread("1.jpg")

# Display the image in the window
cv.imshow("ATTENDANCE MONITORING SYSTEM", image)

# Wait for a key press
cv.waitKey(0)

# Destroy the window
cv.destroyAllWindows()