#-------------------------------------------------------------------------------
# This file adds a function to return keys so that my keys aren't shared on GitHub

#-------------------------------------------------------------------------------
# Imports
#-------------------------------------------------------------------------------
import os


#-------------------------------------------------------------------------------
# Listing the names of the different accounts
#-------------------------------------------------------------------------------
acc1 = "genreDefining"
acc2 = "romanticsEbooks"
acc3 = "ulyssesEbooks"
acc4 = "marioVariants"


#-------------------------------------------------------------------------------
# Function for returning the keys
#-------------------------------------------------------------------------------
def returnKeys(account):
    if account == acc1:
        consumer_key = os.environ.get("CONSUMER_TOKEN_GENRE"),
        consumer_secret = os.environ.get("CONSUMER_SECRET_GENRE"),
        access_token = os.environ.get("ACCESS_TOKEN_GENRE"),
        access_token_secret = os.environ.get("ACCESS_SECRET_GENRE"),

    elif account == acc2:
        consumer_key = os.environ.get("CONSUMER_TOKEN_ROMANTICS"),
        consumer_secret = os.environ.get("CONSUMER_SECRET_ROMANTICS"),
        access_token = os.environ.get("ACCESS_TOKEN_ROMANTICS"),
        access_token_secret = os.environ.get("ACCESS_SECRET_ROMANTICS"),

    elif account == acc3:
        consumer_key = os.environ.get("CONSUMER_TOKEN_ULYSSES"),
        consumer_secret = os.environ.get("CONSUMER_SECRET_ULYSSES"),
        access_token = os.environ.get("ACCESS_TOKEN_ULYSSES"),
        access_token_secret = os.environ.get("ACCESS_SECRET_ULYSSES"),

    elif account == acc4:
        consumer_key = os.environ.get("CONSUMER_TOKEN_MARIO"),
        consumer_secret = os.environ.get("CONSUMER_SECRET_MARIO"),
        access_token = os.environ.get("ACCESS_TOKEN_MARIO"),
        access_token_secret = os.environ.get("ACCESS_SECRET_MARIO"),

    else:
        consumer_key = ""
        consumer_secret = ""
        access_token = ""
        access_token_secret = ""

    return consumer_key, consumer_secret, access_token, access_token_secret;
