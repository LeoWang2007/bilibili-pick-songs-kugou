from public import *

import time,threading
import pygame
import sys

from msgFunc import *
import textFunc,musicFunc,webFunc

import uiAction,dbAction


def addLog(text):
    with open(LOG_NAME,'a+',encoding='utf-8') as f:
        f.write(time.strftime("%Y-%m-%d %H:%M:%S: ", time.localtime())+text+'\n')
    uiAction.ui.sw_logs.addItem(time.strftime("%Y-%m-%d %H:%M:%S: ", time.localtime())+text)

pygame.mixer.init()
def playUrl(info, url):
    songFileName = f'{info["data"]["audio_name"]}_{info["data"]["hash"]}_{info["data"]["album_id"]}.mp3'
    webFunc.downloadFile(url,f'./tempSongs/{songFileName}')
    pygame.mixer.music.load(f'./tempSongs/{songFileName}')
    pygame.mixer.music.play()
    return songFileName,info["data"]["audio_name"]

def controlMusic():
    while True:
        while not SONG_LIST:
            global freeMusicNO,isFreeMusic
            if not isFreeMusic and GLOBAL_RUN_MUSIC:
                info,url = musicFunc.getPlayUrl(defaultMuisc[freeMusicNO]['hash'], defaultMuisc[freeMusicNO]['album_id'])
                songFileName,songName = playUrl(info,url)
                uiAction.setMusicInfo(songName,'[空闲歌单]')
                addLog(f'[playFree] "{songFileName}"')
                print(f'[playFree] "{songFileName}"')

                #限制空闲音乐编号 循环播放，防止溢出
                if freeMusicNO < (freeMusicNumber - 1):
                    uiAction.setFreeMusicNO(freeMusicNO)
                    freeMusicNO += 1
                else:
                    uiAction.setFreeMusicNO(freeMusicNO)
                    freeMusicNO = 0

                isFreeMusic = True
            if not pygame.mixer.music.get_busy():
                isFreeMusic = False
            time.sleep(1)
        if GLOBAL_RUN_MUSIC:
            print(11111)
            isFreeMusic = False
            info,url = musicFunc.searchPlayUrl(SONG_LIST[0][2])
            songFileName,songName = playUrl(info,url)
            uiAction.setMusicInfo(songName,f'{SONG_LIST[0][0]}({SONG_LIST[0][1]})')
            addLog(f'[play]{SONG_LIST[0][0]}({SONG_LIST[0][1]}) picked "{songFileName}"')
            print(f'[play]{SONG_LIST[0][0]}({SONG_LIST[0][1]}) picked "{songFileName}"')
            SONG_LIST.pop(0)
            while pygame.mixer.music.get_busy():
                time.sleep(1)



def checkNewMsg():
    while True:
        msgList = getNewMsg()
        if msgList:
            for m in msgList:
                talkerId = m["talker_id"]
                uid = m["last_msg"]["sender_uid"]
                nickname = getUser(m["last_msg"]["sender_uid"])['name']
                detail = getDetail(talkerId)


                # 检查是否被Ban
                    # 检查用户录入情况，并获取西瓜云id
                wmcId = dbAction.markUser(uid,nickname)
                have_banned = dbAction.checkBanUser(wmcId)

                # cnt = 0 #符合要求的信息条数
                for i in range(m["unread_count"]):
                    latestMsg = detail['data']['messages'][i]
                    text = json.loads(latestMsg['content'])['content']
                    song = textFunc.checkMsgText(text)

                    #已封禁账户，仅记录日志
                    if have_banned:
                        addLog(f'[msg][banned]{nickname}({uid}): "{text}"')
                        continue

                    if song:
                        # cnt += 1
                        print('yes',song)
                        SONG_LIST.append([nickname, uid, song])
                    else:
                        print('no',text)
                    addLog(f'[msg]{nickname}({uid}): "{text}"')
                readMsg(talkerId)
        time.sleep(5)

def clicked_stop():
    global GLOBAL_RUN_MUSIC
    GLOBAL_RUN_MUSIC = not GLOBAL_RUN_MUSIC
    # print(GLOBAL_RUN_MUSIC)
    pygame.mixer.music.stop()
uiAction.ui.btn_stop.clicked.connect(clicked_stop)

def clicked_nextSong():
    pygame.mixer.music.stop()
uiAction.ui.btn_nextSong.clicked.connect(clicked_nextSong)

def clicked_freeMusicNO():
    global freeMusicNO
    freeMusicNO = uiAction.ui.sb_freeMusicNO.value()
    pygame.mixer.music.stop()
uiAction.ui.btn_setFreeMusicNO.clicked.connect(clicked_freeMusicNO)

t1 = threading.Thread(target=controlMusic)
t1.setDaemon(True)
t1.start()

t2 = threading.Thread(target=checkNewMsg)
t2.setDaemon(True)
t2.start()
uiAction.adminWindow.show()
sys.exit(uiAction.app.exec_())