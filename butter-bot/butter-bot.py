import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
from discord.utils import get
import re 
import tweepy 
from tweepy import OAuthHandler 
from textblob import TextBlob
import asyncio
import praw
import random
import urllib.request
from bs4 import BeautifulSoup
import csv
import re
import markovify


TOKEN = 'NzA2ODUyNDQ4ODMyMzIzNjc0.XrARpA.YP7Whs19AKsbiRzvca_8-rzjOdE'
reddit = praw.Reddit(client_id='ReoMUk43GoPB9g',
                    client_secret='PCybyCu_4HffhqLyfOAUe1QKSbU',
                    user_agent='ninja_nate92')




description = '''My purpose is to pass the butter'''
bot = commands.Bot(command_prefix='!', description=description)

@bot.event
async def on_ready():
    print('Butter Robot Online')
    print(bot.user.id)
    print('------')

@bot.command()
async def purpose(message):
    """--What is my purpose?"""
    channel = message.author.voice.channel
    if not channel:
        await message.send("You are not connected to a voice channel")
        return
    voice = get(bot.voice_clients, guild=message.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    source = FFmpegPCMAudio('rick-passbutter.mp3')
    player = voice.play(source)

@bot.command()
async def meme(ctx):
    """--Display a top 10 reddit meme"""
    memes_submissions = reddit.subreddit('memes').hot()
    post_to_pick = random.randint(1, 100)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)

    await ctx.send(submission.url)

@bot.command()
async def wholesome(ctx):
    """--Display a top wholesome reddit meme"""
    memes_submissions = reddit.subreddit('wholesomememes').hot()
    post_to_pick = random.randint(1, 100)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)

    await ctx.send(submission.url)


@bot.command()
async def dank(ctx):
    """--Display a top dank reddit meme"""
    memes_submissions = reddit.subreddit('dankmemes').hot()
    post_to_pick = random.randint(1, 100)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)

    await ctx.send(submission.url)

    
@bot.command()
async def michelle(ctx):
    """--What would Michelle Say?"""
    sota = ['Oh my Gosh.', 'I\'ve got a beg of dregons.', 'Put it in the beg!', '**Strang hiccup noises**', 'I love soup.', 'Yeh, I had soup for lunch.', 'AHH!', 'Beg, behg, beag, beagh, ba-- beg.', 'I\'m from Minnesooooootah.']
    await ctx.send(random.choice(sota))



@bot.command()
async def news(ctx):
    """--What's happening in the news?"""
    URL = 'https://www.foxnews.com'
    page = urllib.request.urlopen(URL)
    soup = BeautifulSoup(page, 'html.parser')

    text_array = []

    headlines = soup.findAll('h2', attrs = {'class':'title'})

    for headline in headlines:
        quote = headline.a.text
        text_array.append(quote)
    text_model = markovify.Text(text_array)

    for i in range(1):
        await ctx.send("Fox News Report: {}".format(text_model.make_sentence()))






class TwitterClient(object): 
    ''' 
    Generic Twitter Class for sentiment analysis. 
    '''
    def __init__(self): 
        ''' 
        Class constructor or initialization method. 
        '''
        # keys and tokens from the Twitter Dev Console 
        consumer_key = "WtuOsWAnbKmwFLulF0pUv5qRL"
        consumer_secret = "erTnMJ5kI7MJscexxfHzvteDk2qUl1IAeCdUBky72BR9Kj2jlA"
        access_token = "1137473005250965505-EwS8kZeWHn3qTjQ8hoQzoUyuue3hgo"
        access_token_secret = "PSyUlZUfa1XGe1P5ax6DgbRgw3Lwd06lwzBsqnCSd254w"
  
        # attempt authentication 
        try: 
            # create OAuthHandler object 
            self.auth = OAuthHandler(consumer_key, consumer_secret) 
            # set access token and secret 
            self.auth.set_access_token(access_token, access_token_secret) 
            # create tweepy API object to fetch tweets 
            self.api = tweepy.API(self.auth) 
        except: 
            print("Error: Authentication Failed") 
  
    def clean_tweet(self, tweet): 
        ''' 
        Utility function to clean tweet text by removing links, special characters 
        using simple regex statements. 
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split()) 
  
    def get_tweet_sentiment(self, tweet): 
        ''' 
        Utility function to classify sentiment of passed tweet 
        using textblob's sentiment method 
        '''
        # create TextBlob object of passed tweet text 
        analysis = TextBlob(self.clean_tweet(tweet)) 
        # set sentiment 
        if analysis.sentiment.polarity > 0: 
            return 'positive'
        elif analysis.sentiment.polarity == 0: 
            return 'neutral'
        else: 
            return 'negative'
  
    def get_tweets(self, query, count = 10): 
        ''' 
        Main function to fetch tweets and parse them. 
        '''
        # empty list to store parsed tweets 
        tweets = [] 
  
        try: 
            # call twitter api to fetch tweets 
            fetched_tweets = self.api.search(q = query, count = count) 
  
            # parsing tweets one by one 
            for tweet in fetched_tweets: 
                # empty dictionary to store required params of a tweet 
                parsed_tweet = {} 
  
                # saving text of tweet 
                parsed_tweet['text'] = tweet.text 
                # saving sentiment of tweet 
                parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text) 
  
                # appending parsed tweet to tweets list 
                if tweet.retweet_count > 0: 
                    # if tweet has retweets, ensure that it is appended only once 
                    if parsed_tweet not in tweets: 
                        tweets.append(parsed_tweet) 
                else: 
                    tweets.append(parsed_tweet) 
  
            # return parsed tweets 
            return tweets 
  
        except tweepy.TweepError as e: 
            # print error (if any) 
            print("Error : " + str(e)) 
@bot.command()    
async def feels(ctx, arg):
        """--An analysis on your topic""" 
        # creating object of TwitterClient Class 
        api = TwitterClient() 
        queryArray = arg
        # calling function to get tweets 
        tweets = api.get_tweets(query = queryArray, count = 1500) 

        # pcking positive tweets from tweets 
        ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive'] 
        # percentage of positive tweets 
        print("Sentiment Analysis on: " + str(queryArray))
        print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets)))
        # picking negative tweets from tweets 
        ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative'] 
        # percentage of negative tweets 
        print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(tweets))) 
        # percentage of neutral tweets 
        print("Neutral tweets percentage: {} % ".format(100*(len(tweets) - len(ntweets) - len(ptweets))/len(tweets)))
        #sendtxt("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets))) 
          # printing first 5 positive tweets 
        # print("\n\nPositive tweets:") 
        for tweet in ptweets[:5]: 
          pos = (tweet['text']) 
    
        # printing first 5 negative tweets 
        #print("\n\nNegative tweets:") 
        for tweet in ntweets[:5]: 
          negs = (tweet['text']) 
        
        await ctx.send("Sentiment Analysis Topic: {} \n-----------------------------\n Positive Tweets Percentage: {} % \n Negative Tweets Percentage: {} % \n Neutral Tweets Percentage: {} % \n-----------------------------\n Random Positive Tweet: \n{} \n\n Random Negative Tweet: \n{}".format(str(queryArray), int(100*len(ptweets)/len(tweets)), int(100*len(ntweets)/len(tweets)), int(100*(len(tweets) - len(ntweets) - len(ptweets))/len(tweets)), pos, negs))
        
    

bot.run(TOKEN)
