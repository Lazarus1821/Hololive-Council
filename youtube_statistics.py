import requests
import json

from tqdm import tqdm


class YTstats:
    def __init__(self, api_key, channel_id):
        self.api_key = api_key
        self.channel_id = channel_id
        self.channel_statistics = None
        self.video_data = None

    def get_channel_statistics(self):
        url = f'https://www.googleapis.com/youtube/v3/channels?part=statistics&id={self.channel_id}&key={self.api_key}'
        json_url = requests.get(url)
        data = json.loads(json_url.text)

        try:
            data = data['items'][0]['statistics']
        except:
            data = None
        self.channel_statistics = data
        return data

    def dump_to_json(self):
        if self.channel_statistics is None or self.video_data is None:
            print("Null Data")
            return

        fused_data = {self.channel_id: {"channel_statistics": self.channel_statistics, "video_data": self.video_data}}

        channel_title = self.video_data.popitem()[1].get('channelTitle', self.channel_id)
        channel_title = channel_title.replace(" ", "_").lower()
        file_name = channel_title + ".json"
        with open(file_name, 'w') as filename:
            json.dump(fused_data, filename, indent=4)

    def video_data_to_json(self,file_name_string):
        if self.video_data is None:
            print("Null Data")
            return

        data = {'video_data': self.video_data}
        file_name = 'video_thumbnail' + file_name_string + ".json"
        with open(file_name, 'w') as filename:
            json.dump(data, filename, indent=4)
        return file_name

    def get_channel_video_data(self):
        channel_videos = self._getchannel_videos(limit=50)
        print(channel_videos, len(channel_videos))

        parts = ["snippet", "statistics", "contentDetails"]
        for video_id in tqdm(channel_videos):
            for part in parts:
                data = self._get_single_video_data(video_id, part)
                channel_videos[video_id].update(data)

        self.video_data = channel_videos
        return channel_videos

    def _get_single_video_data(self,video_id,part):
        url = f"https://www.googleapis.com/youtube/v3/videos?part={part}&id={video_id}&key={self.api_key}"
        json_url = requests.get(url)
        data = json.loads(json_url.text)
        try:
            data = data['items'][0][part]
        except:
            print("Errror")
            data = dict()

        return data

    def _getchannel_videos(self,limit = None):
        url = f"https://www.googleapis.com/youtube/v3/search?key={self.api_key}&channelId={self.channel_id}&part=id&order=date"
        if limit is not None and isinstance(limit, int):
            url += "&maxResults=" + str(limit)

        vid,npt = self._getchannel_videos_per_page(url)
        idx = 0
        while npt is not None and idx<10:
            idx +=1
            nexturl = url + "&pageToken=" + npt
            next_vid,npt = self._getchannel_videos_per_page(nexturl)
            vid.update(next_vid)

        return vid

    def _getchannel_videos_per_page(self,url):
        json_url = requests.get(url)
        data = json.loads(json_url.text)
        channel_videos = dict()
        if 'items' not in data:
            return channel_videos, None

        item_data = data['items']
        nextpageToken = data.get('nextPageToken', None)
        for item in item_data:
            try:
                kind = item['id']['kind']
                if kind == 'youtube#video':
                    video_id = item['id']['videoId']
                    channel_videos[video_id] = dict()
            except KeyError:
                print('No videos found to provide a statistic for')
        return channel_videos, nextpageToken


