import random, twitter

poemFile = open("RomanticsText.txt", "r")

poemString = poemFile.read()
#print poemString

tweetLength = int(random.randint(30,100))
print "Length =",
print tweetLength

#tweetPost = int(random.randint(1,15))
#print "Will Post (If = 15) =",
#print tweetPost


tweetStart = int(random.random()*(len(poemString)-140))
workingTweet = poemString[tweetStart:tweetStart+tweetLength].split(" ")

#print workingTweet
#print 'Test'

#if poemString.find(" "+ workingTweet[0]) < 0:
#    del workingTweet[0]

#print workingTweet

#if poemString.find(workingTweet[-1] + " ") < 0 or poemString.find(workingTweet[-1]) != len(poemString):
#    del workingTweet[-1]

#print workingTweet

workingTweet = workingTweet[1:]
#print workingTweet

workingTweet = workingTweet[:-1]
#print workingTweet

finalTweet = " ".join(workingTweet)
#print finalTweet

api = twitter.Api(consumer_key='',
                  consumer_secret='',
                  access_token_key='',
                  access_token_secret='')

#if tweetPost == 15:
status = api.PostUpdate(finalTweet)
print status.text
