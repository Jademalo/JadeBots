#-------------------------------------------------------------------------------
# Imports
#-------------------------------------------------------------------------------
import tweetBot
import keys
import os

def str2bool(v):
  return str(v).lower() in ("yes", "true", "t", "1")


#-------------------------------------------------------------------------------
# Genre Defining
#-------------------------------------------------------------------------------
def postGenreDefining():

    account = "genreDefining"
    gameFile = "genre-defining/game.txt"
    genreFile = "genre-defining/genre.txt"
    genreExtraFile = "genre-defining/genreExtra.txt"

    # Environment Variables
    postFreqGenre = int(os.environ.get("postFreqGenre"))
    postGenre = str2bool(os.environ.get("postGenre"))
    altPostFreqGenre = int(os.environ.get("altPostFreqGenre"))
    altGenreExtraFreqGenre = int(os.environ.get("altGenreExtraFreqGenre"))
    altGenreGameFreqGenre = int(os.environ.get("altGenreGameFreqGenre"))
    verboseGenre = str2bool(os.environ.get("verboseGenre"))

    # Generate the tweet
    tweetText, altGenreGameDebug, altGenreExtraDebug, gameText, genreText, altPostDebug = tweetBot.genreGen(gameFile, genreFile, genreExtraFile, altPostFreqGenre, altGenreGameFreqGenre, altGenreExtraFreqGenre)

    # If the verbose variable is set to 1, then print extra spam
    if verboseGenre == True:
        print("Alternate Game as Genre? -", altGenreGameDebug)
        print("Alternate Extra Genre? -", altGenreExtraDebug)
        print("gameText =", gameText)
        print("genreText =", genreText)
        print("Alternate format? -", altPostDebug)
    # Print the final tweet
    print(tweetText)

    # Post the tweet to Twitter
    if postGenre == True:
        consumer_key, consumer_secret, access_token, access_token_secret = keys.returnKeys(account)
        tweetBot.poster.postTweet(tweetText, consumer_key, consumer_secret, access_token, access_token_secret, postFreqGenre)



#-------------------------------------------------------------------------------
# Super Mario Variants
#-------------------------------------------------------------------------------
def postMarioVariants():

    account = "marioVariants"
    nameFile = "mario-variants/name.txt"
    prefixFile = "mario-variants/prefix.txt"
    suffixFile = "mario-variants/suffix.txt"

    # Environment Variables
    postFreqMario = int(os.environ.get("postFreqMario"))
    postMario = str2bool(os.environ.get("postMario"))
    extraPrefixPercentMario = int(os.environ.get("extraPrefixPercentMario"))
    suffixPercentMario = int(os.environ.get("suffixPercentMario"))
    verboseMario = str2bool(os.environ.get("verboseMario"))

    # Generate the tweet
    tweetText, nameText, prefixText, suffixText, prefixExtraText, prefixExtraDebug, suffixDebug = tweetBot.variantGen(nameFile, prefixFile, suffixFile, extraPrefixPercentMario, suffixPercentMario)

    # If the verbose variable is set to 1, then print extra spam
    if verboseMario == True:
        print("Extra Prefix? -", prefixExtraDebug)
        print("Suffix? -", suffixDebug)
        print("nameText =", nameText)
        print("prefixText =", prefixText)
        print("prefixExtraText =", prefixExtraText)
        print("suffixText =", suffixText)
    # Print the final tweet
    print(tweetText)

    # Post the tweet to Twitter
    if postMario == True:
        consumer_key, consumer_secret, access_token, access_token_secret = keys.returnKeys(account)
        tweetBot.poster.postTweet(tweetText, consumer_key, consumer_secret, access_token, access_token_secret, postFreqMario)



#-------------------------------------------------------------------------------
# Romantics eBooks
#-------------------------------------------------------------------------------
def postRomanticsEbooks():

    account = "romanticsEbooks"
    mainFile = "romantics-ebooks/RomanticsText.txt"

    # Environment Variables
    postFreqRomantics = int(os.environ.get("postFreqRomantics"))
    postRomantics = str2bool(os.environ.get("postRomantics"))
    maxLengthRomantics = int(os.environ.get("maxLengthRomantics"))
    minLengthRomantics = int(os.environ.get("minLengthRomantics"))

    # Generate the tweet
    tweetText = tweetBot.generator.ebooksGen(mainFile, maxLengthRomantics, minLengthRomantics)
    # Print the final tweet
    print(tweetText)
    # Post the tweet to Twitter
    if postRomantics == True:
        consumer_key, consumer_secret, access_token, access_token_secret = keys.returnKeys(account)
        tweetBot.poster.postTweet(tweetText, consumer_key, consumer_secret, access_token, access_token_secret, postFreqRomantics)



#-------------------------------------------------------------------------------
# Ulysses eBooks
#-------------------------------------------------------------------------------
def postUlyssesEbooks():

    account = "ulyssesEbooks"
    mainFile = "ulysses-ebooks/Ulysses.txt"

    # Environment Variables
    postFreqUlysses = int(os.environ.get("postFreqUlysses"))
    postUlysses = str2bool(os.environ.get("postUlysses"))
    maxLengthUlysses = int(os.environ.get("maxLengthUlysses"))
    minLengthUlysses = int(os.environ.get("minLengthUlysses"))

    # Generate the tweet
    tweetText = tweetBot.generator.ebooksGen(mainFile, maxLengthUlysses, minLengthUlysses)
    # Print the final tweet
    print(tweetText)
    # Post the tweet to Twitter
    if postUlysses == True:
        consumer_key, consumer_secret, access_token, access_token_secret = keys.returnKeys(account)
        tweetBot.poster.postTweet(tweetText, consumer_key, consumer_secret, access_token, access_token_secret, postFreqUlysses)
