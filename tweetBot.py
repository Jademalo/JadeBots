#-------------------------------------------------------------------------------
# Imports
#-------------------------------------------------------------------------------
import keys
import tweepy
import random


#-------------------------------------------------------------------------------
# Define the function to get the twitter acc keys and create a tweepy API object
#-------------------------------------------------------------------------------
def setTwitter(account):
    consumer_key, consumer_secret, access_token, access_token_secret = keys.returnKeys(account)

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    return api


#-------------------------------------------------------------------------------















##-------------------------------------------------------------------------------
## Opening the file and turning the games/genres into lists
#
#def fileToList(fileName):
#    fileRaw = open(fileName, "r")
#    fileString = fileRaw.read()
#    fileList = fileString.split("\n")
#    return list(filter(None, fileList))
#
#
#gameList = fileToList("game.txt")
#genreList = fileToList("genre.txt")
#genreExtraList = fileToList("genreExtra.txt")
#
#
##-------------------------------------------------------------------------------
## Functions to generate a random value and picking a word using that value
#
#def randomInt(freq):
#    return int(random.randint(1,freq))
#
#def pickString(list):
#    listNumber = len(list)                                                      # Finding the length of the list
#    return list[randomInt(listNumber) - 1]                                      # Generating a random value from that list, -1 since 0 is a value # Returning the specific value from the list based on the number generated
#
#
##-------------------------------------------------------------------------------
## Generating a Game and Genre from the lists
#
#gameText = pickString(gameList)
#
#
#altGenreGame = randomInt(altGenreGameFreq)
#altGenreGameDebug = ("No")
#altGenreExtra = randomInt(altGenreExtraFreq)
#altGenreExtraDebug = ("No")
#
#
#if altGenreGame == 1:
#    altGenreGameDebug = ("Yes")
#    genreText = pickString(gameList)
#    if genreText[-1:] == ("."):
#        genreText = genreText[:-1]                                              # If the last character is a ".", remove it
#    genreText = "".join((genreText, "like"))                                    # There are two brackets because the first set makes a string from the two values, and second joins them
#elif altGenreExtra == 1:
#    altGenreExtraDebug = ("Yes")
#    genreText = pickString(genreExtraList)
#else:
#    genreText = pickString(genreList)
#
#
#print("Alternate Game as Genre? -", altGenreGameDebug)
#print("Alternate Extra Genre? -", altGenreExtraDebug)
#print("gameText =", gameText)
#print("genreText =", genreText)
#
#
##-------------------------------------------------------------------------------
## Working out of "a" or "an" is needed
#
#if genreText[0] == ("a") or genreText[0] == ("e") or genreText[0] == ("i") or genreText[0] == ("o") or genreText[0] == ("u") or genreText[0] == ("A") or genreText[0] == ("E") or genreText[0] == ("I") or genreText[0] == ("O") or genreText[0] == ("U"):
#    connectText = (" an ")
#else:
#    connectText = (" a ")
#
#
##-------------------------------------------------------------------------------
## Compositing the final tweet
#
## Logic to decide if alternate format
#altPost = randomInt(altPostFreq)
#altPostDebug = ("No")
#
#
## If statement to change the format of the question, then composite the final tweet
#if altPost == 1:
#    altPostDebug = ("Yes")
#    workingTweet = ("What if ", gameText, " was", connectText, genreText, "?")
#else:
#    workingTweet = ("Is ", gameText, connectText, genreText, "?")
#
#finalTweet = "".join(workingTweet)
#
#
#print("Alternate format? -", altPostDebug)
#print("finalTweet =", finalTweet)
#
#
##-------------------------------------------------------------------------------
## Posting the Tweet
#
#tweetPost = randomInt(postFreq)
#tweetPostDebug = ("No")
#
#if tweetPost == 1:
#    tweetPostDebug = ("Yes")
#    api.update_status(status = finalTweet)                                     # Update the Status
#
#print("Post Tweet? -", tweetPostDebug)
