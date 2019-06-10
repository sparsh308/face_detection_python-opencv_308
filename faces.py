#THIS PROGRAM IS WRITTEN BY SPARSH KISHORE KUMAR 
#FACE _DETECTOR_USING _OPEN CV PYHTON... HAPPY CODING..:)
# Import the necessary libraries
import cv2

#LOADING OF HAAR_CALASSIFIERS...
haar_cascade_face = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")


#fUNCTION TO DETECT FACES AND DRAW RECTANGLE AROUND IT..
def detect_faces(cascade, test_image, scaleFactor=1.5):
    # create a copy of the image to prevent any changes to the original one.
    image_copy = test_image.copy()

    # convert the test image to gray scale as opencv face detector expects gray imagesq
    gray_image = cv2.cvtColor(image_copy, cv2.COLOR_BGR2GRAY)

    # Applying the haar classifier to detect faces
    faces_rect = cascade.detectMultiScale(gray_image, scaleFactor=scaleFactor, minNeighbors=5)

    for (x, y, w, h) in faces_rect:
        cv2.rectangle(image_copy, (x, y), (x + w, y + h), (0, 255, 0), 2)

    return image_copy


#IT OPENS THE CAMERA AND TAKE THE PICTURE AFTER 1 SECOND .. PRESS Q TO QUIT AND TO SHOW DETECTED FACES ..
cap=cv2.VideoCapture(0)
i=0
while(True):
    ret, frame=cap.read()
    cv2.imshow("frame",frame)
    if i==0:
     cv2.imwrite("newimg.jpg",frame)
    i=i+1
    k=cv2.waitKey(1)
    if k==ord('q'):
        break
img=cv2.imread("newimg.jpg")
#call the function to detect faces
faces = detect_faces(haar_cascade_face, img)
#convert to RGB and display image
cv2.imshow("frame",faces)
cv2.waitKey(0)
cv2.imwrite('image1.png',faces)
cap.release()
cv2.destroyAllWindows()
