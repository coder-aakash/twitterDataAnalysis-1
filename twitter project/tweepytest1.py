from tweepy import Stream
from tweepy import OAuthHandler
from tweepy import StreamListener
import time
#from twitter api , consumer key, consumer secret, access token, access secret. 

ckey='GPyE7BV7mNeWDeL4azCZ5tQ0c'
csecret='KhUqAOEgMQ8w1nCLiuGOpqmr5fJxdezT2LN6zhipGkq5GeXAIf'
atoken='777111325126356992-dKXQzw2VnawsYax6XdlaTn2U1AD1QUa'
asecret='H6QYc71i1QwvL6Ix83PWk1gAf2fVMD3kV6GSk7gIEpmCc'

#directly picked from streaming.py module

class listener(StreamListener):
     def on_data(self,data):
         try:
             #print(data)
             #saving information to a text file...
             '''
             This data is really in form of an untrimmed data with twitter giving
             huge amount of surplus and unintended info with each tweet we parse
             '''
             dataFile=open('twitterDbase.csv','a+')
             dataFile.write(data)
             dataFile.write('\n')
             tweet=data.split(',"text":')[1].split(',"source":')[0]
             strng=str(time.time())+":::"+tweet
             print(strng)
             tweetFile=open('twitterDbasev2.0.csv','a+')
             tweetFile.write(strng)
             tweetFile.write('\n')
             dataFile.close()
             tweetFile.close()
             return True
         except BaseException as e:
             print("failed ondata.",str(e))
             time.sleep(5)

     def on_error(self, status):
         if status_code == 420:
             print("NEED TO DISCONNECT\n")
             stream.disconnect()
             # that should wait until next tweet, so let's delete it
             del stream
         print (status)


'''Next thing we need to do is authorise overselves using OAuthHandler
which does a lot of stuff in the background not relevant to new coders per se
'''
auth= OAuthHandler(ckey,csecret)
auth.set_access_token(atoken, asecret)



twitStream = Stream(auth,listener())
twitStream.filter(track=["India"])


