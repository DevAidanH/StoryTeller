from moviepy import *
from moviepy.video.tools.subtitles import SubtitlesClip
from mutagen.mp3 import MP3
import os
import random
import assemblyai as aai
from dotenv import load_dotenv

load_dotenv()


def createVideo():
    audioFiles = os.listdir('./Audio')
    for i in range (len(audioFiles)): #Loop through all the audio files generated
        #Get length of audio clip
        clipLength = round((MP3("./Audio/"+audioFiles[i]).info.length), 0)
        #Default video is 965 in length so we can pick any two points between 0 and 965 which are the clipLength apart and use that for the clip. geenerate one random number and then add the duraction tot it should work
        startOfClip = random.randint(0,(int(965-clipLength))) #Add 965 into variable to allow for addiotnal footage to be used. 
        endOfClip = startOfClip+clipLength
        
        #Generate the video clip from the minecraft footage with the random times
        clip = VideoFileClip("./video/minecraftFootage.mp4").subclipped(startOfClip, endOfClip+1)
        
        audioClip = AudioFileClip("./Audio/"+audioFiles[i])

        #Adding subtitles
        subtitles("./Audio/"+audioFiles[i], i)

        generator = lambda txt: TextClip(text=txt, font='./fonts\Roboto_Condensed-Bold.ttf', font_size=24, color='white', size=(180,100), method='caption')

        subs = SubtitlesClip("subtitles"+str(i)+".srt", make_textclip=generator, encoding='utf-8')

        video = CompositeVideoClip([clip, subs.with_position(('center'))])
        video.audio = audioClip #Adding the audio file over the footage

        video.write_videofile("./Output/video"+str(i+1)+".mp4", logger=None) #Save file

        #Cleanup
        os.remove("subtitles"+str(i)+".srt")
        os.remove("./Audio/"+audioFiles[i])

#Seperate function for generating subtitle fixes unknown timeout error
def subtitles(audio, i):
    aai.settings.api_key=os.getenv("AAI_API_KEY")
    subtitlesAI = ""
    subtitlesAI = aai.Transcriber().transcribe(audio).export_subtitles_srt()
    f = open("subtitles"+str(i)+".srt", "a")
    f.write(subtitlesAI)
    f.close