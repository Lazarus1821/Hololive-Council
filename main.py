from youtube_build import request
from write_to_json import write_to_json

import os
# The API Key here is hidden by saving to an environment variable.
API_KEY = os.environ.get('API_KEY')

# Sana, Fauna, Kronii, Mumei, Baelz Channel URLs
channel_url_id = ["UCsUj0dszADCGbF3gNrQEuSQ", "UCO_aKKYxn4tvrqPjcTzZ6EQ",
                   "UCmbs8T6MWqUHP1tIQvSgKrg", "UC3n5uGu18FoCy23ggWWp8tA", "UCgmPnx-EEeOrZSg5Tiw7ZRQ"]

# printing out the response output obtained for the request.
Sana_channel_details = request('UCsUj0dszADCGbF3gNrQEuSQ')
write_to_json('Sana', Sana_channel_details)

Fauna_channel_details = request("UCO_aKKYxn4tvrqPjcTzZ6EQ")
write_to_json('Fauna', Fauna_channel_details)


Kronii_channel_details = request("UCmbs8T6MWqUHP1tIQvSgKrg")
write_to_json('Kronii', Kronii_channel_details)

Mumei_channel_details = request("UC3n5uGu18FoCy23ggWWp8tA")
write_to_json('Mumei', Mumei_channel_details)

Bae_channel_details = request("UCgmPnx-EEeOrZSg5Tiw7ZRQ")
write_to_json('Bae', Bae_channel_details)

