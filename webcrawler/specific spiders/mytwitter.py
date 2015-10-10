import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import sys

TWITTER_APP_KEY = 'jdlA1VpJnFDdxvfbBYW0yCHaQ' 
TWITTER_APP_KEY_SECRET = 'NDfP4m6eig8Xr2L7TuS3FbQ5uTIj2BwGIqddORfjMxrJf1hOyg' 
TWITTER_ACCESS_TOKEN = '113962350-sQyC6zAwQbMZ61TDfB3ZxOfB1MGsEgXq348M5fwC'
TWITTER_ACCESS_TOKEN_SECRET = '7TJj7YYTWIoW7sx0WWi6FKEQbiIlhXi1dCKijprcQr5Bt'


class TweetListener(StreamListener):
   

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status

auth = OAuthHandler(TWITTER_APP_KEY,TWITTER_APP_KEY_SECRET)
api = tweepy.API(auth)

auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
twitterStream = Stream(auth,TweetListener())

# user = api.get_user('robbierogers')
#user1 = api.get_user('landondonovan')


#names=['robbierogers', 'landondonovan']
# users=api.search_users('robbie rogers')
myusers = []
otherusers=[]
# others = [[0 for x in range(2)] for x in range(2)]
trueusers = []
actresses = []
# myplayer='abc'
t=0
i=0
f = open('myfinal.txt','r')
for line in f:
  str2=line.replace('\n','')
  actresses.append(str2)

f.close()
print actresses
for actress in actresses:
  try:
     # c=0
     users = api.search_users(actress)
     for u in users:
      if u.verified == True and u.name == actress:
         # myusers=myusers+[u.screen_name]
         # print u.screen_name
         myusers.append(u.screen_name)
         break
         
      else:
         # others.append(u.screen_name)
         otherusers.append(u.screen_name)
      
         # print u.name + "   ===   https://twitter.com/" + u.screen_name
  except:
     # print("exception happened!")
   
     continue
print myusers
print 'hahah'
print "   "
# print others
# print "   "
print otherusers

 for player in myusers:
  # user = api.get_user('robbierogers')
  user = api.get_user(player)
  print " "
  print "Basic information for",user.name
  print "Screen Name:",user.screen_name
  print "Name: ",user.name
  print "Twitter Unique ID: ",user.id
  print "Account created at: ",user.created_at
  print "Player DEscription: ",user.description
  print "Number of followers: ",user.followers_count
  print "Number of tweets:",user.statuses_count
  print "Players webite URL: ",user.url
  print "  "
  timeline = api.user_timeline(screen_name=user.screen_name, include_rts=True, count=1)
  for tweet in timeline:
         print "Tweet ID:", tweet.id
         print "Text:", tweet.text
         print "Created:", tweet.created_at
         print "Retweeted:", tweet.retweeted
         print "Retweet count:", tweet.retweet_count
         print "Source:", tweet.source   
         print " "


for player in otherusers:
 # user = api.get_user('robbierogers')
  user = api.get_user(player)
  if(user.followers_count>1000):
    trueusers.append(player)
print trueusers

 for myplayer in trueusers:
  usr=api.get_user(myplayer)
  print " "
  print "Basic information for",user.name
  print "Screen Name:",user.screen_name
  print "Name: ",user.name
  print "Twitter Unique ID: ",user.id
  print "Account created at: ",user.created_at
  print "Player DEscription: ",user.description
  print "Number of followers: ",user.followers_count
  print "Number of tweets:",user.statuses_count
  print "Players webite URL: ",user.url
  print "  "
  timeline = api.user_timeline(screen_name=user.screen_name, include_rts=True, count=1)
  for tweet in timeline:
         print "Tweet ID:", tweet.id
         print "Text:", tweet.text
         print "Created:", tweet.created_at
         print "Retweeted:", tweet.retweeted
         print "Retweet count:", tweet.retweet_count
         print "Source:", tweet.source   
         print " "