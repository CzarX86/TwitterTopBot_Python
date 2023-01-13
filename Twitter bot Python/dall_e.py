import requests


# Define the text description of the image
description = "the solitary clone. season 2 of star wars bad batch is now streaming only on disney plus"

# Define the DALL-E API endpoint
url = "https://api.openai.com/v1/images/generations"

# Define the API key
headers = {"Content-Type": "application/json",
           "Authorization": "Bearer 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"}

# Define the data to be sent in the request body
data = '{"model": "image-alpha-001", "prompt": ' + '"'+description+'"'+'}'

# Send the request to the API
response = requests.post(url, headers=headers, data=data)

# Print the response
print(response.json())
