from pydub import AudioSegment

original_audio = AudioSegment.from_wav("Section 24_Audio Processing/files/beat.wav")

reversed_audio = original_audio.reverse()
reversed_audio.export(
    "Section 24_Audio Processing/files/reversed_beat.wav", format="wav"
)

first_two = original_audio[0:2000]
first_two.export("Section 24_Audio Processing/files/first_2_seconds.wav", format="wav")

merged_audio = original_audio + reversed_audio
merged_audio.export("Section 24_Audio Processing/files/merged_audio.wav", format="wav")
