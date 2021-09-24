import cv2
import time
import HandTrackingModule as htm


pTime = 0  # Previous time
cTime = 0  # Current time
# Webcam 1
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

detector = htm.handDetector()

while True:
    success, img = cap.read()  # Get image
    img = detector.findHands(img)
    lmList = detector.findPosition(img)
    if len(lmList) != 0:
        print(lmList[4])

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    # Show fps on cam screen
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 255), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)