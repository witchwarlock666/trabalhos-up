import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1)
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

while True:
    suc, img = cap.read()
    img = cv2.resize(img, (1280, 720))
    img = cv2.flip(img, 1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    res = hands.process(imgRGB)
    
    if res.multi_hand_landmarks:
        for handLms in res.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
    
    # cTime = time.time()
    # fps = 1/(cTime-pTime)
    # pTime = cTime
    
    # cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
            
    cv2.imshow("Image", img)
    cv2.waitKey(1)
