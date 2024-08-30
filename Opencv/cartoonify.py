import cv2 
import numpy as np


def cart(frame):
    grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    blur=cv2.medianBlur(grey,5)
    
    eds=cv2.Canny(blur,50,150)
    
    eds=cv2.dilate(eds,None)


    smt=cv2.bilateralFilter(frame,9,100,300)

    cat=cv2.bitwise_and(smt, smt ,mask=eds)

    return cat

cap=cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
     
    if not ret:
        break

    cartoon_frame = cart(frame)
    
    cv2.imshow('Cartoonify', cartoon_frame)
    
    if cv2.waitKey(1) & 0xFF == ord('c'):
        break

cap.release()
cv2.destroyAllWindows()