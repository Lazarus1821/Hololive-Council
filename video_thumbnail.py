import json


def thumbnail_url(file_name):
    with open(file_name) as json_file:
        data = json.load(json_file)

        video_data_arr = data["video_data"]
        url_list = []
        # for video in video_data_arr.values():
        #     url_list['thumbnail_url'] = video["thumbnails"]["maxres"]["url"]

        for video in video_data_arr.values():
            url_value = video["thumbnails"]["maxres"]["url"]
            url_list.append(url_value)
            #print(video["thumbnails"]["maxres"]["url"])
        #print(len(url_list))
        return url_list



