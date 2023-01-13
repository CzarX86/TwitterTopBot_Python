# TwitterTopBot_Python
 
## Introduction
This project is a Python script that utilizes the Tweepy library to access the Twitter API and retrieve popular tweets for a given search query. These tweets are then formatted and rendered as an image using the PIL library. The script also allows for custom styling of the text through a CSS file.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Requirements
* Python 3.x
* Tweepy library
* PIL (Python Imaging Library)
* Textwrap library

## Setup
1. Clone the repository to your local machine
2. Create a new application on your Twitter account at developer.twitter.com
3. Generate the necessary API keys and access tokens
4. Create a file called config.py in the root directory and store your API keys and access tokens as follows:
  ⋅⋅* consumer_key = 'YOUR_CONSUMER_KEY'
  ⋅⋅* consumer_secret = 'YOUR_CONSUMER_SECRET'
  ⋅⋅* access_token = 'YOUR_ACCESS_TOKEN'
  ⋅⋅* access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'
6. Install the necessary libraries by running pip install -r requirements.txt in your terminal
7. Run the script with python main.py

##Usage
The script has two main functions: get_trending_tweets() and post_image().
get_trending_tweets() retrieves popular tweets for a given search query and returns a list of tweets.
post_image() takes an image file path as a parameter and posts the image to Twitter.

##Contribution
If you want to contribute to this project, please feel free to fork the repository and make a pull request with your changes.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
If you have any questions or suggestions, please feel free to contact me on Twitter https://twitter.com/CzarX86.



