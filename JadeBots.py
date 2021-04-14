#-------------------------------------------------------------------------------
# Imports
#-------------------------------------------------------------------------------
import tweetBot
import os

# Quick little function to convert a text string to a boolean
def str2bool(v):
  return str(v).lower() in ("yes", "true", "t", "1")


#-------------------------------------------------------------------------------
# Function for returning the keys from environment variables
#-------------------------------------------------------------------------------
def getKeys():

    consumer_key = os.environ.get("CONSUMER_TOKEN")
    consumer_secret = os.environ.get("CONSUMER_SECRET")
    access_token = os.environ.get("ACCESS_TOKEN")
    access_token_secret = os.environ.get("ACCESS_SECRET")

    return consumer_key, consumer_secret, access_token, access_token_secret;


#-------------------------------------------------------------------------------
# Genre Defining
#-------------------------------------------------------------------------------
def postGenreDefining():

    account = "genreDefining"
    gameFile = "genre-defining/game.txt"
    genreFile = "genre-defining/genre.txt"
    genreExtraFile = "genre-defining/genreExtra.txt"

    # Environment Variables
    postFreq = int(os.environ.get("postFreq"))
    post = str2bool(os.environ.get("post"))
    altPostFreq = int(os.environ.get("altPostFreq"))
    altGenreExtraFreq = int(os.environ.get("altGenreExtraFreq"))
    altGenreGameFreq = int(os.environ.get("altGenreGameFreq"))
    verbose = str2bool(os.environ.get("verbose"))

    # Generate the tweet
    tweetText, altGenreGameDebug, altGenreExtraDebug, gameText, genreText, altPostDebug = tweetBot.genreGen(gameFile, genreFile, genreExtraFile, altPostFreq, altGenreGameFreq, altGenreExtraFreq)

    # If the verbose variable is set to 1, then print extra spam
    if verbose == True:
        print("Alternate Game as Genre? -", altGenreGameDebug)
        print("Alternate Extra Genre? -", altGenreExtraDebug)
        print("gameText =", gameText)
        print("genreText =", genreText)
        print("Alternate format? -", altPostDebug)
    # Print the final tweet
    print(tweetText)

    # Post the tweet to Twitter
    if post == True:
        consumer_key, consumer_secret, access_token, access_token_secret = getKeys()
        tweetBot.poster.postTweet(tweetText, consumer_key, consumer_secret, access_token, access_token_secret, postFreq)



#-------------------------------------------------------------------------------
# Super Mario Variants
#-------------------------------------------------------------------------------
def postMarioVariants():

    account = "marioVariants"
    nameFile = "mario-variants/name.txt"
    prefixFile = "mario-variants/prefix.txt"
    suffixFile = "mario-variants/suffix.txt"

    # Environment Variables
    postFreq = int(os.environ.get("postFreq"))
    post = str2bool(os.environ.get("post"))
    extraPrefixPercent = int(os.environ.get("extraPrefixPercent"))
    suffixPercent = int(os.environ.get("suffixPercent"))
    verbose = str2bool(os.environ.get("verbose"))

    # Generate the tweet
    tweetText, nameText, prefixText, suffixText, prefixExtraText, prefixExtraDebug, suffixDebug = tweetBot.variantGen(nameFile, prefixFile, suffixFile, extraPrefixPercent, suffixPercent)

    # If the verbose variable is set to 1, then print extra spam
    if verbose == True:
        print("Extra Prefix? -", prefixExtraDebug)
        print("Suffix? -", suffixDebug)
        print("nameText =", nameText)
        print("prefixText =", prefixText)
        print("prefixExtraText =", prefixExtraText)
        print("suffixText =", suffixText)
    # Print the final tweet
    print(tweetText)

    # Post the tweet to Twitter
    if post == True:
        consumer_key, consumer_secret, access_token, access_token_secret = getKeys()
        tweetBot.poster.postTweet(tweetText, consumer_key, consumer_secret, access_token, access_token_secret, postFreq)



#-------------------------------------------------------------------------------
# Romantics eBooks
#-------------------------------------------------------------------------------
def postRomanticsEbooks():

    account = "romanticsEbooks"
    mainFile = "romantics-ebooks/RomanticsText.txt"

    # Environment Variables
    postFreq = int(os.environ.get("postFreq"))
    post = str2bool(os.environ.get("post"))
    maxLength = int(os.environ.get("maxLength"))
    minLength = int(os.environ.get("minLength"))

    # Generate the tweet
    tweetText = tweetBot.generator.ebooksGen(mainFile, maxLength, minLength)
    # Print the final tweet
    print(tweetText)
    # Post the tweet to Twitter
    if post == True:
        consumer_key, consumer_secret, access_token, access_token_secret = getKeys()
        tweetBot.poster.postTweet(tweetText, consumer_key, consumer_secret, access_token, access_token_secret, postFreq)



#-------------------------------------------------------------------------------
# Ulysses eBooks
#-------------------------------------------------------------------------------
def postUlyssesEbooks():

    account = "ulyssesEbooks"
    mainFile = "ulysses-ebooks/Ulysses.txt"

    # Environment Variables
    postFreq = int(os.environ.get("postFreq"))
    post = str2bool(os.environ.get("post"))
    maxLength = int(os.environ.get("maxLength"))
    minLength = int(os.environ.get("minLength"))

    # Generate the tweet
    tweetText = tweetBot.generator.ebooksGen(mainFile, maxLength, minLength)
    # Print the final tweet
    print(tweetText)
    # Post the tweet to Twitter
    if post == True:
        consumer_key, consumer_secret, access_token, access_token_secret = getKeys()
        tweetBot.poster.postTweet(tweetText, consumer_key, consumer_secret, access_token, access_token_secret, postFreq)
