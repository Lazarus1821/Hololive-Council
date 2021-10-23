# from youtube_build import request -obsolete
#import video_thumbnail
#from write_to_json import write_to_json

from youtube_statistics import YTstats
from video_thumbnail import thumbnail_url

import os
# The API Key here is hidden by saving to an environment variable.
API_KEY = os.environ.get('API_KEY')

# Sana, Fauna, Kronii, Mumei, Baelz Channel URLs
channel_url_id = ["UCsUj0dszADCGbF3gNrQEuSQ", "UCO_aKKYxn4tvrqPjcTzZ6EQ",
                   "UCmbs8T6MWqUHP1tIQvSgKrg", "UC3n5uGu18FoCy23ggWWp8tA", "UCgmPnx-EEeOrZSg5Tiw7ZRQ"]


file_name_array = []
for channel in channel_url_id:
    yt = YTstats(API_KEY, channel)
    yt.get_channel_statistics()
    yt.get_channel_video_data()
    yt.dump_to_json()


for channel in channel_url_id:
    file_name = yt.video_data_to_json(channel)
    file_name_array.append(file_name)
print(file_name_array)

for file_name in file_name_array:
    print(thumbnail_url(file_name))

