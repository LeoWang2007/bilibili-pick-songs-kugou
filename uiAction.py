from public import *

from PyQt5.QtWidgets import *
import PyQt5.QtCore as QtCore
from PyQt5.QtGui import *

import sys

import adminWin
import dbAction

app = QApplication(sys.argv)
adminWindow = QWidget()
ui = adminWin.Ui_Form()
ui.setupUi(adminWindow)

from PyQt5.QtGui import QFontDatabase, QFont
import font_rc  # 此处直接导入qrc转换后的py文件

# 注册特殊字体
fontDb = QFontDatabase()
fontID = fontDb.addApplicationFont(":/font/kingnam")  # 此处的路径为qrc文件中的字体路径

def setMusicInfo(name,picker):
    ui.sw_nowMusic.setText(name)
    ui.sw_pickUser.setText(picker)

def setFreeMusicNO(NO):
    ui.sb_freeMusicNO.setValue(NO)

ui.sb_freeMusicNO.setRange(0,freeMusicNumber-1)

def showUserList():
    global USER_NUMBER_DIGIT,uidList

    # 准备工作
    ui.list_users.clear()
    uidList = []

    swUlist = dbAction.getUiUserList()
    last = swUlist[-1][0]
    digit = len(str(last))
    USER_NUMBER_DIGIT = digit
    for u in swUlist:
        showInfo = f'{str(u[0]).zfill(digit)}|{u[1]}({u[2]})'
        if dbAction.checkBanUser(u[0]):
            showInfo = '[Ban]' + showInfo
        ui.list_users.addItem(showInfo)
        uidList.append([u[0],u[1],u[2]])
showUserList()

# # 废弃函数
# def addUserList(wmcId, name, uid):
#     #更新全局id位数
#     global USER_NUMBER_DIGIT
#     swUlist = dbAction.getUiUserList()
#     last = swUlist[-1][0]
#     digit = len(str(last))
#     USER_NUMBER_DIGIT = digit
#
#     showInfo = f'{str(wmcId).zfill(digit)}|{name}({uid})'
#     ui.list_users.addItem(showInfo)
#     uidList.append([wmcId, name, uid])

def clicked_ban():
    selectedIndex = ui.list_users.currentRow()
    selectedItem = ui.list_users.currentItem()
    userRow = uidList[selectedIndex]
    dbAction.BanUser(userRow[0])
    if dbAction.checkBanUser(userRow[0]):
        selectedItem.setText('[Ban]'+selectedItem.text())
    else:
        selectedItem.setText(f'{str(userRow[0]).zfill(USER_NUMBER_DIGIT)}|{userRow[1]}({userRow[2]})')
ui.btn_ban.clicked.connect(clicked_ban)