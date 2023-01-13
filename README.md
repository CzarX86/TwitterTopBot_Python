# TwitterTopBot_Python
 
Twitter Image Generator
This project is a Python script that utilizes the Tweepy library to access the Twitter API and retrieve popular tweets for a given search query. These tweets are then formatted and rendered as an image using the PIL library. The script also allows for custom styling of the text through a CSS file.

Requirements
Python 3.x
Tweepy library
PIL library
Setup
Clone the repository to your local machine
Create a new application on your Twitter account at developer.twitter.com
Generate the necessary API keys and access tokens
Create a file called config.py in the root directory and store your API keys and access tokens as follows:
Copy code
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'
Install the necessary libraries by running pip install -r requirements.txt in your terminal
Run the script with python main.py
Usage
The script has two main functions: get_trending_tweets() and post_image().
get_trending_tweets() retrieves popular tweets for a given search query and returns a list of tweets.
post_image() takes an image file path as a parameter and posts the image to Twitter.