import cv2


def main():
    """Find faces in a video"""
    FACE_CASCADE = cv2.CascadeClassifier(
        "section 13_Webcam Capture and Video Processing/faces.xml"
    )

    video = cv2.VideoCapture(0)
    success, frame = video.read()

    output = cv2.VideoWriter(
        "section 13_Webcam Capture and Video Processing/files/output_webcam.avi",
        cv2.VideoWriter_fourcc(*"DIVX"),
        30,
        (frame.shape[1], frame.shape[0]),
    )

    while success:
        detect_faces(frame, FACE_CASCADE, output)
        key = cv2.waitKey(1)
        if key == ord("q"):
            break
        success, frame = video.read()

    output.release()
    video.release()
    cv2.destroyAllWindows()


def detect_faces(_frame, _face_cascade: cv2.CascadeClassifier, _video) -> None:
    """Detect faces in a frame and draw a rectangle around them"""
    faces = _face_cascade.detectMultiScale(_frame, 1.1, 4)
    for x, y, w, h in faces:
        cv2.rectangle(_frame, (x, y), (x + w, y + h), (255, 0, 0), 3)
    cv2.imshow("Recording", _frame)
    _video.write(_frame)


if __name__ == "__main__":
    main()
