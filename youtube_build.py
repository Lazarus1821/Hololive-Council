from googleapiclient.discovery import build
import os

import requests
# The API Key here is hidden by saving to an environment variable.
API_KEY = os.environ.get('API_KEY')

# for building a request to the YouTube API using an API Key.
youtube = build('youtube', 'v3', developerKey=API_KEY)


# Request to be sent to the Youtube API. The Channel ID is obtained from the channel_url_id list defined earlier.
# the request is made as per the Youtube API documentation.
def request(channel_id):
    request_to_channel = youtube.channels().list(
        part='statistics',
        id=channel_id
    )
    response_to_request = request_to_channel.execute()
    return response_to_request["items"][0]["statistics"]
