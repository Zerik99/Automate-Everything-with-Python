import cv2
from pandas import Timestamp

frames_folder = "section 13_Webcam Capture and Video Processing/files/frames"

video = cv2.VideoCapture(
    "section 13_Webcam Capture and Video Processing/files/video.mp4"
)

width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
nr_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
fps = int(video.get(cv2.CAP_PROP_FPS))
DURATION: float = nr_frames / fps
TIMESTAMP: float = 1.88  # in seconds
timestampframe: int = round(TIMESTAMP * fps)
print(
    "Width: ",
    width,
    " Height: ",
    height,
    " Frames: ",
    nr_frames,
    " FPS: ",
    fps,
    " Duration: ",
    DURATION,
    " Timestamp: ",
    TIMESTAMP,
    " TimestampFrame: ",
    timestampframe,
)

success, frame = video.read()
count: int = 1

# with time stamp
# while success:
#     if count == timestampframe:
#         cv2.imwrite(f"{frames_folder}/frame-{count}.jpg", frame)
#         break
#     success, frame = video.read()
#     count += 1

# no time stamp
# while success:
#     cv2.imwrite(f"{frames_folder}/frame-{count}.jpg", frame)
#     success, frame = video.read()
#     count += 1
