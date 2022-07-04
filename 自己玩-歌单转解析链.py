# ----------配置区----------
# 请配置Cookies，填写的Cookies名称与变量名对应
# 使用VIP账号Cookies可听VIP歌曲，游客登录也要填，不填会报错

# 酷狗账户凭证
kg_mid = "b9f5afdfa461f4d1979f337162305a8f"
# 酷狗登录信息聚合
KuGoo = "KugooID=1425017232&KugooPwd=F0FE98324B8877D02558A97DBF94821C&NickName=%u0046%u0061%u0073%u0068%u0069%u006f%u006e%u0062%u0075%u0079%u0065%u0072%u4e22%u4e22&Pic=http://imge.kugou.com/kugouicon/165/20190303/20190303184238753621.jpg&RegState=1&RegFrom=&t=1cc4891b1d0a8fffb751f53fd8fbf0660f13072f7730252863060a4517c056de&t_ts=1656222400&t_key=&a_id=1014&ct=1656222400&UserName=%u006b%u0067%u006f%u0070%u0065%u006e%u0031%u0034%u0032%u0035%u0030%u0031%u0037%u0032%u0033%u0032"
# ----------配置区----------

import requests, json, time


def musicUrl(hash, album_id):
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
    return j['data']['play_url']

print('| 歌曲名 | 链接 |')
print('| ---- | ---- |')

with open('defaultList.json','r',encoding='utf-8') as f:
    jl = f.read()
    jl = json.loads(jl)
    for i in jl:
        name = i['name']
        url = musicUrl(i['hash'],i['album_id'])
        time.sleep(0.02)
        print(f'| {name} | [西瓜音乐免费听]({url}) |')