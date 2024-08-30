import cv2 as cv

img=cv.imread('Opencv/photos/faces.jpeg')


gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

harcas = cv.CascadeClassifier('Opencv/harface.xml')

facer= harcas.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=2)

print(f'no of faces found ={len(facer)})')

for(x,y,w,h) in facer:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)

cv.imshow('face',img)

cv.waitKey(0)