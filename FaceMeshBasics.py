#all videos set to 1920x1080
import cv2 #opencv
import mediapipe as mp #Google library import
import time #for framerate

cap = cv2.VideoCapture("Videos/pc1.mp4") #read video file
pTime = 0 #past time

mpDraw = mp.solutions.drawing_utils #helps draw on faces
mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh(max_num_faces=1) #to create object and from where faces can be found. must be converted for image file

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceMesh.process(imgRGB)
    if results.multi_face_landmarks:
        for faceLms in results.multi_face_landmarks:
            mpDraw.draw_landmarks(img, faceLms, mpFaceMesh.FACE_CONNECTIONS)
            #get points, number them. how do you get these values?
            for id,lm in enumerate(faceLms.landmark):
             #   print(lm) #to display in terminal which landmarks in their X, Y and Z coordinates are being captured
                ih, iw, ic = img.shape
                x,y = int(lm.x*iw), int(lm.y*ih) #changed values to pixels
                print(id,x,y)


    cTime = time.time() #beginning of framerate
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN,
                3, (0, 255, 0), 3) #end of framerate
    cv2.imshow("Image", img)
    cv2.waitKey(1)