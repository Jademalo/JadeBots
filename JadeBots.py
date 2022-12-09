#-------------------------------------------------------------------------------
# Imports
#-------------------------------------------------------------------------------
import tweetBot
import os
import dotenv
import logging



#-------------------------------------------------------------------------------
# Functions
#-------------------------------------------------------------------------------

# Function to get a variable from the environment if it's empty
def getVar(var, name):
    if var is None:
        return os.getenv(name)
    else:
        return var



#-------------------------------------------------------------------------------
# Genre Defining
#-------------------------------------------------------------------------------
def postGenreDefining(postTwitter=None, twitterKeys=None, postMastodon=None, mastodonKeys=None, postFreq=None, altPostFreq=None, altGenreExtraFreq=None, altGenreGameFreq=None):

    dotenv.load_dotenv() # Does not override existing env variables

    # Generate the message
    text = tweetBot.genreGen(
        gameFile = "genre-defining/game.txt", 
        genreFile = "genre-defining/genre.txt", 
        genreExtraFile = "genre-defining/genreExtra.txt", 
        altPostFreq = getVar(altPostFreq, "ALT_POST_FREQ"), 
        altGenreGameFreq = getVar(altGenreGameFreq, "ALT_GENRE_GAME_FREQ"), 
        altGenreExtraFreq = getVar(altGenreExtraFreq, "ALT_GENRE_EXTRA_FREQ")
        )

    # Post the message
    tweetBot.post(
        text = text, 
        postFreq = getVar(postFreq, "POST_FREQ"), 
        twitterPost = getVar(postTwitter, "POST_TWITTER"), 
        twitterKeys = twitterKeys, 
        mastodonPost = getVar(postMastodon, "POST_MASTODON"), 
        mastodonKeys = mastodonKeys
        )



#-------------------------------------------------------------------------------
# Super Mario Variants
#-------------------------------------------------------------------------------
def postMarioVariants(postTwitter=None, twitterKeys=None, postMastodon=None, mastodonKeys=None, postFreq=None, extraPrefixPercent=None, suffixPercent=None):

    dotenv.load_dotenv() # Does not override existing env variables

    # Generate the message
    text = tweetBot.variantGen(
        nameFile = "mario-variants/name.txt", 
        prefixFile = "mario-variants/prefix.txt", 
        suffixFile = "mario-variants/suffix.txt", 
        extraPrefixPercent = getVar(extraPrefixPercent, "EXTRA_PREFIX_PERCENT"), 
        suffixPercent = getVar(suffixPercent, "SUFFIX_PERCENT")
        )

    # Post the message
    tweetBot.post(
        text = text, 
        postFreq = getVar(postFreq, "POST_FREQ"), 
        twitterPost = getVar(postTwitter, "POST_TWITTER"), 
        twitterKeys = twitterKeys, 
        mastodonPost = getVar(postMastodon, "POST_MASTODON"), 
        mastodonKeys = mastodonKeys
        )



#-------------------------------------------------------------------------------
# Romantics eBooks
#-------------------------------------------------------------------------------
def postRomanticsEbooks(postTwitter=None, twitterKeys=None, postMastodon=None, mastodonKeys=None, postFreq=None, minLength=None, maxLength=None):

    dotenv.load_dotenv() # Does not override existing env variables

    # Generate the message
    text = tweetBot.ebooksGen(
        file = "romantics-ebooks/RomanticsText.txt", 
        minLength = getVar(minLength, "MIN_LENGTH"),
        maxLength = getVar(maxLength, "MAX_LENGTH") 
        )

    # Post the message
    tweetBot.post(
        text = text, 
        postFreq = getVar(postFreq, "POST_FREQ"), 
        twitterPost = getVar(postTwitter, "POST_TWITTER"), 
        twitterKeys = twitterKeys, 
        mastodonPost = getVar(postMastodon, "POST_MASTODON"), 
        mastodonKeys = mastodonKeys
        )



#-------------------------------------------------------------------------------
# Ulysses eBooks
#-------------------------------------------------------------------------------
def postUlyssesEbooks(postTwitter=None, twitterKeys=None, postMastodon=None, mastodonKeys=None, postFreq=None, minLength=None, maxLength=None):

    dotenv.load_dotenv() # Does not override existing env variables

    # Generate the message
    text = tweetBot.ebooksGen(
        file = "ulysses-ebooks/Ulysses.txt", 
        minLength = getVar(minLength, "MIN_LENGTH"),
        maxLength = getVar(maxLength, "MAX_LENGTH") 
        )

    # Post the message
    tweetBot.post(
        text = text, 
        postFreq = getVar(postFreq, "POST_FREQ"), 
        twitterPost = getVar(postTwitter, "POST_TWITTER"), 
        twitterKeys = twitterKeys, 
        mastodonPost = getVar(postMastodon, "POST_MASTODON"), 
        mastodonKeys = mastodonKeys
        )



#-------------------------------------------------------------------------------
# Main Function
#-------------------------------------------------------------------------------

# Run the four bots if this file is run directly
if __name__ == "__main__":

    logging.basicConfig(level = logging.DEBUG)

    logging.info("~Genre Defining~")
    postGenreDefining(postTwitter=False, postMastodon=False)
    print()

    logging.info("~Super Mario Variants~")
    postMarioVariants(postTwitter=False, postMastodon=False)
    print()

    logging.info("~Romantics eBooks~")
    postRomanticsEbooks(postTwitter=False, postMastodon=False)
    print()

    logging.info("~Ulysses eBooks~")
    postUlyssesEbooks(postTwitter=False, postMastodon=False)
