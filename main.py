#-------------------------------------------------------------------------------
# Requirements
#-------------------------------------------------------------------------------
#tweepy

#-------------------------------------------------------------------------------
# Imports
#-------------------------------------------------------------------------------
import JadeBots


#-------------------------------------------------------------------------------
# Main Functions
#-------------------------------------------------------------------------------

def postAll():

    #Genre Defining
    postFreq = 24
    post = False
    altPostFreq = 12
    altGenreExtraFreq = 16
    altGenreGameFreq = 24
    verbose = False

    print("~Genre Defining~")
    JadeBots.postGenreDefining(postFreq, post, altPostFreq, altGenreExtraFreq, altGenreGameFreq, verbose)


    #Mario Variants
    postFreq = 24
    post = False
    extraPrefixPercent = 25
    suffixPercent = 5
    verbose = False

    print("\n~Super Mario Variants~")
    JadeBots.postMarioVariants(postFreq, post, extraPrefixPercent, suffixPercent, verbose)


    # Romantics Ebooks
    postFreq = 15
    post = False
    maxLength = 100

    print("\n~Romantics eBooks~")
    JadeBots.postRomanticsEbooks(postFreq, post, maxLength)


    # Ulysses Ebooks
    postFreq = 1
    post = True
    maxLength = 120

    print("\n~Ulysses eBooks~")
    JadeBots.postUlyssesEbooks(postFreq, post, maxLength)
