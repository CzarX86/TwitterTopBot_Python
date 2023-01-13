import twitter_api
import pytest


class Test_Twitterapi_Get_trending_tweets:

    @pytest.fixture()
    def twitterapi(self):
        return twitter_api.TwitterAPI()

    def test_get_trending_tweets_1(self, twitterapi):
        twitterapi.get_trending_tweets()
