import cv2
import numpy as np

kamera = cv2.VideoCapture(0)

dusuk = np.array([88, 50, 50])
yuksek = np.array([130, 255, 255])

while True:
    ret, gorsel = kamera.read()

    hsv = cv2.cvtColor(gorsel, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, dusuk, yuksek)

    son = cv2.bitwise_and(gorsel, gorsel, mask=mask)

    cv2.imshow("mask", mask)
    cv2.imshow("son_resim", son)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

kamera.release()
cv2.destroyAllWindows()

