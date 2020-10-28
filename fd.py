import cv2

#create a cascadeclassifier Object
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#Reading an Image

img= cv2.imread("sample.jpg",1)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#search the Co-ordinates
faces =  face_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=5)
print(type(faces))
print(faces)

for x,y,w,h in faces:
    img = cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0),3)

resized = cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))

cv2.imshow("Gray",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#===========================================================Video Image Recognition====================================
