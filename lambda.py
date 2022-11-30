#-------------------------------------------------------------------------------
# Requirements
#-------------------------------------------------------------------------------
#tweepy
#mastodon.py
#python-dotenv

#-------------------------------------------------------------------------------
# Imports
#-------------------------------------------------------------------------------
import JadeBots
from JadeBots import str2bool
import os
import json
import urllib.request



#-------------------------------------------------------------------------------
# Functions
#-------------------------------------------------------------------------------

# Check if a string is valid JSON
def isJson(myjson):
  try:
    json.loads(myjson)
  except ValueError as e:
    return False
  return True


# Retrive a parameter from Parameter Store
def retriveParam(name):

    aws_session_token = os.environ.get('AWS_SESSION_TOKEN')
    req = urllib.request.Request('http://localhost:2773/systemsmanager/parameters/get?name='+name+'&withDecryption=true')
    req.add_header('X-Aws-Parameters-Secrets-Token', aws_session_token)
    param = json.loads(urllib.request.urlopen(req).read())

    return param #Returned as a dict
    

# Format a parameter from Parameter Store
def formatParam(param):

    if param["Parameter"]["Type"] == "String" or param["Parameter"]["Type"] == "SecureString":
        value = param["Parameter"]["Value"]
        
        if isJson(value):
            value = json.loads(value)
    
    if param["Parameter"]["Type"] == "StringList":
        value = param["Parameter"]["Value"].split(",")
        
    return value #Returned as either a string, list, or dict depending on data type


# Retrive and format a parameter from Parameter Store
def getParam(name):
    param = retriveParam(name)
    value = formatParam(param)

    return value


# Retrive Twitter and Mastodon keys
def retrieveKeys(account):

    name = account+"Keys"
    keys = getParam(name)

    twitterKeys = keys.get("Twitter")
    mastodonKeys = keys.get("Mastodon")

    return twitterKeys, mastodonKeys
    


#-------------------------------------------------------------------------------
# Main Handler
#-------------------------------------------------------------------------------

def lambdaHandler(event, context):
    # Import variables from Lambda event json
    account = event.get("ACCOUNT") #get() returns None as the default value if the key isn't found
    postTwitter = str2bool(event.get("POST_TWITTER")) 
    postMastodon = str2bool(event.get("POST_MASTODON"))
    postFreq = int(event.get("POST_FREQ"))

    twitterKeys, mastodonKeys = retrieveKeys(account)

    if account == "genreDefining":

        altPostFreq = int(event.get("ALT_POST_FREQ"))
        altGenreExtraFreq = int(event.get("ALT_GENRE_EXTRA_FREQ"))
        altGenreGameFreq = int(event.get("ALT_GENRE_GAME_FREQ"))
        verbose = str2bool(event.get("VERBOSE"))

        print("~Genre Defining~")
        JadeBots.postGenreDefining(postTwitter, twitterKeys, postMastodon, mastodonKeys, postFreq, altPostFreq, altGenreExtraFreq, altGenreGameFreq, verbose)


    if account == "marioVariants":

        extraPrefixPercent = int(event.get("EXTRA_PREFIX_PERCENT"))
        suffixPercent = int(event.get("SUFFIX_PERCENT"))
        verbose = str2bool(event.get("VERBOSE"))

        print("~Super Mario Variants~")
        JadeBots.postMarioVariants(postTwitter, twitterKeys, postMastodon, mastodonKeys, postFreq, extraPrefixPercent, suffixPercent, verbose)


    if account == "romanticsEbooks":

        minLength = int(event.get("MIN_LENGTH"))
        maxLength = int(event.get("MAX_LENGTH"))

        print("~Romantics eBooks~")
        JadeBots.postRomanticsEbooks(postTwitter, twitterKeys, postMastodon, mastodonKeys, postFreq, minLength, maxLength)


    if account == "ulyssesEbooks":

        minLength = int(event.get("MIN_LENGTH"))
        maxLength = int(event.get("MAX_LENGTH"))

        print("~Ulysses eBooks~")
        JadeBots.postUlyssesEbooks(postTwitter, twitterKeys, postMastodon, mastodonKeys, postFreq, minLength, maxLength)

