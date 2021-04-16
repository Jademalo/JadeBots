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


def awsRunGenre(event, context):

    #Genre Defining
    print("~Genre Defining~")
    JadeBots.postGenreDefining()


def awsRunMario(event, context):

    #Mario Variants
    print("\n~Super Mario Variants~")
    JadeBots.postMarioVariants()


def awsRunRomantics(event, context):

    # Romantics Ebooks
    print("\n~Romantics eBooks~")
    JadeBots.postRomanticsEbooks()


def awsRunUlysses(event, context):

    # Ulysses Ebooks
    print("\n~Ulysses eBooks~")
    JadeBots.postUlyssesEbooks()



def awsRunAll(event, context):

    #event is the payload from EventBridge, context is something
    print(event)
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
