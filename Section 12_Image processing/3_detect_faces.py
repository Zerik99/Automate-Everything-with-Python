import cv2

image = cv2.imread("Section 12_Image processing/images/humans.jpeg")

face_cascade = cv2.CascadeClassifier("Section 12_Image processing/faces.xml")

faces = face_cascade.detectMultiScale(image, 1.1, 4)

print(faces)

for x, y, w, h in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 3)

cv2.imwrite("Section 12_Image processing/images/humans_faces.jpeg", image)
