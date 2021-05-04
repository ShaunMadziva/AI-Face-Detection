import cv2
from random import randrange # use this to randomise the colour of the rectangles

#load the pre-trained data form opencv (haar cascade algorithm)
trained_faces = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

#choose image to detect faces in
img = cv2.imread('Imges/group_img.jpeg')

#Must convert image to grayscale for better detection 
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Detects faces and gives us the coordinates of rectangle surrounding the face
face_coordinates = trained_faces.detectMultiScale(gray_image)
#print(face_coordinates)

#Draw rectangles around face_coordinates, use for loop to draw around multiple faces
for (x,y,w,h) in face_coordinates:
    cv2.rectangle(img, (x, y), (x+w, y+h), (randrange(100, 256), randrange(100, 256), randrange(100, 256)), 3)


#this will display the chosen image
cv2.imshow("Face Detection", img)
key = cv2.waitKey()

### Stop when 'Q' key is pressed
if key == 81 or key == 113:
    cv2.destroyAllWindows()


print("all is good")