import cv2 as cv
import numpy as np

img = cv.imread('Opencv/photos/cat.jpeg')

grey=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

lap=cv.Laplacian(grey,cv.CV_64F)
lap=np.uint8(np.absolute(lap))

cv.imshow('lap',lap)

cv.waitKey(0)