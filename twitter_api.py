import tweepy
from typing import List


class TwitterAPI:
    def __init__(self, consumer_key: str, consumer_secret: str, access_token: str, access_token_secret: str):
        self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(self.auth)

    def get_trending_tweets(self) -> List[str]:
        tweets = self.api.search_tweets(
            q='*', lang='en', result_type='popular', tweet_mode='extended')
        return [tweet.full_text for tweet in tweets[:3]]

    def post_image(self, image_path: str):
        try:
            media = self.api.update_status_with_media(
                status="test tweet", filename=image_path)
            # self.api.update_status(status='test  tweet', media_ids=[media.media_id])

            print("Image posted to Twitter successfully!")
        except tweepy.TweepyException as e:
            print(f"Error posting to Twitter: {str(e)}")
