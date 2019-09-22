import random, tweepy

# Random frequency variables
postFrequency = 1
altFrequency = 8
genreFrequency = 16


# Twitter API Stuff
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



# Opening the file and turning the games/genres into lists
gameFile = open("game.txt", "r")
gameString = gameFile.read()
#print("gameString =", gameString)
gameList = gameString.split("\n")
#print("gameList =", gameList)

genreFile = open("genre.txt", "r")
genreString = genreFile.read()
#print("genreString =", genreString)
genreList = genreString.split("\n")
#print("genreList =", genreList)



#Generating random values from the list
gameNumber = len(gameList)
#print("gameNumber =", gameNumber)

gamePick = int(random.randint(2,gameNumber)) #Two since there is an extra entry appended on the list
gamePick = gamePick - 2 #One for zero being the first, and another for the blank line at the end
#print("gamePick =", gamePick)


genreNumber = len(genreList)
#print("genreNumber =", genreNumber)

genrePick = int(random.randint(2,genreNumber)) #Two since there is an extra entry appended on the list
genrePick = genrePick - 2 #One for zero being the first, and another for the blank line at the end
#print("genrePick =", genrePick)



# Picking a word using those values
gameText = gameList[gamePick]
print("gameText =", gameText)


# If statement to create a genre from a game name
altGenre = int(random.randint(1,genreFrequency))
#print("altGenre =", altGenre)

if altGenre == 1:
    altGenreDebug = ("Yes")
    gamePickGenre = int(random.randint(2,gameNumber))
    gamePickGenre = gamePickGenre - 2
    gameTextGenre = gameList[gamePickGenre]
    #print("gameTextGenre =", gameTextGenre)
    workingGenre = (gameTextGenre, "like")
    gamelikeGenre = "".join(workingGenre)
    genreText = gamelikeGenre
else:
    altGenreDebug = ("No")
    genreText = genreList[genrePick]

print("Alternate Game as Genre? -", altGenreDebug)
print("genreText =", genreText)


# Logic to decide if alternate format
altPost = int(random.randint(1,altFrequency))
#print("altPost = ", altPost)

# If statement to change the format of the question, then composite the final tweet
if altPost == 1:
    altPostDebug = ("Yes")
    workingTweet = ("What if ", gameText, " was a ", genreText, "?")
else:
    altPostDebug = ("No")
    workingTweet = ("Is ", gameText, " a ", genreText, "?")

finalTweet = "".join(workingTweet)
print("Alternate format? -", altPostDebug)
print("finalTweet =", finalTweet)

tweetPost = int(random.randint(1,postFrequency))
#print("tweetPost =", tweetPost)

if tweetPost == 1:
    tweetPostDebug = ("Yes")
    api.update_status(status = finalTweet) #Update the Status
else:
    tweetPostDebug = ("No")

print("Post Tweet? -", tweetPostDebug)
