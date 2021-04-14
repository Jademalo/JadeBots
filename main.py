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


def gcpRunGenre(data, context):

    #Genre Defining
    print("~Genre Defining~")
    JadeBots.postGenreDefining()


def gcpRunMario(data, context):

    #Mario Variants
    print("\n~Super Mario Variants~")
    JadeBots.postMarioVariants()


def gcpRunRomantics(data, context):

    # Romantics Ebooks
    print("\n~Romantics eBooks~")
    JadeBots.postRomanticsEbooks()


def gcpRunUlysses(data, context):

    # Ulysses Ebooks
    print("\n~Ulysses eBooks~")
    JadeBots.postUlyssesEbooks()



def gcpRunAll(data, context):

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
