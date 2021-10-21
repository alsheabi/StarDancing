import cv2
import mediapipe as mp
import time

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()


def findPose( img, draw=True):
    global results
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    if results.pose_landmarks:
        if draw:
            mpDraw.draw_landmarks(img,results.pose_landmarks,
                                       mpPose.POSE_CONNECTIONS)
    return img

##############################################
def findPosition( img, draw=True):
    lmList = []
    lmListR = []
    if results.pose_landmarks:
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = img.shape
            # print(id, lm)
            cx, cy = int(lm.x * w), int(lm.y * h)
            lmList.append([id, cx, cy,lm.z])
            lmListR.append([id,lm.x,lm.y,lm.z])
            if draw:
                cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
    return lmList,lmListR
###############################################
cap = cv2.VideoCapture(0)
pTime = 0

out = cv2.VideoWriter('output.avi', -1, 20.0, (640,480))
while True:
    success, img = cap.read()
    img = findPose(img)
    lmList,lmListR = findPosition(img, draw=False)
    if len(lmList) != 0:
        print(lmList[0])
        print(lmListR[0])
        print(lmList[13])
        print(lmListR[13])
        print(lmList[14])
        print(lmListR[14])

        cv2.circle(img, (lmList[14][1], lmList[14][2]), 15, (255, 0, 0), cv2.FILLED)
        cv2.circle(img, (lmList[13][1], lmList[13][2]), 15, (255, 0, 0), cv2.FILLED)
        cv2.circle(img, (lmList[0][1], lmList[0][2]), 15, (255, 0, 0), cv2.FILLED)
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 0), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
cap.release()
out.release()
cv2.destroyAllWindows()