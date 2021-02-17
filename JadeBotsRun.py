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
JadeBots.postGenreDefining(postFreq, post, altPostFreq, altGenreExtraFreq, altGenreGameFreq, verbose)


#Mario Variants
postFreq = 1
extraPrefixPercent = 20
suffixPercent = 5
verbose = False
post = False

print("\n~Super Mario Variants~")
JadeBots.postMarioVariants(postFreq, post, extraPrefixPercent, suffixPercent, verbose)


# Romantics Ebooks
postFreq = 15
maxLength = 100
post = False

print("\n~Romantics eBooks~")
JadeBots.postRomanticsEbooks(postFreq, post, maxLength)


# Ulysses Ebooks
postFreq = 15
maxLength = 120
post = False

print("\n~Ulysses eBooks~")
JadeBots.postUlyssesEbooks(postFreq, post, maxLength)
