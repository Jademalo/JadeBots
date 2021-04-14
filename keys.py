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
# Function for returning the env names for each account
#-------------------------------------------------------------------------------
def returnKeys(account):
    if account == acc1:
        consumer_key_env = "CONSUMER_TOKEN_GENRE"
        consumer_secret_env = "CONSUMER_SECRET_GENRE"
        access_token_env = "ACCESS_TOKEN_GENRE"
        access_token_secret_env = "ACCESS_SECRET_GENRE"

    elif account == acc2:
        consumer_key_env = "CONSUMER_TOKEN_ROMANTICS"
        consumer_secret_env = "CONSUMER_SECRET_ROMANTICS"
        access_token_env = "ACCESS_TOKEN_ROMANTICS"
        access_token_secret_env = "ACCESS_SECRET_ROMANTICS"

    elif account == acc3:
        consumer_key_env = "CONSUMER_TOKEN_ULYSSES"
        consumer_secret_env = "CONSUMER_SECRET_ULYSSES"
        access_token_env = "ACCESS_TOKEN_ULYSSES"
        access_token_secret_env = "ACCESS_SECRET_ULYSSES"

    elif account == acc4:
        consumer_key_env = "CONSUMER_TOKEN_MARIO"
        consumer_secret_env = "CONSUMER_SECRET_MARIO"
        access_token_env = "ACCESS_TOKEN_MARIO"
        access_token_secret_env = "ACCESS_SECRET_MARIO"

    else:
        consumer_key_env = ""
        consumer_secret_env = ""
        access_token_env = ""
        access_token_secret_env = ""

    consumer_key = os.environ.get(consumer_key_env),
    consumer_secret = os.environ.get(consumer_secret_env),
    access_token = os.environ.get(access_token_env),
    access_token_secret = os.environ.get(access_token_secret_env),

    print(type(consumer_key))

    return consumer_key, consumer_secret, access_token, access_token_secret;
