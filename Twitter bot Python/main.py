from twitter_api import TwitterAPI
from image_formatter import ImageFormatter


def main():
    # Authenticate to the Twitter API using Tweepy
    consumer_key = "lG4Lut1LmOFPthGBS8gfTLZyM"
    consumer_secret = "qgbd01Evb02oZ40ADkRETTYFmt4KsawPQht0QBmmyNw9WBh7Ni"
    access_token = "1443658109726216197-qYeWkQOTOslpj93K1NvTrwuuNHPjYE"
    access_token_secret = "TnaZJODLg7ILyQzsiXwsTH2e9jZ1aNqRKg87JY9tUPdNp"

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
