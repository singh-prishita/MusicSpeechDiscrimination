# import yt_dlp

# URLS = ['https://www.youtube.com/watch?v=vnVwvPpdFeY']

# ydl_opts = {
#     'format': 'mp3/bestaudio/best',
#     # ℹ️ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
#     'postprocessors': [{  # Extract audio using ffmpeg
#         'key': 'FFmpegExtractAudio',
#         'preferredcodec': 'mp3',
#     }]
# }

# with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#     error_code = ydl.download(URLS)

from pydub import AudioSegment
import os

# sc_list = os.listdir('podcasts')
# print(sc_list)
StrtMin = 0
StrtSec = 0

EndMin = 0
EndSec = 15
sound = AudioSegment.from_mp3("speeches.mp3")
j=5
for i in range(5):
    StrtSec+=180
    EndSec+=180
    # Time to milliseconds conversion
    StrtTime = StrtMin*60*1000+StrtSec*1000
    EndTime = StrtMin*60*1000+EndSec*1000

    # Opening file and extracting portion of it
    extract = sound[StrtTime:EndTime]

        # Saving file in required location
    extract.export("speechnew/sound"+"_"+str(i)+".wav", format="wav")
    print( "audio trimmed: " + str(i) + " saved" )