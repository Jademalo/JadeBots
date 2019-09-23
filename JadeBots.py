#-------------------------------------------------------------------------------
# Imports
#-------------------------------------------------------------------------------
import tweetBot


#-------------------------------------------------------------------------------
# Genre Defining
#-------------------------------------------------------------------------------
def postGenreDefining(postFreq=4, altPostFreq=12, altGenreExtraFreq=16, altGenreGameFreq=24, verbose=False):

    account = "genreDefining"
    gameFile = "genre-defining/game.txt"
    genreFile = "genre-defining/genre.txt"
    genreExtraFile = "genre-defining/genreExtra.txt"

    # Generate the tweet
    tweetText, altGenreGameDebug, altGenreExtraDebug, gameText, genreText, altPostDebug = tweetBot.genreTweet(gameFile, genreFile, genreExtraFile, altPostFreq, altGenreGameFreq, altGenreExtraFreq)

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
    tweetBot.postTweet(tweetText, account, postFreq)



#-------------------------------------------------------------------------------
# Romantics eBooks
#-------------------------------------------------------------------------------
def postRomanticsEbooks(postFreq=15, maxLength=100, minLength=30):

    account = "romanticsEbooks"
    mainFile = "romantics-ebooks/RomanticsText.txt"

    # Generate the tweet
    tweetText = tweetBot.ebooksTweet(mainFile, maxLength, minLength)
    # Print the final tweet
    print(tweetText)
    # Post the tweet to Twitter
    tweetBot.postTweet(tweetText, account, postFreq)



#-------------------------------------------------------------------------------
# Ulysses eBooks
#-------------------------------------------------------------------------------
def postUlyssesEbooks(postFreq=15, maxLength=120, minLength=30):

    account = "ulyssesEbooks"
    mainFile = "ulysses-ebooks/Ulysses.txt"

    # Generate the tweet
    tweetText = tweetBot.ebooksTweet(mainFile, maxLength, minLength)
    # Print the final tweet
    print(tweetText)
    # Post the tweet to Twitter
    tweetBot.postTweet(tweetText, account, postFreq)
