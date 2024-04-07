from pydub import AudioSegment

def trans_mp3_to_wav(filepath):
    song = AudioSegment.from_mp3(filepath)
    song.export("D:\python文件\py脚本\嵌入式上机\Bandari.wav", format="wav")

trans_mp3_to_wav("D:\python文件\py脚本\嵌入式上机\ 1.mp3")
