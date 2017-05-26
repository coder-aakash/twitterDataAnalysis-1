import tweepy

consumer_key = 'GPyE7BV7mNeWDeL4azCZ5tQ0c'
consumer_secret = 'KhUqAOEgMQ8w1nCLiuGOpqmr5fJxdezT2LN6zhipGkq5GeXAIf'
access_token = '777111325126356992-dKXQzw2VnawsYax6XdlaTn2U1AD1QUa'
access_token_secret = 'H6QYc71i1QwvL6Ix83PWk1gAf2fVMD3kV6GSk7gIEpmCc'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


def print_tweet(tweet):
    print('@{} - {}'.format(tweet.user.screen_name, tweet.user.name))
    print(tweet.text)
    print('')

result = api.search(q = 'MIvsRPS')
#for tweet in result:
#  print_tweet(tweet)


