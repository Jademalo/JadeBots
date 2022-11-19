#-------------------------------------------------------------------------------
# Imports
#-------------------------------------------------------------------------------
import tweetBot
import os
import dotenv

# Quick little function to convert a text string to a boolean
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
    dotenv.load_dotenv()
    postTwitter = str2bool(os.getenv("POST_TWITTER"))
    postMastodon = str2bool(os.getenv("POST_MASTODON"))
    postFreq = int(os.getenv("POST_FREQ"))
    altPostFreq = int(os.getenv("ALT_POST_FREQ"))
    altGenreExtraFreq = int(os.getenv("ALT_GENRE_EXTRA_FREQ"))
    altGenreGameFreq = int(os.getenv("ALT_GENRE_GAME_FREQ"))
    verbose = str2bool(os.getenv("VERBOSE"))

    # Generate the message
    text, altGenreGameDebug, altGenreExtraDebug, gameText, genreText, altPostDebug = tweetBot.genreGen(gameFile, genreFile, genreExtraFile, altPostFreq, altGenreGameFreq, altGenreExtraFreq)

    # If the verbose variable is set to 1, then print extra spam
    if verbose == True:
        print("Alternate Game as Genre? -", altGenreGameDebug)
        print("Alternate Extra Genre? -", altGenreExtraDebug)
        print("gameText =", gameText)
        print("genreText =", genreText)
        print("Alternate format? -", altPostDebug)

    # Print the final message
    print(text)
    # Post the message
    tweetBot.post(text, postFreq, twitterPost=postTwitter, mastodonPost=postMastodon)



#-------------------------------------------------------------------------------
# Super Mario Variants
#-------------------------------------------------------------------------------
def postMarioVariants():

    account = "marioVariants"
    nameFile = "mario-variants/name.txt"
    prefixFile = "mario-variants/prefix.txt"
    suffixFile = "mario-variants/suffix.txt"

    # Environment Variables
    dotenv.load_dotenv()
    postTwitter = str2bool(os.getenv("POST_TWITTER"))
    postMastodon = str2bool(os.getenv("POST_MASTODON"))
    postFreq = int(os.getenv("POST_FREQ"))
    extraPrefixPercent = int(os.getenv("EXTRA_PREFIX_PERCENT"))
    suffixPercent = int(os.getenv("SUFFIX_PERCENT"))
    verbose = str2bool(os.getenv("VERBOSE"))

    # Generate the message
    text, nameText, prefixText, suffixText, prefixExtraText, prefixExtraDebug, suffixDebug = tweetBot.variantGen(nameFile, prefixFile, suffixFile, extraPrefixPercent, suffixPercent)

    # If the verbose variable is set to 1, then print extra spam
    if verbose == True:
        print("Extra Prefix? -", prefixExtraDebug)
        print("Suffix? -", suffixDebug)
        print("nameText =", nameText)
        print("prefixText =", prefixText)
        print("prefixExtraText =", prefixExtraText)
        print("suffixText =", suffixText)

    # Print the final message
    print(text)
    # Post the message
    tweetBot.post(text, postFreq, twitterPost=postTwitter, mastodonPost=postMastodon)



#-------------------------------------------------------------------------------
# Romantics eBooks
#-------------------------------------------------------------------------------
def postRomanticsEbooks():

    account = "romanticsEbooks"
    mainFile = "romantics-ebooks/RomanticsText.txt"

    # Environment Variables
    dotenv.load_dotenv()
    postTwitter = str2bool(os.getenv("POST_TWITTER"))
    postMastodon = str2bool(os.getenv("POST_MASTODON"))
    postFreq = int(os.getenv("POST_FREQ"))
    minLength = int(os.getenv("MIN_LENGTH"))
    maxLength = int(os.getenv("MAX_LENGTH"))

    # Generate the message
    text = tweetBot.ebooksGen(mainFile, maxLength, minLength)

    # Print the final message
    print(text)
    # Post the message
    tweetBot.post(text, postFreq, twitterPost=postTwitter, mastodonPost=postMastodon)



#-------------------------------------------------------------------------------
# Ulysses eBooks
#-------------------------------------------------------------------------------
def postUlyssesEbooks():

    account = "ulyssesEbooks"
    mainFile = "ulysses-ebooks/Ulysses.txt"

    # Environment Variables
    dotenv.load_dotenv()
    postTwitter = str2bool(os.getenv("POST_TWITTER"))
    postMastodon = str2bool(os.getenv("POST_MASTODON"))
    postFreq = int(os.getenv("POST_FREQ"))
    minLength = int(os.getenv("MIN_LENGTH"))
    maxLength = int(os.getenv("MAX_LENGTH"))

    # Generate the message
    text = tweetBot.ebooksGen(mainFile, maxLength, minLength)

    # Print the final message
    print(text)
    # Post the message
    tweetBot.post(text, postFreq, twitterPost=postTwitter, mastodonPost=postMastodon)
