""" A Flask application to stream live webcam feed to the browser."""
import cv2
from flask import Flask, render_template, Response

video = cv2.VideoCapture(1)


def get_frame():
    """Video streaming generator function."""
    while True:
        success, frame = video.read()
        sc, encoded_image = cv2.imencode(".jpg", frame)
        frame = encoded_image.tobytes()
        yield (b"--frame\r\ncontent-type: image/jpeg\r\n\r\n" + frame + b"\r\n")


app = Flask(__name__)


@app.route("/")
def index():
    """Video streaming home page."""
    return render_template("index.html")


@app.route("/video_feed_url")
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag.""" ""
    return Response(get_frame(), mimetype="multipart/x-mixed-replace; boundary=frame")


if __name__ == "__main__":
    app.run(debug=True)
