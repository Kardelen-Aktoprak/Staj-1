import cv2
import numpy

resim = cv2.imread("resim.png", 0)

cv2.imshow("ATATURK", resim)

cv2.waitKey(0)
cv2.destroyAllWindows()