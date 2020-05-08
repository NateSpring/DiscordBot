import tweepy

consumer_key = "WtuOsWAnbKmwFLulF0pUv5qRL"
consumer_secret = "erTnMJ5kI7MJscexxfHzvteDk2qUl1IAeCdUBky72BR9Kj2jlA"
access_token = "1137473005250965505-EwS8kZeWHn3qTjQ8hoQzoUyuue3hgo"
access_token_secret = "PSyUlZUfa1XGe1P5ax6DgbRgw3Lwd06lwzBsqnCSd254w"

# Creating the authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# Setting your access token and secret
auth.set_access_token(access_token, access_token_secret)
# Creating the API object while passing in auth information

api = tweepy.API(auth)

query = [""]
language = "en"

# Calling the user_timeline function with our parameters
results = api.search(q=query, lang=language)

# foreach through all tweets pulled
for tweet in results:
   # printing the text stored inside the tweet object
   print (tweet.user.screen_name, "Tweeted:", tweet.text)