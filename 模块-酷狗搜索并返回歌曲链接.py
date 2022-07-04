# ----------配置区----------
# 请配置Cookies，填写的Cookies名称与变量名对应
# 使用VIP账号Cookies可听VIP歌曲，游客登录也要填，不填会报错

# 酷狗账户凭证
kg_mid = "60e02aa56568e240b6c891cb32659253"
# 酷狗登录信息聚合
KuGoo = "KugooID=1425017232&KugooPwd=F0FE98324B8877D02558A97DBF94821C&NickName=%u0046%u0061%u0073%u0068%u0069%u006f%u006e%u0062%u0075%u0079%u0065%u0072%u4e22%u4e22&Pic=http://imge.kugou.com/kugouicon/165/20190303/20190303184238753621.jpg&RegState=1&RegFrom=&t=1cc4891b1d0a8fffb751f53fd8fbf066c60db5f2708d5f492025d7dc0b0ed3f6&t_ts=1648558639&t_key=&a_id=1014&ct=1648558639&UserName=%u006b%u0067%u006f%u0070%u0065%u006e%u0031%u0034%u0032%u0035%u0030%u0031%u0037%u0032%u0033%u0032"
# ----------配置区----------

import requests, json


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

if __name__ == '__main__':
    m = searchMusic('dance monkey')  # 获取歌曲信息
    m = m[0]  # 取第一首歌曲
    # print(m)
    hash = m['hash']
    album_id = m['album_id']
    print(musicInfo(hash, album_id)['data']['play_url'])