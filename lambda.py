#-------------------------------------------------------------------------------
# Requirements
#-------------------------------------------------------------------------------
#tweepy
#mastodon.py
#python-dotenv
#str2bool

#-------------------------------------------------------------------------------
# Imports
#-------------------------------------------------------------------------------
import JadeBots
import os
import json
import urllib.request
import logging
import str2bool



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
def getParam(name, format=True):

    try:
        aws_session_token = os.environ.get('AWS_SESSION_TOKEN')
        req = urllib.request.Request('http://localhost:2773/systemsmanager/parameters/get?name='+name+'&withDecryption=true')
        req.add_header('X-Aws-Parameters-Secrets-Token', aws_session_token)
        param = json.loads(urllib.request.urlopen(req).read())
    except:
        return None

    # Returned as either a string, list, or dict depending on data type - String for regular params, list for csv params, dict for json params
    if format:
        if param["Parameter"]["Type"] == "String" or param["Parameter"]["Type"] == "SecureString":
            param = param["Parameter"]["Value"]
        
            if isJson(param):
                param = json.loads(param)
    
        elif param["Parameter"]["Type"] == "StringList":
            param = param["Parameter"]["Value"].split(",")

    return param
    

# Return a variable from either the event object or environment variables
def getVariable(event, name): 

    # Check the event object
    if event.get(name): #get() returns None as the default value if the key isn't found
        return event.get(name)

    # Check the Parameter Store
    if getParam(name): #getParam() returns None if the parameter doesn't exist
        return getParam(name)

    # Check the Environment Variables
    if os.getenv(name): #os.getenv() returns None as the default value if the environment variable isn't found
        return os.getenv(name)

    # Return None if there's no variable passed
    return None
    


#-------------------------------------------------------------------------------
# Main Handler
#-------------------------------------------------------------------------------

def lambdaHandler(event, context):

    # Enable debug logs if variable set
    if str2bool(getVariable(event, "DEBUG")):
        logging.basicConfig(level = logging.DEBUG)
    else:
        logging.basicConfig(level = logging.INFO)

    # Import account from Lambda event json
    account = getVariable(event, "ACCOUNT")
    if not account: 
        raise Exception("No account specified")

    # Import keys
    keys = getParam(account+"Keys")


    if account == "genreDefining":
        logging.info("~Genre Defining~")
        JadeBots.postGenreDefining(
            postTwitter = getVariable(event, "POST_TWITTER"), 
            twitterKeys = keys.get("Twitter"), 
            postMastodon = getVariable(event, "POST_MASTODON"), 
            mastodonKeys = keys.get("Mastodon"), 
            postFreq = getVariable(event, "POST_FREQ"), 
            altPostFreq = getVariable(event, "ALT_POST_FREQ"), 
            altGenreExtraFreq = getVariable(event, "ALT_GENRE_EXTRA_FREQ"), 
            altGenreGameFreq = getVariable(event, "ALT_GENRE_GAME_FREQ")
        )


    if account == "marioVariants":
        logging.info("~Super Mario Variants~")
        JadeBots.postMarioVariants(
            postTwitter = getVariable(event, "POST_TWITTER"), 
            twitterKeys = keys.get("Twitter"), 
            postMastodon = getVariable(event, "POST_MASTODON"), 
            mastodonKeys = keys.get("Mastodon"), 
            postFreq = getVariable(event, "POST_FREQ"),  
            extraPrefixPercent = getVariable(event, "EXTRA_PREFIX_PERCENT"), 
            suffixPercent = getVariable(event, "SUFFIX_PERCENT")
        )


    if account == "romanticsEbooks":
        logging.info("~Romantics eBooks~")
        JadeBots.postRomanticsEbooks(
            postTwitter = getVariable(event, "POST_TWITTER"), 
            twitterKeys = keys.get("Twitter"), 
            postMastodon = getVariable(event, "POST_MASTODON"), 
            mastodonKeys = keys.get("Mastodon"),  
            postFreq = getVariable(event, "POST_FREQ"),  
            minLength = getVariable(event, "MIN_LENGTH"), 
            maxLength = getVariable(event, "MAX_LENGTH")
        )


    if account == "ulyssesEbooks":
        logging.info("~Ulysses eBooks~")
        JadeBots.postUlyssesEbooks(
            postTwitter = getVariable(event, "POST_TWITTER"), 
            twitterKeys = keys.get("Twitter"), 
            postMastodon = getVariable(event, "POST_MASTODON"), 
            mastodonKeys = keys.get("Mastodon"), 
            postFreq = getVariable(event, "POST_FREQ"),  
            minLength = getVariable(event, "MIN_LENGTH"), 
            maxLength = getVariable(event, "MAX_LENGTH")
        )

