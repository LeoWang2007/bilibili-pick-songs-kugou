import json

with open('defaultMusicList.json', 'r', encoding='utf-8') as f:
    j = f.read()
    j = json.loads(j)['data']['info']
    # print(j)
    ml = [{'name': i['name'].replace("'","\'"),'hash': i['hash'],'album_id': i['album_id']} for i in j]
    print(len(ml))
    with open('defaultList.json','w',encoding='utf-8') as w:
        w.write(json.dumps(ml))