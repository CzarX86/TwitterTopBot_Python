# TwitterTopBot_Python by ChatGPT

## Introduction

This project is a Python script that utilizes the Tweepy library to interact with the Twitter API to retrieve popular tweets for a given search query, the PIL library for image processing, and json library for reading and parsing the API keys stored in a local json file.

These tweets are then formatted and rendered as an image using the PIL library. The script also allows for custom styling of the text through a CSS file.

## Documentation

The script authenticates to the Twitter API using the TwitterAPI class, which takes in four authentication keys (consumer key, consumer secret, access token, and access token secret) and uses them to authenticate with the API via the tweepy.OAuthHandler class. It then creates an instance of the tweepy.API class and assigns it to an instance variable self.api.

- The TwitterAPI class:

  - `__init__`(self, consumer_key: str, consumer_secret: str, access_token: str, access_token_secret: str):

    - This method is used to authenticate to the Twitter API using the provided authentication keys.
    - It creates an instance of the 'tweepy.OAuthHandler' class and sets the access token and secret.
    - It also creates an instance of the 'tweepy.API' class and assigns it to an instance variable 'self.api'.

  - 'get_trending_tweets(self) -> List[str]':
    - This method is used to get the top trending tweets by searching for tweets with the query 'star wars' and in english language,
    - it returns only the full_text of the top 3 tweets.
  - post_image(self, image_path: str):
    - This method is used to post the image to twitter by updating the status with the media file,
    - it should be noted that this method is now deprecated, and you should use the media_upload method along with the update_status method for uploading media.
  - main() function:
    - calls the get_trending_tweets() method from TwitterAPI class and assigns the returned tweets to a variable tweets
    - calls methods to format the tweets into an image using the ImageFormatter class, creates the image, and posts it to twitter using the post_image method.

- The ImageFormatter class:

  - `__init__`(self, tweets: List[str], image_path: str):
    - This method takes in a list of tweets and an image path, it creates a new image with a specified size and background color and creates a Draw object to draw on the image.
    - It also defines the font and font size of the text to be written.
  - create_image(self):
    - This method writes the tweets on the image and saves the image to the specified path.
  - format_image(self, css_path: str):
    - This method reads the css file and updates the font object with the new font-family, font-size, and font-color.
  - The script is using the wrap method from the textwrap library to divide the text into lines with a maximum of 40 characters.

Overall, the script uses the Twitter API to get the top trending tweets, formats them into an image, and posts the image to Twitter. However, there are some limitations and the implementation could be improved.

It should be noted that the script expects the existence of a "twitter_keys.json" file with the specified structure for the authentication keys.

### twitter_keys.json

<pre>
    <code>
         {
            "consumer_key": "qwertyuiopasdfghjklzxcvbnm",
            "consumer_secret": "abcdefghijklmnopqrstuvwxyz",
            "access_token": "1234567890qwertyuiopasdfghjk",
            "access_token_secret": "zxcvbnmasdfghjklqwertyuiop123"
         } 
      </code>
</pre>

It also expects the existence of a css file for formatting the image.

### styles.css

<pre>
    <code>
         /*
         font-family: TwitterChirp, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
         src: url('twitterchirp.ttf') format('truetype');
         */

         /* Set the font and font size */
         @font-face {
         font-family: PICOBLA, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto,
            Helvetica, Arial, sans-serif;
         src: url('PICOBLA_.ttf') format('truetype');
         font-size: 20px;
         }

         /* Set the color scheme to match Twitter */
         body {
         background-color: #1da1f2;
         color: #fff;
         }

         /* Set the font for the tweets */
         .tweet-text {
         font-family: PICOBLA, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto,
            Helvetica, Arial, sans-serif;
         font-size: 20px;
         line-height: 1.5;
         color: #fff;
         }

         /* Style the image */
         img {
         border: 2px solid #fff;
         }
      </code>
</pre>

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
4. Create a file called twitter_keys.json in the root directory and store your API keys and access tokens as described above.
5. Install the necessary libraries by running the following code in your terminal:
<pre>
   <code>
      pip install -r requirements.txt
   </code>
</pre>

6. Run the script with:
<pre>
   <code>
      python main.py
   </code>
</pre>

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
11. Add user interface. 🔥🔥🔥

## Transforming this project into a Python API and consuming it in a Firebase Node.js app:

1. Create a new Python web application using a web framework such as Flask or Django.
2. Move existing code from the main script into the web application, and organize it into appropriate modules or classes.
3. Create API endpoints in the web application to handle different API calls. For example, create an endpoint that returns top trending tweets and another endpoint that posts an image to Twitter.
4. Test the API using a tool like Postman to make sure it's working correctly.
5. Consume the API in the Firebase Node.js app using the http module or another package like request.
6. Update Firebase data with the data returned from the API.
7. Test the Firebase app to make sure it's consuming the data from the API correctly.
8. Deploy the Python API on a hosting service like Heroku or AWS and update the Firebase app to point to the deployed API.
