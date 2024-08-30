import cv2 as cv

img=cv.imread('Opencv/photos/cat.jpeg')

cv.imshow('cat',img)

grey=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gry',grey)


Blur= cv.GaussianBlur(img,(3,3),cv.BORDER_CONSTANT)
cv.imshow('blr',Blur)

cv.waitKey(0)