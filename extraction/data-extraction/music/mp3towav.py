from pydub import AudioSegment
import os

sc_list = os.listdir( 'speechnew' )
# print(sc_list)

i = 1

for file in sc_list:
    if file.endswith(".wav") and file != "UK & Ireland Dance Belters_Sonny Fodera, Gorgon City, & Danny Howard.mp3" and file != "UK & Ireland Dance Belters_Solardo Angel Dust.mp3" and file != "UK & Ireland Dance Belters_Romy & Fred again Strong.mp3" and file != "UK & Ireland Dance Belters_Sonny Fodera, Gorgon City, & Danny Howard - Remember.mp3" :
        #importing file from location by giving its path
        sound = AudioSegment.from_mp3("speechnew/"+file)
        sound = sound.set_channels(1)

        name = file.split(".wav")

        sound.export("wav-mono/"+name[0]+".wav", format="wav")

        print( "{} audio trimmed: ".format(i, 1) + name[0] + ".wav" )

        i += 1