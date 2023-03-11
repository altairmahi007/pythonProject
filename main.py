import cv2
# read haarcascade data
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# read image from doc
img = cv2.imread('how-to-determine-your-faceshape.jpg')
# convert to grayscale as CV2 supports that
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# show grayscale image
cv2.imshow('Testing',gray_img)
# find coordinates
coord = trained_face_data.detectMultiScale(gray_img)
cv2.waitKey()
print(coord)
# read haarcascade data
for (x,y,w,h) in coord:
 cv2.rectangle(img,(x ,y),(x+w,y+h),(255,255,255),3)
cv2.imshow('Testing',img)
cv2.waitKey()


