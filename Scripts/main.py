#Aidan Humpidge
#Story Teller
#29/01/2025

from redditScraper import generateAudio
from videoGen import createVideo

subredditTitle = "TwoSentenceHorror" #Change to use input

#Main app
numberOfPosts = input("Please input how many top posts you want to get >>> ")
generateAudio(subredditTitle, int(numberOfPosts))
createVideo()
print("Program complete")