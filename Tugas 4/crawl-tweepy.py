import tweepy

auth = tweepy.OAuthHandler(txclJxqIJvu2mstTKCNB05Gfi, HOUhwMPgC36GHGlIrsRwAHzhJhproNDSEztQphmiqTbr3QUvkH)
auth.set_access_token(866251020-ssvtwYc5PIvdTdScA8J1jswjDDLGryKBVjvvoGbB, usIHEhmGvSdfkBwXLw9x4tEMB5B754Cvhpoet8dLZrVdO)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)