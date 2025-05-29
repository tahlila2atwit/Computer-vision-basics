import os 
import cv2 as cv
import easyocr as eo
import matplotlib as mat
import mediapipe as mp

# read image

img = cv.imread("C:/Users/lilha/Desktop/CommaPrep/Screenshot 2025-05-21 154601.png")

# instance text detector

reader = eo.Reader(['en'], gpu = True)

#detect text on image

text = reader.readtext(img)


# draw bbox and text
for t in text:
    #print(t)
    bbox, textt, score = t

    cv.rectangle(img,bbox[0],bbox[2],(233,0,0),2)
    cv.putText(img, textt, bbox[0], 2, .6,(255,255,0), 2)




cv.imshow('img',img)
cv.waitKey(0)



#---------------------------------------------------

imgg = cv.imread("C:/Users/lilha/Desktop/CommaPrep/Screenshot 2025-05-21 154601.png")

readerr = eo.Reader(['en'], gpu = True)

text = readerr.readtext(imgg)

for tt in text:
    bbbox,textttt,score = tt
    cv.rectangle(imgg,bbbox[0],bbbox[2],(233,3,2),2)
    cv.putText(imgg,textttt,bbbox[0],2,.6,(255,0,0),2)


cv.imshow('real',imgg)
cv.waitKey(0)

#--------------------------------------------------------

cam2 = cv.VideoCapture(0)

readshi = eo.Reader(['en'], gpu = False)

while True:
    ret, frame = cam2.read()
    text2 = readshi.readtext(frame)

    for t in text2:
        box2,text3,score3 = t

        lq = tuple(map(int,box2[0]))
        hw = tuple(map(int, box2[2]))

        detected = text3.upper()
        if "STOP" in detected:
            print("STOP")

        cv.rectangle(frame,lq,hw,(255,255,0),2)
        cv.putText(frame,text3,lq,2,.6,(0,0,0),2)

    cv.imshow('frame',frame)
    if cv.waitKey(100) & 0xFF == ord('q'):
        break

cam2.release()
cv.destroyAllWindows()


#------------------------------------------------
cam3 = cv.VideoCapture(0)

f = eo.Reader(['en'], gpu = False)

while True:
    ret, frame = cam3.read()
    text3 = f.readtext(frame)

    for tt in text3:
        box4,text4,score4 = tt

        l = tuple(map(int,box4[0]))
        h = tuple(map(int, box4[2]))


        if text4 == "STOP":
            print("STOP SIGN DETECTED")

        cv.rectangle(frame,l,h,(255,255,0),2)
        cv.putText(frame,text4,l,2,.6,(0,0,0),2)

    cv.imshow('shi',frame)
    if cv.waitKey(10) & 0xFF == ord('q'):
        break

cam3.release()
cv.destroyAllWindows
#--------------------------------------------------------

cvc = cv.VideoCapture(0)

fr = mp.solutions.face_detection
frr = fr.FaceDetection(min_detection_confidence = .5)

while True:
    ret,frame = cv.read()
    rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    proc = frr.process(rgb)

    if proc.detections:
        for d in proc.detections:
            box = d.location_data.relative_bounding_box
            h,w,_ = frame.shape

            x = int(box.xmin * w)
            y = int(box.ymin * h)
            bw = int(box.width * w)
            bh = int(box.height * h)

            fc = frame[y:y+bh, x:x+bw]

            rect = cv.rectangle(frame,(x,y),(x+bw,y+bh),(255,0,0),2)


    cv.imshow('fr',frame)
    if cv.waitKey(10) & 0xFF == ord('q'):
        break

cvc.release()
cv.destroyAllWindows()
