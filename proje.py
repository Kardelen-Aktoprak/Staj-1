import cv2

kamera = cv2.VideoCapture(0)

kamera.set(3, 300)
kamera.set(4, 300)

#def ayarlama(kare, yuzde = 50):
    #genislik = int(kare.shape[1] * yuzde / 100)
    #yukseklik = int(kare.shape[0] * yuzde / 100)
    #boyut = (genislik, yukseklik)
    #return cv2.resize(kare, boyut, interpolation= cv2.INTER_AREA)

while True:
    ret, kare = kamera.read()
    griTon = cv2.cvtColor(kare, cv2.COLOR_BGR2GRAY)
    #kare2 = ayarlama(kare)

    cv2.imshow("kamera", kare)
    cv2.imshow("gri", griTon)
    #cv2.imshow("boyutlandirilmis kamera", kare2)


    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

kamera.release()
cv2.destroyAllWindows()
