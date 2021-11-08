import urllib.request
import json
from yt_video.pipeline.steps.step import Step
from yt_video.settings import API_KEY  # 用絕對路徑import環境變數


class GetVideoList(Step):
    def process(self, data, inputs, utils):
        channel_id = inputs['channel_id']  # 將未來可能在process傳入的參數儲存為字典

        if utils.video_list_file_exist(channel_id):  # 先查詢該channel list 是否存在
            print(channel_id, '清單已存在')
            return self.read_file(utils.get_video_list_filepath(channel_id))

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
        self.write_to_file(video_links, utils.get_video_list_filepath(channel_id))
        return video_links

    def write_to_file(self, video_links, filepath):
        with open(filepath, 'w', encoding='utf-8') as f:
            for url in video_links:
                f.write(url + '\n')

    def read_file(self, filepath):
        with open(filepath, 'r') as f:
            video_links = []
            for url in f:
                video_links.append(url.strip())
        return video_links
