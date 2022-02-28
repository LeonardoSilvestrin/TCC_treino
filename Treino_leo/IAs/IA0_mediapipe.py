import cv2 as cv
import mediapipe as mp
import time


cam = cv.VideoCapture(0)

mpHands = mp.solutions.hands
maos = mpHands.Hands()
MpDraw = mp.solutions.drawing_utils

while True:
    sucess, img = cam.read()

    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    results = maos.process(imgRGB)
    #print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for HandLMS in results.multi_hand_landmarks:
            MpDraw.draw_landmarks(img, HandLMS, mpHands.HAND_CONNECTIONS)
    cv.imshow("Imagem",img)
    cv.waitKey(1)