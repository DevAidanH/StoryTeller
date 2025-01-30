#Aidan Humpidge
#Story Teller
#29/01/2025

from redditScraper import generateAudio
from videoGen import createVideo

subredditTitle = "TwoSentenceHorror" #Change to use input

#Main app
print("XXXXXXXXXXXXXXXXXXXXXXXXXXX")
print("Welcome to Story Teller")
print("XXXXXXXXXXXXXXXXXXXXXXXXXXX")
numberOfPosts = input("Please input how many top posts you want to get >>> ")
print("Scraping reddit...")
print("Generating audio...")
generateAudio(subredditTitle, int(numberOfPosts))
print("Creating video...")
createVideo()
print("Program complete")