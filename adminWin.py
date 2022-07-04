# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adminWin.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1073, 704)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(13)
        Form.setFont(font)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 1051, 71))
        font = QtGui.QFont()
        font.setFamily("Kingnam Maiyuan")
        font.setPointSize(27)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 27pt \"Kingnam Maiyuan\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 460, 1051, 231))
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.sw_logs = QtWidgets.QListWidget(self.groupBox)
        self.sw_logs.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.sw_logs.setObjectName("sw_logs")
        self.horizontalLayout_2.addWidget(self.sw_logs)
        self.formLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 90, 1051, 121))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.sw_nowMusic = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.sw_nowMusic.setFont(font)
        self.sw_nowMusic.setText("")
        self.sw_nowMusic.setReadOnly(True)
        self.sw_nowMusic.setObjectName("sw_nowMusic")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.sw_nowMusic)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.sw_pickUser = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.sw_pickUser.setFont(font)
        self.sw_pickUser.setText("")
        self.sw_pickUser.setReadOnly(True)
        self.sw_pickUser.setObjectName("sw_pickUser")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.sw_pickUser)
        self.list_users = QtWidgets.QListWidget(Form)
        self.list_users.setGeometry(QtCore.QRect(10, 220, 281, 161))
        self.list_users.setObjectName("list_users")
        self.btn_ban = QtWidgets.QPushButton(Form)
        self.btn_ban.setGeometry(QtCore.QRect(10, 390, 281, 46))
        self.btn_ban.setObjectName("btn_ban")
        self.btn_stop = QtWidgets.QPushButton(Form)
        self.btn_stop.setGeometry(QtCore.QRect(600, 330, 231, 41))
        self.btn_stop.setObjectName("btn_stop")
        self.list_songs = QtWidgets.QListWidget(Form)
        self.list_songs.setGeometry(QtCore.QRect(300, 220, 291, 161))
        self.list_songs.setObjectName("list_songs")
        self.btn_delSong = QtWidgets.QPushButton(Form)
        self.btn_delSong.setGeometry(QtCore.QRect(310, 390, 61, 51))
        self.btn_delSong.setObjectName("btn_delSong")
        self.btn_upSOng = QtWidgets.QPushButton(Form)
        self.btn_upSOng.setGeometry(QtCore.QRect(380, 390, 61, 51))
        self.btn_upSOng.setObjectName("btn_upSOng")
        self.btn_downSong = QtWidgets.QPushButton(Form)
        self.btn_downSong.setGeometry(QtCore.QRect(450, 390, 61, 51))
        self.btn_downSong.setObjectName("btn_downSong")
        self.btn_nextSong = QtWidgets.QPushButton(Form)
        self.btn_nextSong.setGeometry(QtCore.QRect(600, 380, 231, 41))
        self.btn_nextSong.setObjectName("btn_nextSong")
        self.le_search = QtWidgets.QLineEdit(Form)
        self.le_search.setGeometry(QtCore.QRect(850, 330, 211, 41))
        self.le_search.setText("")
        self.le_search.setObjectName("le_search")
        self.btn_run = QtWidgets.QPushButton(Form)
        self.btn_run.setGeometry(QtCore.QRect(850, 380, 211, 41))
        self.btn_run.setObjectName("btn_run")
        self.btn_play = QtWidgets.QPushButton(Form)
        self.btn_play.setGeometry(QtCore.QRect(520, 390, 61, 51))
        self.btn_play.setObjectName("btn_play")
        self.sb_freeMusicNO = QtWidgets.QSpinBox(Form)
        self.sb_freeMusicNO.setGeometry(QtCore.QRect(610, 270, 71, 41))
        self.sb_freeMusicNO.setObjectName("sb_freeMusicNO")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(610, 220, 271, 41))
        self.label_2.setObjectName("label_2")
        self.btn_setFreeMusicNO = QtWidgets.QPushButton(Form)
        self.btn_setFreeMusicNO.setGeometry(QtCore.QRect(720, 270, 112, 41))
        self.btn_setFreeMusicNO.setObjectName("btn_setFreeMusicNO")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "瓜云科技B站点歌软件[管理员端]"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:28pt; color:#00b0f0;\">WatermelonCloud </span><span style=\" font-size:28pt; color:#01a5f0;\">YourSymbol </span><span style=\" font-size:28pt; color:#a7a7a7;\">for </span><span style=\" font-size:28pt; color:#fb7299;\">Bilibili</span><span style=\" font-size:16pt;\">(Beta)</span></p></body></html>"))
        self.groupBox.setTitle(_translate("Form", "运行日志"))
        self.label_5.setText(_translate("Form", "当前歌曲"))
        self.label_6.setText(_translate("Form", "点歌用户"))
        self.btn_ban.setText(_translate("Form", "封禁/解封焦点用户"))
        self.btn_stop.setText(_translate("Form", "全局停止/继续"))
        self.btn_delSong.setText(_translate("Form", "🗑️"))
        self.btn_upSOng.setText(_translate("Form", "▲"))
        self.btn_downSong.setText(_translate("Form", "▼"))
        self.btn_nextSong.setText(_translate("Form", "播放下一首"))
        self.btn_run.setText(_translate("Form", "强制查找并播放"))
        self.btn_play.setText(_translate("Form", "🎵"))
        self.label_2.setText(_translate("Form", "当前播放空闲歌曲编号"))
        self.btn_setFreeMusicNO.setText(_translate("Form", "赋值"))
import font_rc
