import config

import requests
import json
import time

import textFunc

def getUser(uid):
    rdata = {
        "uids": uid
    }
    res = requests.get('https://api.vc.bilibili.com/account/v1/user/cards', params=rdata)
    return json.loads(res.text)['data'][0]

def getChatList()->dict:
    rdata = {
        "sender_device_id": 1,
        "talker_id": 119304214,
        "session_type": 1,
        "size": 20,
        "build": 0,
        "mobi_app": "web"
    }
    rcookies = {
        "SESSDATA": config.SESSDATA
    }
    res = requests.get('https://api.vc.bilibili.com/session_svr/v1/session_svr/get_sessions', params=rdata, cookies=rcookies)
    return json.loads(res.text)

def getNewMsg():
    chatList = getChatList()["data"]["session_list"]
    newChat = [i for i in chatList if i["unread_count"] > 0]
    return newChat

def getDetail(talker_id):
    rdata = {
        "sender_device_id": 1,
        "talker_id": talker_id,
        "session_type": 1,
        "size": 20,
        "build": 0,
        "mobi_app": "web"
    }
    rcookies = {
        "SESSDATA": config.SESSDATA
    }
    res = requests.get('https://api.vc.bilibili.com/svr_sync/v1/svr_sync/fetch_session_msgs', params=rdata, cookies=rcookies)
    return json.loads(res.text)

def readMsg(talker_id, ack_seqno=0):
    rcookies = {
        "SESSDATA": config.SESSDATA
    }
    rdata = {
        "talker_id": talker_id,
        "session_type": 1,
        # "ack_seqno": ack_seqno,
        "build": 0,
        "mobi_app": "web"
    }
    res = requests.get(f'https://api.vc.bilibili.com/session_svr/v1/session_svr/update_ack', cookies=rcookies, params=rdata)

# print(getNewMsg())
# print(getChatList())
# print(getDetail(1551676824))
# readMsg(337521240,4956773007371)
# print(getUser(398866340))
# checkNewDM()