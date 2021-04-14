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

def gcpRun(data, context):

    #data is the payload from PubSub, context is something
    print(data)
    print(context)

    #Genre Defining
    print("~Genre Defining~")
    JadeBots.postGenreDefining()

    #Mario Variants
    print("\n~Super Mario Variants~")
    JadeBots.postMarioVariants()

    # Romantics Ebooks
    print("\n~Romantics eBooks~")
    JadeBots.postRomanticsEbooks()

    # Ulysses Ebooks
    print("\n~Ulysses eBooks~")
    JadeBots.postUlyssesEbooks()
