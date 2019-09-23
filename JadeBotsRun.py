#-------------------------------------------------------------------------------
# Imports
#-------------------------------------------------------------------------------
import JadeBots


#-------------------------------------------------------------------------------
# Main Functions
#-------------------------------------------------------------------------------

print("~Genre Defining~")
    postFreq = 0
    altPostFreq = 12
    altGenreExtraFreq = 16
    altGenreGameFreq = 24
    verbose = False
postGenreDefining(postFreq, altPostFreq, altGenreExtraFreq, altGenreGameFreq, verbose)

print("\n~Romantics eBooks~")
    postFreq = 0
    maxLength = 100
    print(maxLength)
postRomanticsEbooks(postFreq, maxLength)

print("\n~Ulysses eBooks~")
    postFreq = 0
    maxLength = 120
    print(maxLength)
postUlyssesEbooks(postFreq, maxLength)
