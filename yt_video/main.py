import urllib.request
import json
from yt_video.settings import API_KEY  # 用絕對路徑import環境變數
CHANNEL_id = 'UCd4JzeAkgTsyJDEkWC11PoA'

print(API_KEY)

def get_all_video_in_channel(channel_id):
    base_video_url = 'https://www.youtube.com/watch?v='
    base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

    first_url = base_search_url + f'key={api_key}&channelId={channel_id}&part=snippet,id&order=date&maxResults=25'

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
    return video_links


# video_list = get_all_video_in_channel(CHANNEL_id)

# print(video_list)
# print(len(video_list))
