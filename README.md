# TwitterTopBot_Python by ChatGPT

## Introduction

This project is a Python script that utilizes the Tweepy library to interact with the Twitter API to retrieve popular tweets for a given search query, the PIL library for image processing, and json library for reading and parsing the API keys stored in a local json file.

These tweets are then formatted and rendered as an image using the PIL library. The script also allows for custom styling of the text through a CSS file.

## Documentation

The script authenticates to the Twitter API using the TwitterAPI class, which takes in four authentication keys (consumer key, consumer secret, access token, and access token secret) and uses them to authenticate with the API via the tweepy.OAuthHandler class. It then creates an instance of the tweepy.API class and assigns it to an instance variable self.api.

The TwitterAPI class has two methods get_trending_tweets() which is used to get the top trending tweets and post_image(self, image_path: str) which is used to post the image to twitter by updating the status with the media file.

The main() function calls the get_trending_tweets() method and assigns the returned tweets to a variable tweets. It then formats the tweets into an image using the ImageFormatter class, creates the image, and posts it to twitter using the post_image method.

The ImageFormatter class takes in a list of tweets and an image path and creates an image with the tweets written on it. It creates a new image with a specified size and background color and creates a Draw object to draw on the image. It defines the font and font size of the text to be written.
The class has two methods create_image() which is used to create the image with the tweets and format_image(self, css_path: str) which is used to read the css file and get the font-family, font-size, and font-color.

The create_image() method writes the tweets on the image and saves the image to the specified path.
The format_image(self, css_path: str) method reads the css file and updates the font object with the new font-family and font-size, and color.
The script is using the wrap method from textwrap library to divide the text into lines with a maximum of 40 characters.

It should be noted that the script expects the existence of a "twitter_keys.json" file with the following structure:
{
"consumer_key": "YOUR_CONSUMER_KEY",
"consumer_secret": "YOUR_CONSUMER_SECRET",
"access_token": "YOUR_ACCESS_TOKEN",
"access_token_secret": "YOUR_ACCESS_TOKEN_SECRET"
}

It also expects the existence of a css file for formatting the image.

Overall, the script uses the Twitter API to get the top trending tweets, formats them into an image, and posts the image to Twitter.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Requirements

- Python 3.x
- Libraries: - Tweepy - PIL (Python Imaging Library) - Textwrap

## Setup

1. Clone the repository to your local machine
2. Create a new application on your Twitter account at https://developer.twitter.com
3. Generate the necessary API keys and access tokens
4. Create a file called twitter_keys.json in the root directory and store your API keys and access tokens as follows:

<pre>
    <code>
      {
         "consumer_key": "lG4Lut1LmOFPthGBS8gfTLZyM",
         "consumer_secret": "qgbd01Evb02oZ40ADkRETTYFmt4KsawPQht0QBmmyNw9WBh7Ni",
         "access_token": "1443658109726216197-qYeWkQOTOslpj93K1NvTrwuuNHPjYE",
         "access_token_secret": "TnaZJODLg7ILyQzsiXwsTH2e9jZ1aNqRKg87JY9tUPdNp"
      } 
      </code>
</pre>

5. Install the necessary libraries by running pip install -r requirements.txt in your terminal
6. Run the script with python main.py

## Usage

The script has two main functions: get_trending_tweets() and post_image().
get_trending_tweets() retrieves popular tweets for a given search query and returns a list of tweets.
post_image() takes an image file path as a parameter and posts the image to Twitter.

## Contribution

If you want to contribute to this project, please feel free to fork the repository and make a pull request with your changes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

If you have any questions or suggestions, please feel free to contact me on Twitter https://twitter.com/CzarX86.

# Roadmap

1. Research AI image generation APIs (such as DALL-E, DeepDream, etc.) and determine which one(s) would be the most suitable for creating background images for the project.
2. Implement the chosen AI image generation API(s) and integrate them into the existing codebase.
3. Test and debug the AI background image generation functionality.
4. Allow users to customize and choose their own background images for the generated tweets images.
5. Continue to gather user feedback and make improvements to the AI background image generation functionality.
6. Explore the possibility of using other AI techniques such as style transfer to create unique and personalized background images.
7. Develop a user interface or a command-line interface (CLI) to make it easier for users to select the background image they want.
8. Add options for users to upload their own images to use as background images.
9. Add ability for the user to change the background color of the image if they don't want to use a background image.
10. Create a documentation for the AI background image generation functionality and update the Readme file.
