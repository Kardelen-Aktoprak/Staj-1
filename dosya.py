import cv2
import numpy as np

yuz = cv2.CascadeClassifier("haarcascade_frontalface_default (1).xml")

resim = cv2.imread("images.jpg")

gri_ton = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)

goster = yuz.detectMultiScale(gri_ton, 1.1, 4)

print(goster)

for (x, y, w, h) in goster:
    cv2.rectangle(resim, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow("resim", resim)


cv2.waitKey(0)
cv2.destroyAllWindows()