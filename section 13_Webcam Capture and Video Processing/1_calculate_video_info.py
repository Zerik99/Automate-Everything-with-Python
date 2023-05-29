import cv2

video = cv2.VideoCapture(
    "section 13_Webcam Capture and Video Processing/files/video.mp4"
)

width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
num_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
fps = int(video.get(cv2.CAP_PROP_FPS))

print("Width: ", width, " Height: ", height, " Frames: ", num_frames, " FPS: ", fps)
