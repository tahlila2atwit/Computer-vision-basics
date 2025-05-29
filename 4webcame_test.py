import cv2

# read webcam
webcam  = cv2.VideoCapture(0)

#visualize webcam

#not ret - true, while ret b/c its webcam - live vid
while True:
    ret, frame = webcam.read()
    
    cv2.imshow('bitch', frame)
    if cv2.waitKey(300) & 0xFF == ord('q'): # once the user presses q - get out of while True
        break

webcam.release()
cv2.destroyAllWindows()