# Story Teller
## A Python script to generate Youtube shorts

### Working idea
Write a script that will scrape certain reddit subs and take a text post. Convert this text post into a script and create an audio file of this being read. Then either scrape stock video footage or generate something relevant using AI. Place the audio ontop of the footage and upload to YT or Instagram. 

### Actions to be completed
* Generate subtitles
* Edit video together and format
* Upload to YouTube / Instagram

### Completed actions
* Scrape data from reddit
* Convert reddit data to audio
* Take a random clip from a collection of minecraft footage

### Issues
* Would like to find a better text-to-speech then GTTS for future iterations 
* There is an issue with audio length at the time of writing, need to include code to select a max length of each reddit post or skip it. 
* Program cause an error the first time it runs but then works the second time. This is all a probem with the subtitles generatetion - might try and seperate these later