import cv2 as cv

img = cv.imread('Opencv/photos/cat.jpeg')
cv.imshow('cat',img)

gray =cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow=('gy',gray)

canny = cv.Canny(img , 125,125)
cv.imshow('cannny', canny)

cons ,hei=cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
print(f'{len(cons)} contours(s) found')



cv.waitKey(0)