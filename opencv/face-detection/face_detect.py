# https://realpython.com/face-recognition-with-python/

import cv2 as cv
import sys

# run python commands in the shell to detect face in multiple images :
# $ python face_detect.py abba.png haarcascade_frontalface_default.xml
# $ python face_detect.py NADA-Auto-Show-1.jpg haarcascade_frontalface_default.xml

print(cv.__version__)

# Get user supplied values
imagePath = sys.argv[1]
cascPath = "haarcascade_frontalface_default.xml"

# Create the haar cascade
faceCascade = cv.CascadeClassifier(cascPath)

# Read the image
image = cv.imread(imagePath)
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    # flags=cv.CV_HAAR_SCALE_IMAGE
    # You are using OpenCV 3.X, where the cv attribute is no more available.
    # Just remove that line (like it is done in the repo) or replace it with e.g.
    flags=cv.CASCADE_SCALE_IMAGE
)

print("Found {0} faces!".format(len(faces)))

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv.imshow("Faces found", image)
cv.waitKey(0)
