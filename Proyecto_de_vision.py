#Jorge Misael Galán Santana. 19110166. 7E1.
import cv2
import webbrowser
import time
# initalize the camera
cap = cv2.VideoCapture(0)
# initialize the OpenCV QRCode detector
detector = cv2.QRCodeDetector()
while True:
  _, img = cap.read()
  # detect and decode
  data, vertices_array, _ = detector.detectAndDecode(img)
  # check if there is a QRCode in the image
  if vertices_array is not None:
    if data:
      print("QR Code detected, data:\n", data)
      cv2.putText(img,data,(350,20),2,0.38,(255,125,180),1,cv2.LINE_AA)
      webbrowser.open(data)
      time.sleep(5)
  # display the result
  cv2.imshow("img", img)
  # Enter q to Quit
  k=cv2.waitKey(30) & 0xff
  if k==27:
    break

cv2.destroyAllWindows()
cap.release()
