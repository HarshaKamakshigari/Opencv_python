import cv2 as cv
import numpy as np

blank=np.zeros((500,500,3) , dtype='uint8')


#paint

cv.rectangle(blank, (150,150), (250,250),(0,255,0), thickness=-1)
cv.imshow('reactangle',blank)
#cir
cv.circle(blank,(blank.shape[1]//2, blank.shape[0]//2),40,(0,0,255), thickness=3)
cv.imshow('circle',blank)
#line

cv.line(blank,(100,300),(blank.shape[1]//2, blank.shape[0]//2),(0,255,0),thickness=1)
cv.imshow('line',blank)
cv.waitKey(0)