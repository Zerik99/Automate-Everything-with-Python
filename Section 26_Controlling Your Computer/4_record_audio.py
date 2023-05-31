""" A simple app to record audio from your microphone and save it to a file."""
import sounddevice as sd
from scipy.io.wavfile import write

seconds = 5
fps = 44100

myrecording = sd.rec(int(seconds * fps), samplerate=fps, channels=2)
sd.wait()
write("Section 26_Controlling Your Computer/files/output.mp3", fps, myrecording)
