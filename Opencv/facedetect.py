import cv2 as cv

cap = cv.VideoCapture(0)

harcas = cv.CascadeClassifier('Opencv/harface.xml')

while True:
    ret, frame = cap.read()
    
    if not ret:
        print("Failed to capture image")
        break
    
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    facer = harcas.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=2)
    
    print(f'Number of faces found = {len(facer)}')
    
    for (x, y, w, h) in facer:
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)
    
    cv.imshow('Face Detection', frame)
    
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
