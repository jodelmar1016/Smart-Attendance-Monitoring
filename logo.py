import cv2 as cv
import numpy as np

def addLogo(img):
    color = (100,191,105)
    points = [(25,70),(10,70),(10,10),(70,10),(70,70),(46,70)]
    points = np.array(points, np.int32)
    img = cv.polylines(img, [points], isClosed=False, color=color, thickness=1)

    img = cv.ellipse(img, (46,46),(24,24),0,90,270,color,1)
    img = cv.line(img, (22,46),(56,46),color,1)
    img = cv.line(img, (46,22),(56,22),color,1)

    font = cv.FONT_HERSHEY_PLAIN
    img = cv.putText(img, 'ECO SYSTEM', (10,80), font, 0.6, color)

    return img