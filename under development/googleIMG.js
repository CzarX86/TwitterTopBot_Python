const query = 'star wars';
let imageUrl = null;

// Make a request to Google Images
fetch(`https://www.google.com/search?q=${query}&tbm=isch`)
  .then((response) => response.text())
  .then((data) => {
    // Parse the HTML
    const parser = new DOMParser();
    const htmlDoc = parser.parseFromString(data, 'text/html');

    // Find the first image on the page
    const imageTag = htmlDoc.querySelector('img');

    if (imageTag) {
      imageUrl = imageTag.src;
    }
    if (imageUrl) {
      // Authenticate with Twitter
      var Twit = require('twit');

      var T = new Twit({
        consumer_key: 'YOUR_CONSUMER_KEY',
        consumer_secret: 'YOUR_CONSUMER_SECRET',
        access_token: 'YOUR_ACCESS_TOKEN',
        access_token_secret: 'YOUR_ACCESS_TOKEN_SECRET',
        timeout_ms: 60 * 1000, // optional HTTP request timeout to apply to all requests.
      });
      // post the tweet with the image
      T.post(
        'media/upload',
        { media_data: imageUrl },
        function (err, data, response) {
          var mediaIdStr = data.media_id_string;
          var params = { status: 'YOUR_TWEET_TEXT', media_ids: [mediaIdStr] };

          T.post('statuses/update', params, function (err, data, response) {
            console.log(data);
          });
        }
      );
    } else {
      console.log('No image found for the given query.');
    }
  });
