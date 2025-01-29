import praw
from gtts import gTTS
import os
from dotenv import load_dotenv

load_dotenv()

#Global var to store posts downloaded
postsDict = {"Title": [], "Post Text": []}


def getPosts(subredditTitle, numberOfPosts):
    #Creating a reddit instance - XX need to connect config.txt file here XX
    redditReadOnly = praw.Reddit(client_id=os.getenv("CLIENT_ID"), 
                                client_secret=os.getenv("CLIENT_SECRET"), 
                                user_agent=os.getenv("USER_AGENT"))

    #Set target subreddit here
    TargetSubReddit = redditReadOnly.subreddit(subredditTitle)

    posts = TargetSubReddit.hot(limit=(numberOfPosts+2)) # Set to plus two as we need to cut the first two elements from the dictionary to avoid reddit top posts etc. 

    #Extract posts
    for post in posts:
        postsDict["Title"].append(post.title)
        postsDict["Post Text"].append(post.selftext)

    

def generateAudio(subredditTitle, numberOfPosts):
    language = "en"
    
    #Get reddit posts - might need more input validation for speical charcaters etc. in titles and text bodies
    getPosts(subredditTitle, numberOfPosts)

    for i in range (2, len(postsDict["Title"])):
        text = postsDict["Title"][i] + " " + postsDict["Post Text"][i]
        myObj = gTTS(text=text, lang=language, slow=False)
        myObj.save("./Audio/audio"+str(i)+".mp3")

