from Vocalyze import vocalyze
from IPython.display import Audio as play

model = vocalyze('car songs/XXXTentacion_-_Moonlight_(Lyrics)_(256k).mp3')
signal,sr = model.get_signal()

vocals = model.vocal_regions()
play(vocals,rate=22050)


