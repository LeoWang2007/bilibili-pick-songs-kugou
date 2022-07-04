import time

import musicFunc

LOG_NAME = ('logs/' + time.strftime("[XG_yourSymbol]%Y-%m-%d", time.localtime()) + '.log')

SONG_LIST = []
defaultMuisc = musicFunc.defaultMusic
isFreeMusic = False
freeMusicNO = 0
freeMusicNumber = len(defaultMuisc)
GLOBAL_RUN_MUSIC = True

uidList = []

#用户总人数位数（用于计算补0数量）
USER_NUMBER_DIGIT = 0