from pydub import AudioSegment
from pydub.playback import play
from pydub.silence import split_on_silence
from tkFileDialog import askopenfilename
import Tkinter as tk

'''def getAudio(song1, song2, song3):
	sound = [
 AudioSegment.from_file(song1),
 AudioSegment.from_file(song2),
 AudioSegment.from_file(song3)
 ]
 	return sound'''
 
def mixAudio(song1, song2, song3):
	#root = tk.Tk()
	#root.withdraw()
	sound = [
 AudioSegment.from_file(song1),
 AudioSegment.from_file(song2),
 AudioSegment.from_file(song3)
 ]
	"""song1 = askopenfilename()
	song2 = askopenfilename()
	song3 = askopenfilename()   """
	combineds = AudioSegment.empty()
	hope = AudioSegment.empty()
	ms = 3000
	beat = AudioSegment.silent(duration=ms).overlay(sound[1]).overlay(sound[2],position=ms//2) * 4
	for song in sound:
		combined = (song.overlay(beat) * 2).fade_in(1000).fade_out(1000).reverse
        	combined = (song.overlay(beat) * 2).fade_in(1000).fade_out(1000).set_channels(1)
        	combineds += combined
    	#three minutes is : 180000ms & 45 seconds is : 45000 = 225000(3:45)
	#combined[1500:1900]= (song.overlay(beat)*2).fade_in(1000).fade_out(1000).reverse

	hope += combineds[:225000]
	hope = hope.fade_in(30)
	hope = hope.fade_out(30)

	hope.export("combined9.wav", format='wav')
	return hope
mixAudio("Bilando.wav", "riverflowsinyou.wav","tearinmyheart.wav")	
#mixAudio("Bilando.wav","ILikeIt.wav", "VivirMiVida.wav")
#play(hope)
    #sourcefile_wav = gb.glob("*.wav")
    
    #return sourcefile_wav[3]
