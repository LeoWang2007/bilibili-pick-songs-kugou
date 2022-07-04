import requests, json
from config import *

with open('defaultList.json','r') as f:
    defaultMusic = json.loads(f.read())

def searchMusic(name):
    musicName = name
    url = f"http://msearchcdn.kugou.com/api/v3/search/song?showtype=14&highlight=em&pagesize=30&tag_aggr=1&tagtype=全部&plat=0&sver=5&keyword={musicName}&correct=1&api_ver=1&version=9108&page=1&area_code=1&tag=1&with_res_tag=1"

    r = requests.get(url)
    j = r.text.replace('<!--KG_TAG_RES_START-->', '').replace('<!--KG_TAG_RES_END-->', '')
    j = json.loads(j)
    j = j['data']['info']  # 仅保留歌曲信息
    return j


def musicInfo(hash, album_id):
    url = f"https://wwwapi.kugou.com/yy/index.php?r=play/getdata&hash={hash}&appid=1014&platid=4&album_id={album_id}"
    cookie = {
        'kg_mid': kg_mid,
        # 'KugooID': '1425017232',
        # 'kg_dfid': '4FIuLV4Z4yHq11CNUd3PWjY3',
        'KuGoo': KuGoo
    }
    r = requests.get(url, cookies=cookie)
    # print(r.text)
    j = json.loads(r.text)
    return j

def searchPlayUrl(keyText):
    m = searchMusic(keyText)  # 获取歌曲信息
    m = m[0]  # 取第一首歌曲
    # print(m)
    hash = m['hash']
    album_id = m['album_id']
    return musicInfo(hash, album_id), musicInfo(hash, album_id)['data']['play_url']

def getPlayUrl(hash, album_id):
    return musicInfo(hash, album_id), musicInfo(hash, album_id)['data']['play_url']

# print(getPlayUrl('dancemonkey'))