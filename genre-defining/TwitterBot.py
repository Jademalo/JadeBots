import random, tweepy

postFrequency = 1
altFrequency = 10

# personal details
consumer_key =""
consumer_secret =""
access_token =""
access_token_secret =""

# authentication of consumer key and secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# authentication of access token and secret
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)



genreFile = open("genre.txt", "r")
gameFile = open("game.txt", "r")

genreString = genreFile.read()
gameString = gameFile.read()
print(genreString)
print(gameString)

genreList = genreString.split("\n")
gameList = gameString.split("\n")
print(genreList)
print(gameList)

genreNumber =len(genreList)
gameNumber = len(gameList)
print(genreNumber)
print(gameNumber)




#tweetStart = int(random.random()*(len(poemString)-140))
#workingTweet = poemString[tweetStart:tweetStart+tweetLength].split(" ")

genrePick = int(random.randint(2,genreNumber)) #Two since there is an extra entry appended on the list
gamePick = int(random.randint(2,gameNumber))
genrePick = genrePick - 2 #One for zero being the first, and another for the blank line at the end
gamePick = gamePick - 2
print(genrePick)
print(gamePick)

genreText = genreList[genrePick]
gameText = gameList[gamePick]
print(genreText)
print(genreList)

#workingTweet = poemString[tweetStart:tweetStart+tweetLength].split(" ")

altPost = int(random.randint(1,altFrequency))
print("Alt format if = 1",)
print(altPost)

if altPost == 1:
    workingTweet = ("What if ", gameText, " was a ", genreText, "?")
    finalTweet = "".join(workingTweet)
    print(finalTweet)
else:
    workingTweet = ("Is ", gameText, " a ", genreText, "?")
    finalTweet = "".join(workingTweet)
    print(finalTweet)


tweetPost = int(random.randint(1,postFrequency))
print("Will Post (If = 1) =",)
print(tweetPost)

if tweetPost == 1:
    # update the status
    api.update_status(status = finalTweet)
