import tweepy
import json
import codecs

consumer_key = "WafKnu1qFkyTk97ywThW9bJHd"
consumer_secret = "e9oay20TLtXWRKtLwgedAvBMkNjfWjHk7IsjVzGRSyQZottc4y"
access_token = "907859869889384448-eC2oiD8JfHpGpIqpGws29G2bACAUeDB"
access_token_secret = "XQbbPiA5ld3IvKKtjcCO68sRg0he0bhGXCqWJCccpK70e"

# Creating the authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# Setting your access token and secret
auth.set_access_token(access_token, access_token_secret)
# Creating the API object while passing in auth information
api = tweepy.API(auth)		


# The Twitter user who we want to get tweets from
name = input("Enter the search : ")

# Number of tweets to pull
tweetCount = 100

# Calling the user_timeline function with our parameters
results = api.user_timeline(id=name, count=tweetCount)

# foreach through all tweets pulled
with codecs.open("indianexpress.txt", "w", encoding='utf8') as f:
	for tweet in results:
		# printing the text stored inside the tweet object
		f.write(str(tweet.text)+'\n')		

