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
def postGenreDefining(postTwitter=None, twitterKeys=None, postMastodon=None, mastodonKeys=None, postFreq=None, altPostFreq=None, altGenreExtraFreq=None, altGenreGameFreq=None, verbose=None):

    account = "genreDefining"
    gameFile = "genre-defining/game.txt"
    genreFile = "genre-defining/genre.txt"
    genreExtraFile = "genre-defining/genreExtra.txt"

    # Load from Environment Variables if variables aren't passed
    dotenv.load_dotenv()
    postTwitter = str2bool(os.getenv("POST_TWITTER")) if postTwitter is None else postTwitter #postTwitter should be set to the environment variable if it is equal to None, else it should be set to itself.
    postMastodon = str2bool(os.getenv("POST_MASTODON")) if postMastodon is None else postMastodon
    postFreq = int(os.getenv("POST_FREQ")) if postFreq is None else postFreq
    altPostFreq = int(os.getenv("ALT_POST_FREQ")) if altPostFreq is None else altPostFreq
    altGenreExtraFreq = int(os.getenv("ALT_GENRE_EXTRA_FREQ")) if altGenreExtraFreq is None else altGenreExtraFreq
    altGenreGameFreq = int(os.getenv("ALT_GENRE_GAME_FREQ")) if altGenreGameFreq is None else altGenreGameFreq
    verbose = str2bool(os.getenv("VERBOSE")) if verbose is None else verbose

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
    tweetBot.post(text, postFreq, postTwitter, twitterKeys, postMastodon, mastodonKeys)



#-------------------------------------------------------------------------------
# Super Mario Variants
#-------------------------------------------------------------------------------
def postMarioVariants(postTwitter=None, twitterKeys=None, postMastodon=None, mastodonKeys=None, postFreq=None, extraPrefixPercent=None, suffixPercent=None, verbose=None):

    account = "marioVariants"
    nameFile = "mario-variants/name.txt"
    prefixFile = "mario-variants/prefix.txt"
    suffixFile = "mario-variants/suffix.txt"

    # Environment Variables
    dotenv.load_dotenv()
    postTwitter = str2bool(os.getenv("POST_TWITTER")) if postTwitter is None else postTwitter #postTwitter should be set to the environment variable if it is equal to None, else it should be set to itself.
    postMastodon = str2bool(os.getenv("POST_MASTODON")) if postMastodon is None else postMastodon
    postFreq = int(os.getenv("POST_FREQ")) if postFreq is None else postFreq
    extraPrefixPercent = int(os.getenv("EXTRA_PREFIX_PERCENT")) if extraPrefixPercent is None else extraPrefixPercent
    suffixPercent = int(os.getenv("SUFFIX_PERCENT")) if suffixPercent is None else suffixPercent
    verbose = str2bool(os.getenv("VERBOSE")) if verbose is None else verbose

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
    tweetBot.post(text, postFreq, postTwitter, twitterKeys, postMastodon, mastodonKeys)



#-------------------------------------------------------------------------------
# Romantics eBooks
#-------------------------------------------------------------------------------
def postRomanticsEbooks(postTwitter=None, twitterKeys=None, postMastodon=None, mastodonKeys=None, postFreq=None, minLength=None, maxLength=None):

    account = "romanticsEbooks"
    mainFile = "romantics-ebooks/RomanticsText.txt"

    # Environment Variables
    dotenv.load_dotenv()
    postTwitter = str2bool(os.getenv("POST_TWITTER")) if postTwitter is None else postTwitter #postTwitter should be set to the environment variable if it is equal to None, else it should be set to itself.
    postMastodon = str2bool(os.getenv("POST_MASTODON")) if postMastodon is None else postMastodon
    postFreq = int(os.getenv("POST_FREQ")) if postFreq is None else postFreq
    minLength = int(os.getenv("MIN_LENGTH")) if minLength is None else minLength
    maxLength = int(os.getenv("MAX_LENGTH")) if maxLength is None else maxLength

    # Generate the message
    text = tweetBot.ebooksGen(mainFile, maxLength, minLength)

    # Print the final message
    print(text)
    # Post the message
    tweetBot.post(text, postFreq, postTwitter, twitterKeys, postMastodon, mastodonKeys)



#-------------------------------------------------------------------------------
# Ulysses eBooks
#-------------------------------------------------------------------------------
def postUlyssesEbooks(postTwitter=None, twitterKeys=None, postMastodon=None, mastodonKeys=None, postFreq=None, minLength=None, maxLength=None):

    account = "ulyssesEbooks"
    mainFile = "ulysses-ebooks/Ulysses.txt"

    # Environment Variables
    dotenv.load_dotenv()
    postTwitter = str2bool(os.getenv("POST_TWITTER")) if postTwitter is None else postTwitter #postTwitter should be set to the environment variable if it is equal to None, else it should be set to itself.
    postMastodon = str2bool(os.getenv("POST_MASTODON")) if postMastodon is None else postMastodon
    postFreq = int(os.getenv("POST_FREQ")) if postFreq is None else postFreq
    minLength = int(os.getenv("MIN_LENGTH")) if minLength is None else minLength
    maxLength = int(os.getenv("MAX_LENGTH")) if maxLength is None else maxLength

    # Generate the message
    text = tweetBot.ebooksGen(mainFile, maxLength, minLength)

    # Print the final message
    print(text)
    # Post the message
    tweetBot.post(text, postFreq, postTwitter, twitterKeys, postMastodon, mastodonKeys)
