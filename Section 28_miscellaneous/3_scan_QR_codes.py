import cv2

image = cv2.imread("Section 28_miscellaneous/files/qr.png")
detector = cv2.QRCodeDetector()

url, coords, pixels = detector.detectAndDecode(image)
