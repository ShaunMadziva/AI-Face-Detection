import cv2
from random import randrange # use this to randomise the colour of the rectangles

#load the pre-trained data form opencv (haar cascade algorithm)
trained_faces = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

#To capature video from your default webcam use 0, instead of 0 you put a video filename
webcam = cv2.VideoCapture(0)

#loop through frames forever
while True:
    ###read current frame
    successful_frame_read, frame = webcam.read()

    #Must convert image to grayscale for better detection 
    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Detects faces and gives us the coordinates of rectangle surrounding the face
    face_coordinates = trained_faces.detectMultiScale(gray_image)

    #Draw rectangles around face_coordinates, use for loop to draw around multiple faces
    for (x,y,w,h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (randrange(100, 256), randrange(100, 256), randrange(100, 256)), 3)

    #this will display the chosen image
    cv2.imshow("Video_Face Detection", frame)
    key = cv2.waitKey(1)

    ### Stop when 'S' key is pressed
    if key == 83 or key == 115:
        break

webcam.release()



print("all is good")