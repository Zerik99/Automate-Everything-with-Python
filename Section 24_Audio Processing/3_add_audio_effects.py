from pydub import AudioSegment

# base audio
original_audio = AudioSegment.from_wav("Section 24_Audio Processing/files/beat.wav")

low_pass = original_audio.low_pass_filter(2000)
low_pass.export("Section 24_Audio Processing/files/low_pass.wav", format="wav")

high_pass = original_audio.high_pass_filter(2000)
high_pass.export("Section 24_Audio Processing/files/high_pass.wav", format="wav")

beat_left = original_audio.pan(-0.5)
beat_left.export("Section 24_Audio Processing/files/beat_left.wav", format="wav")
