import numpy as np
import cv2

#img = './omr.png'
#img_read = cv2.imread(img, cv2.IMREAD_COLOR)

#cv2.namedWindow('model', cv2.WINDOW_NORMAL)
#cv2.imshow('model',img_read)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

def showImage():
    imgfile = './omr.png'
    img = cv2.imread(imgfile, cv2.IMREAD_COLOR)
    cv2.imshow('model', img)

    k = cv2.waitKey(0) & 0xFF

    if k == 27:
        cv2.destroyAllWindows()

showImage()