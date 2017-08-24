#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = '777111325126356992-dKXQzw2VnawsYax6XdlaTn2U1AD1QUa'
access_token_secret = 'H6QYc71i1QwvL6Ix83PWk1gAf2fVMD3kV6GSk7gIEpmCc'
consumer_key = 'GPyE7BV7mNeWDeL4azCZ5tQ0c'
consumer_secret = 'KhUqAOEgMQ8w1nCLiuGOpqmr5fJxdezT2LN6zhipGkq5GeXAIf'


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print (data)
        return True

    def on_error(self, status):
        print (status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])
