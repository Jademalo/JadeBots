#-------------------------------------------------------------------------------
# Imports
#-------------------------------------------------------------------------------
import tweetBot


#-------------------------------------------------------------------------------
# Genre Defining
#-------------------------------------------------------------------------------
def postGenreDefining(verbose=0):

    account = "genreDefining"
    #postFreq = 4
    postFreq = 0

    altPostFreq = 12
    altGenreExtraFreq = 16
    altGenreGameFreq = 24

    gameFile = "genre-defining/game.txt"
    genreFile = "genre-defining/genre.txt"
    genreExtraFile = "genre-defining/genreExtra.txt"

    # Generate the tweet
    tweetText, altGenreGameDebug, altGenreExtraDebug, gameText, genreText, altPostDebug = tweetBot.genreTweet(gameFile, genreFile, genreExtraFile, altPostFreq, altGenreGameFreq, altGenreExtraFreq)

    # If the verbose variable is set to 1, then print extra spam
    if verbose == 1:
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
def postRomanticsEbooks():

    account = "romanticsEbooks"
    #postFreq = 15
    postFreq = 0

    mainFile = "romantics-ebooks/RomanticsText.txt"

    # Generate the tweet
    tweetText = tweetBot.ebooksTweet(mainFile)
    # Print the final tweet
    print(tweetText)
    # Post the tweet to Twitter
    tweetBot.postTweet(tweetText, account, postFreq)



#-------------------------------------------------------------------------------
# Ulysses eBooks
#-------------------------------------------------------------------------------
def postUlyssesEbooks():

    account = "ulyssesEbooks"
    #postFreq = 15
    postFreq = 0

    mainFile = "ulysses-ebooks/Ulysses.txt"
    # Generate the tweet
    tweetText = tweetBot.ebooksTweet(mainFile)
    # Print the final tweet
    print(tweetText)
    # Post the tweet to Twitter
    tweetBot.postTweet(tweetText, account, postFreq)



#-------------------------------------------------------------------------------
# Main Functions
#-------------------------------------------------------------------------------

verbose = True


print("~Genre Defining~")
postGenreDefining(verbose)

print("\n~Romantics eBooks~")
postRomanticsEbooks()

print("\n~Ulysses eBooks~")
postUlyssesEbooks()
