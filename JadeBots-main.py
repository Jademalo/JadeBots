#-------------------------------------------------------------------------------
# Imports
#-------------------------------------------------------------------------------
import tweetBot


#-------------------------------------------------------------------------------
# Genre Defining
#-------------------------------------------------------------------------------
def postGenreDefining():

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
    tweetText = tweetBot.genreTweet(gameFile, genreFile, genreExtraFile, altPostFreq, altGenreGameFreq, altGenreExtraFreq)
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
    print(tweetText)
    # Post the tweet to Twitter
    tweetBot.postTweet(tweetText, account, postFreq)



#-------------------------------------------------------------------------------
# Main Functions
#-------------------------------------------------------------------------------
print("~Genre Defining~")
postGenreDefining()
print("\n~Romantics eBooks~")
postRomanticsEbooks()
print("\n~Ulysses eBooks")
postUlyssesEbooks()
