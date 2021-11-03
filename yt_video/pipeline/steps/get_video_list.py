import urllib.request
import json
from yt_video.pipeline.steps.step import Step
from yt_video.settings import API_KEY  # 用絕對路徑import環境變數


class GetVideoList(Step):
    def process(self, data, inputs):
        channel_id = inputs['channel_id']  # 將未來可能在process傳入的參數儲存為字典
        base_video_url = 'https://www.youtube.com/watch?v='
        base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

        first_url = base_search_url + f'key={API_KEY}&channelId={channel_id}&part=snippet,id&order=date&maxResults=25'

        video_links = []
        url = first_url
        while True:
            inp = urllib.request.urlopen(url)
            resp = json.load(inp)
            # print(resp)
            for i in resp['items']:
                if i['id']['kind'] == "youtube#video":
                    video_links.append(base_video_url + i['id']['videoId'])

            try:
                next_page_token = resp['nextPageToken']
                url = first_url + f'&pageToken={next_page_token}'
            except KeyError:
                break
        print(video_links)
        print(len(video_links))
        return video_links
