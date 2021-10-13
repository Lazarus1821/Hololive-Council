from dict_to_list import get_all_values

from youtube_build import request

# Sana, Fauna, Kronii, Mumei, Baelz Channel URLs
channel_url_id = ["UCsUj0dszADCGbF3gNrQEuSQ", "UCO_aKKYxn4tvrqPjcTzZ6EQ",
              "UCmbs8T6MWqUHP1tIQvSgKrg", "UC3n5uGu18FoCy23ggWWp8tA", "UCgmPnx-EEeOrZSg5Tiw7ZRQ"]

# printing out the response output obtained for the request.
for channel in channel_url_id:
    response = request(channel)
    print(list(get_all_values(response)))



