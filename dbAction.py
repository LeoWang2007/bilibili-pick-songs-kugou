import sqlite3

import uiAction

conn = sqlite3.connect('wmc.db', check_same_thread=False)
cur = conn.cursor()

def getId(uid):
    sql = "select id from users where uid=?"
    cur.execute(sql, (uid,))
    datas = cur.fetchall()
    if datas:
        return datas[0][0]

def markUser(uid, name):
    if getId(uid):
        return getId(uid)
    else:
        sql = "INSERT INTO users(uid, name) VALUES(?, ?)"
        cur.execute(sql, (uid,name,))
        conn.commit()
        wmcId = getId(uid)
        # uiAction.addUserList(wmcId, name, uid)
        uiAction.showUserList()
        return wmcId

def getUiUserList():
    sql = "select id, name, uid from users"
    cur.execute(sql)
    datas = cur.fetchall()
    if datas:
        return datas

def BanUser(id):
    sql = "update users set banned=? where id=?"
    if checkBanUser(id):
        cur.execute(sql,(0,id))
    else:
        cur.execute(sql, (1, id))
    conn.commit()

def checkBanUser(id):
    sql = "select banned from users where id=?"
    cur.execute(sql, (id,))
    datas = cur.fetchall()
    return bool(datas[0][0])

# print(markUser(398866340,'西瓜科技'))
# print(markUser(39886634,'西瓜科'))