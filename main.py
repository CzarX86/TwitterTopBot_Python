from twitter_api import TwitterAPI
from image_formatter import ImageFormatter
import json


def main():
    # Authenticate to the Twitter API using Tweepy
    with open('twitter_keys.json', 'r') as f:
        keys = json.load(f)

    consumer_key = keys['consumer_key']
    consumer_secret = keys['consumer_secret']
    access_token = keys['access_token']
    access_token_secret = keys['access_token_secret']


    # Create an instance of the TwitterAPI class
    twitter_api = TwitterAPI(
        consumer_key, consumer_secret, access_token, access_token_secret)
    # Get the top trending tweets
    tweets = twitter_api.get_trending_tweets()
    print(tweets)
    image_formatter = ImageFormatter(tweets, 'top_tweets.jpg')
    image_formatter.format_image('styles/styles.css')  # path of css files
    image_formatter.create_image()
    twitter_api.post_image('top_tweets.jpg')


if __name__ == "__main__":
    main()
