#-------------------------------------------------------------------------------
# Imports
#-------------------------------------------------------------------------------
import tweetBot


#-------------------------------------------------------------------------------
# Variables
#-------------------------------------------------------------------------------
account = "romanticsEbooks"
postFreq = 15

mainFile = "romantics-ebooks/RomanticsText.txt"


#-------------------------------------------------------------------------------
# Main
#-------------------------------------------------------------------------------

# Generate the tweet
tweetText = tweetBot.ebooksTweet(mainFile)
print(tweetText)

# Post the tweet to Twitter
tweetBot.postTweet(tweetText, account, postFreq)
