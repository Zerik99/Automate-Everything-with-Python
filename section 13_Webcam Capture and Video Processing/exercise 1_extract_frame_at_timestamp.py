import cv2


def get_timestamp(_seconds: float) -> str:
    """Convert seconds to timestamp format HH:MM:SS"""
    minutes, seconds = divmod(_seconds, 60)
    hours, minutes = divmod(minutes, 60)
    seconds_format = "0%.4f"
    return f"{int(hours):02d}:{int(minutes):02d}:{seconds_format % seconds}"


def get_timestamp_frame(_timestamp: str, _fps: int) -> int:
    """Convert timestamp format HH:MM:SS to frame number"""
    _hours, _minutes, _seconds = _timestamp.split(":")
    seconds: float = float(_hours) * 3600 + float(_minutes) * 60 + float(_seconds)
    return round(seconds * _fps)


frames_folder = "section 13_Webcam Capture and Video Processing/files/frames"

video = cv2.VideoCapture(
    "section 13_Webcam Capture and Video Processing/files/video.mp4"
)

WIDTH = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
HEIGHT = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
NR_FRAMES = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
FPS = int(video.get(cv2.CAP_PROP_FPS))
DURATION: str = get_timestamp(float(NR_FRAMES / FPS))
timestamp: str = get_timestamp(1.88)
time_stamp_frame_num: int = get_timestamp_frame(timestamp, FPS)

success, frame = video.read()
count: int = 1

while success:
    if count == time_stamp_frame_num:
        cv2.imwrite(f"{frames_folder}/frame-{count}.jpg", frame)
        break
    success, frame = video.read()
    count += 1
