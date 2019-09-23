#-------------------------------------------------------------------------------
# Imports
#-------------------------------------------------------------------------------
import JadeBots


#-------------------------------------------------------------------------------
# Main Functions
#-------------------------------------------------------------------------------

#Genre Defining
postFreq = 0
altPostFreq = 12
altGenreExtraFreq = 16
altGenreGameFreq = 24
verbose = False

print("~Genre Defining~")
postGenreDefining(postFreq, altPostFreq, altGenreExtraFreq, altGenreGameFreq, verbose)


# Romantics Ebooks
postFreq = 0
maxLength = 100
print(maxLength)

print("\n~Romantics eBooks~")
postRomanticsEbooks(postFreq, maxLength)


# Ulysses Ebooks
postFreq = 0
maxLength = 120
print(maxLength)

print("\n~Ulysses eBooks~")
postUlyssesEbooks(postFreq, maxLength)
