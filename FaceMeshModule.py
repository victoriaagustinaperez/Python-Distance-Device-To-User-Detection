#all videos set to 1920x1080
import cv2 #opencv
import mediapipe as mp #Google library import
import time #for framerate

#write class
class FaceMeshDetector():

    def __init__(self,staticMode = False, maxFaces = 1, minDetectionCon = 0.5, minTrackCon = 0.5):

        self.staticMode= staticMode
        self.maxFaces= maxFaces
        self.minDetectionCon= minDetectionCon
        self.minTrackCon= minTrackCon

        self.mpDraw = mp.solutions.drawing_utils #helps draw on faces
        self.mpFaceMesh = mp.solutions.face_mesh
        self.faceMesh = self.mpFaceMesh.FaceMesh(self.staticMode, self.maxFaces,
                                                 self.minDetectionCon, self.minTrackCon) #to create object and from where faces can be found. must be converted for image file

    def findFaceMesh(self,img,draw=True):
        self.imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.faceMesh.process(self.imgRGB)
        landmarks = []
        if self.results.multi_face_landmarks:
            for faceLms in self.results.multi_face_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, faceLms, self.mpFaceMesh.FACE_CONNECTIONS)
                #go through every landmark, convert to X and Y and store it in variabe face
                face = []
                for id,lm in enumerate(faceLms.landmark):
                 #   print(lm) #to display in terminal which landmarks in their X, Y and Z coordinates are being captured
                    ih, iw, ic = img.shape
                    x,y = int(lm.x*iw), int(lm.y*ih) #changed values to pixels
                    cv2.putText(img, str(id), (x, y), cv2.FONT_HERSHEY_PLAIN,
                                1, (0, 255, 0), 1)  # end of framerate
                    #print(id,x,y)
                    face.append([x,y] )
                landmarks.append(face)
        return img, landmarks

#while/if face detected:
    #when minDetectionCon < 0.5 || minTrackCon < 0.5:
        #assume SAR limit being applied is at maximum exposure against head
        #calculate cumulative exposure under answered call on 5G spectrum simulation
        #print 5G simulation waveforms
        #print cumulative exposure graph/log
        #print warning message and suggestion

#what to do if running module by itself
def main():
    cap = cv2.VideoCapture("Videos/1.mp4")  # read video file
    pTime = 0  # past time
    detector = FaceMeshDetector()
    cb = []
    while True:
        success, img = cap.read()
        img, landmarks = detector.findFaceMesh(img,False)

        if len(landmarks) == 0:
            cv2.putText(img, f'', (20, 70), cv2.FONT_HERSHEY_PLAIN,
                    1, (0, 255, 0), 1)  # end of framerate

        else:
            while len(landmarks) != 0:
                # print (landmarks[0])
                cv2.putText(img, f'Specific Absorption Rate (SAR): Calculating....', (20, 70), cv2.FONT_HERSHEY_PLAIN,
                         3, (0, 255, 0), 3) #end of framerate
                cv2.putText(img, f'Reminder that cumulative RF exposure, particularly in direct contact with the head, has shown to cause adverse health', (20, 150), cv2.FONT_HERSHEY_PLAIN,
                    1, (0, 255, 0), 1)  # end of framerate
                cv2.putText(img, f'effects.You are advised to use a handsfree option whenever possible.', (20, 180), cv2.FONT_HERSHEY_PLAIN,
                    1, (0, 255, 0), 1)  # end of framerate

            else:
                cv2.putText(img, f'Specific Absorption Rate (SAR): Reading....', (20, 70), cv2.FONT_HERSHEY_PLAIN,
                         3, (0, 255, 0), 3) #end of framerate
                cv2.putText(img, f'Reminder that cumulative RF exposure, particularly in direct contact with the head, has shown to cause adverse health', (20, 150), cv2.FONT_HERSHEY_PLAIN,
                    1, (0, 255, 0), 1)  # end of framerate
                cv2.putText(img, f'effects.You are advised to use a handsfree option whenever possible.', (20, 180), cv2.FONT_HERSHEY_PLAIN,
                    1, (0, 255, 0), 1)  # end of framerate

        #else:
            #len(landmarks) == 0 && 0.1 < self.faceMesh(self.minTrackCon) < 0.5: #IF LANDMARK IS BEING DETECTED
            # cv2.putText(img, f'Specific Absorption Rate (SAR): Simulating...', (20, 70), cv2.FONT_HERSHEY_PLAIN,
            #         3, (0, 255, 0), 3) #end of framerate
            # cv2.putText(img, f'Reminder that cumulative RF exposure, particularly in direct contact with the head, has shown to cause adverse health', (20, 150), cv2.FONT_HERSHEY_PLAIN,
            #     1, (0, 255, 0), 1)  # end of framerate
            # cv2.putText(img, f'effects.You are advised to use a handsfree option whenever possible.', (20, 180), cv2.FONT_HERSHEY_PLAIN,
            #     1, (0, 255, 0), 1)  # end of framerate



        cv2.imshow("Image", img)
        cv2.waitKey(1)

        # cTime = time.time() #beginning of framerate
        # fps = 1/(cTime-pTime)
        # pTime = cTime
        # cv2.putText(img, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN,
        #             3, (0, 255, 0), 3) #end of framerate

        #if face not detected, print nothing
        #while face detected, print empty SAR
            #if face no longer detected, print sim. SAR

        # while len(landmarks) == 0: #IF LANDMARK IS NOT BEING DETECTED
        #     # cv2.putText(img, f'Specific Absorption Rate (SAR): 50', (20, 70), cv2.FONT_HERSHEY_PLAIN,
        #     #             3, (0, 255, 0), 3) #end of framerate
        #     cv2.putText(img, f'', (20, 70), cv2.FONT_HERSHEY_PLAIN,
        #             3, (0, 255, 0), 3) #end of framerate
if __name__ == "__main__":
    main()