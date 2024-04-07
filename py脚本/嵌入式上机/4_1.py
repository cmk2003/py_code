from pydub import AudioSegment
def trans_mp3_to_wav(filepath):
    song = AudioSegment.from_mp3(filepath)
    song.export("/home/pi/Music/Bandari.wav",format="wav")


trans_mp3_to_wav("/home/pi/Music/Bandari.mp3")
