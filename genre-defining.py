#-------------------------------------------------------------------------------
# Imports
#-------------------------------------------------------------------------------
import tweetBot


#-------------------------------------------------------------------------------
# Variables
#-------------------------------------------------------------------------------
account = "genreDefining"
postFreq = 4

altPostFreq = 12
altGenreExtraFreq = 16
altGenreGameFreq = 24

gameFile = "genre-defining/game.txt"
genreFile = "genre-defining/genre.txt"
genreExtraFile = "genre-defining/genreExtra.txt"


#-------------------------------------------------------------------------------
# Main
#-------------------------------------------------------------------------------

# Generate the tweet
tweetText = tweetBot.main.genreTweet(gameFile, genreFile, genreExtraFile, altPostFreq, altGenreGameFreq, altGenreExtraFreq)

# Post the tweet to Twitter
tweetBot.main.postTweet(tweetText, account, postFreq)
