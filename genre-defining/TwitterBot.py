import random, tweepy


#-------------------------------------------------------------------------------
# Random frequency variables

postFreq = 1
altPostFreq = 12
altGenreExtraFreq = 16
altGenreGameFreq = 24


#-------------------------------------------------------------------------------
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


#-------------------------------------------------------------------------------
# Opening the file and turning the games/genres into lists

gameFile = open("game.txt", "r")
gameString = gameFile.read()
#print("gameString =", gameString)
gameList = gameString.split("\n")
#print("gameList =", gameList)
gameList = list(filter(None, gameList))
print("gameList =", gameList)

genreFile = open("genre.txt", "r")
genreString = genreFile.read()
#print("genreString =", genreString)
genreList = genreString.split("\n")
#print("genreList =", genreList)
genreList = list(filter(None, genreList))
print("genreList =", genreList)

genreExtraFile = open("genreExtra.txt", "r")
genreExtraString = genreExtraFile.read()
#print("genreExtraString =", genreExtraString)
genreExtraList = genreExtraString.split("\n")
#print("genreExtraList =", genreExtraList)
genreExtraList = list(filter(None, genreExtraList))
print("genreExtraList =", genreExtraList)


#-------------------------------------------------------------------------------
# Generating random values from the list

gameNumber = len(gameList)
#print("gameNumber =", gameNumber)

gamePick = int(random.randint(1,gameNumber))
gamePick = gamePick - 1                                                         #One for zero being the first
#print("gamePick =", gamePick)


genreNumber = len(genreList)
#print("genreNumber =", genreNumber)

genrePick = int(random.randint(1,genreNumber))
genrePick = genrePick - 1                                                       #One for zero being the first
#print("genrePick =", genrePick)


genreExtraNumber = len(genreExtraList)
#print("genreExtraNumber =", genreExtraNumber)

genreExtraPick = int(random.randint(1,genreExtraNumber))
genreExtraPick = genreExtraPick - 1                                             #One for zero being the first
#print("genreExtraPick =", genreExtraPick)


#-------------------------------------------------------------------------------
# Picking a word using those values

gameText = gameList[gamePick]
print("gameText =", gameText)

altGenreExtra = int(random.randint(1,altGenreExtraFreq))
#print("altGenreExtra =", altGenreExtra)
altGenreGame = int(random.randint(1,altGenreGameFreq))
#print("altGenreGame =", altGenreGame)

if altGenreGame == 1:
    altGenreExtraDebug = ("No")
    altGenreGameDebug = ("Yes")
    gamePickGenre = int(random.randint(2,gameNumber))
    gamePickGenre = gamePickGenre - 2
    gameTextGenre = gameList[gamePickGenre]
    #print("gameTextGenre =", gameTextGenre)
    workingGenre = (gameTextGenre, "like")
    gamelikeGenre = "".join(workingGenre)
    genreText = gamelikeGenre
elif altGenreExtra == 1:
    altGenreExtraDebug = ("Yes")
    altGenreGameDebug = ("No")
    genreText = genreExtraList[genreExtraPick]
else:
    altGenreExtraDebug = ("No")
    altGenreGameDebug = ("No")
    genreText = genreList[genrePick]

print("Alternate Game as Genre? -", altGenreGameDebug)
print("Alternate Extra Genre? -", altGenreExtraDebug)
print("genreText =", genreText)


#-------------------------------------------------------------------------------
# Working out of "a" or "an" is needed
if genreText[0] == ("a") or genreText[0] == ("e") or genreText[0] == ("i") or genreText[0] == ("o") or genreText[0] == ("u") or genreText[0] == ("A") or genreText[0] == ("E") or genreText[0] == ("I") or genreText[0] == ("O") or genreText[0] == ("U"):
    connectText = (" an ")
else:
    connectText = (" a ")

#-------------------------------------------------------------------------------
# Compositing the final tweet

# Logic to decide if alternate format
altPost = int(random.randint(1,altPostFreq))
#print("altPost = ", altPost)

# If statement to change the format of the question, then composite the final tweet
if altPost == 1:
    altPostDebug = ("Yes")
    workingTweet = ("What if ", gameText, " was", connectText, genreText, "?")
else:
    altPostDebug = ("No")
    workingTweet = ("Is ", gameText, connectText, genreText, "?")

finalTweet = "".join(workingTweet)
print("Alternate format? -", altPostDebug)
print("finalTweet =", finalTweet)


#-------------------------------------------------------------------------------
# Posting the Tweet

tweetPost = int(random.randint(1,postFreq))
#print("tweetPost =", tweetPost)

if tweetPost == 1:
    tweetPostDebug = ("Yes")
#    api.update_status(status = finalTweet)                                      #Update the Status
else:
    tweetPostDebug = ("No")

print("Post Tweet? -", tweetPostDebug)
