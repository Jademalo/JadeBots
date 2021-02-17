#-------------------------------------------------------------------------------
# Imports
#-------------------------------------------------------------------------------
import JadeBots


#-------------------------------------------------------------------------------
# Main Functions
#-------------------------------------------------------------------------------

#Genre Defining
postFreq = 24
altPostFreq = 12
altGenreExtraFreq = 16
altGenreGameFreq = 24
verbose = False

print("~Genre Defining~")
JadeBots.postGenreDefining(postFreq, altPostFreq, altGenreExtraFreq, altGenreGameFreq, verbose)


#Mario Variants
postFreq = 1
verbose = True

print("\n~Super Mario Variants~")
JadeBots.postMarioVariants(postFreq, verbose)


# Romantics Ebooks
postFreq = 15
maxLength = 100

print("\n~Romantics eBooks~")
JadeBots.postRomanticsEbooks(postFreq, maxLength)


# Ulysses Ebooks
postFreq = 15
maxLength = 120

print("\n~Ulysses eBooks~")
JadeBots.postUlyssesEbooks(postFreq, maxLength)
