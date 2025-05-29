import os   
import cv2 as cv
import mediapipe as mp

#read image
img = cv.imread("C:/Users/lilha/Desktop/CommaPrep/Screenshot 2025-02-17 183751.png")

resize = cv.resize(img,(800,600))
#detect faces
mp_face = mp.solutions.face_detection

fd = mp_face.FaceDetection(min_detection_confidence=0.5)

rgb = cv.cvtColor(resize,cv.COLOR_BGR2RGB)
result = fd.process(rgb)

#blur faces

if result.detections:
    for face in result.detections:
        box = face.location_data.relative_bounding_box
        h,w, _ = resize.shape

        x = int(box.xmin * w)
        y = int(box.ymin * h)
        bw = int(box.width * w)
        bh = int(box.height * h)

        face_crop = resize[y:y+bh, x:x+bw]
        blurred = cv.GaussianBlur(face_crop, (55, 55), 30)
        resize[y:y+bh, x:x+bw] = blurred


#save image

cv.imshow('img',resize)
cv.waitKey(0)
cv.destroyAllWindows