# AI-Face-Detection
Face Detection program using the Haar Cascade algorithm 

AI Face Detection

‘Haar Cascade’?

Is an algorithm that cascades down through lines of code and it was developed by a guy named Haar.

The algorithm takes an image or frame and passes the pixels through the code like a funnel until it narrows down to the rectangle where the face is detected 

How does it work?


The idea is that blocks are overlain over an image and the pixels under the black and white sections are compared to show the relationship between them. This process is then layered over and again, and by cascading down these different layers. The algorithm is trained by giving it faces so that it can build models, which it can then use to refer to in-order to recognise faces in production. The algorithm works by comparing the darker and lighter parts of a face in grayscale. 


Training (the CascadeObjectDetector):
The algorithm is trained through supervised learning, were it is fed ‘positive images’ (faces) and ‘negative images’ (non faces).

We have to test every Haar Feature on every image.
Every TYPE, every SIZE, every LOCATION (Each HF gives us a number Right or Wrong)
The program adds up all the numbers in the white section and in the black section and returns the difference. This is then compared to a known threshold for a face. 
Whichever Haar Feature matches closest to our training images is our FIRST winner.

Once we have found our first ~1000 winner Haar Features, we can chain them together into our face detector.




OpenCV does all the hard work of training for us and they provide a pre-trained classifier that has the chain of hair features that best match a face.

We just pass a sliding window of the image into the classifier, and it’s run through all of the Haar cascades. If it gets all the way to the end it's a face.

Useful links:
https://docs.opencv.org/master/index.html

https://github.com/opencv/opencv/tree/master/data/haarcascades

Haar Cascade Visualisation:-  https://www.youtube.com/watch?v=hPCTwxF0qf4&ab_channel=AnkurDivekar


