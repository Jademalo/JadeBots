#-------------------------------------------------------------------------------
# Imports
#-------------------------------------------------------------------------------
import tweetBot


#-------------------------------------------------------------------------------
# Variables
#-------------------------------------------------------------------------------
account = "ulyssesEbooks"
postFreq = 15

mainFile = "ulysses-ebooks/Ulysses.txt"


#-------------------------------------------------------------------------------
# Main
#-------------------------------------------------------------------------------

# Generate the tweet
tweetText = tweetBot.ebooksTweet(mainFile)
print(tweetText)

# Post the tweet to Twitter
tweetBot.postTweet(tweetText, account, postFreq)
