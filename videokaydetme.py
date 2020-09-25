import cv2


kamera = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*"XVID") #format
kayit = cv2.VideoWriter("kayit.avi", fourcc, 30, (640, 480))

while True:
    ret, goruntu = kamera.read()

    if ret == True:
        kayit.write(goruntu)

    cv2.imshow("goruntu", goruntu)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

kamera.release()
cv2.destroyAllWindows()
