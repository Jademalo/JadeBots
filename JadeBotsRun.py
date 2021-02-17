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
post = False

print("~Genre Defining~")
JadeBots.postGenreDefining(postFreq, altPostFreq, altGenreExtraFreq, altGenreGameFreq, verbose, post)


#Mario Variants
postFreq = 1
extraPrefixPercent = 20
suffixPercent = 5
verbose = False
post = False

print("\n~Super Mario Variants~")
JadeBots.postMarioVariants(postFreq, extraPrefixPercent, suffixPercent, verbose, post)


# Romantics Ebooks
postFreq = 15
maxLength = 100
post = False

print("\n~Romantics eBooks~")
JadeBots.postRomanticsEbooks(postFreq, maxLength, post)


# Ulysses Ebooks
postFreq = 15
maxLength = 120
post = False

print("\n~Ulysses eBooks~")
JadeBots.postUlyssesEbooks(postFreq, maxLength, post)
