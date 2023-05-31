from pydub import AudioSegment

# base audio
original_audio = AudioSegment.from_wav("Section 24_Audio Processing/files/beat.wav")

# Overlaying audio
overlay_audio = AudioSegment.from_wav("Section 24_Audio Processing/files/sax.wav")

beat2 = original_audio * 2
beat2.export("Section 24_Audio Processing/files/beat2.wav", format="wav")

mixed = beat2.overlay(overlay_audio)
mixed.export("Section 24_Audio Processing/files/mixed.wav", format="wav")
