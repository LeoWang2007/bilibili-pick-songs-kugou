def ORmatch(s,l):
    for i in l:
        if i == s:
            return True
    return False

def findFirstNot(s,char):
    '''
    返回s中第一个不为char的字符位置
    :param s: 原字符串
    :param char: 无效字符
    :return: 第一个有效字符位置
    '''
    for i,c in enumerate(s):
        if c != char:
            return i
    return -1

def checkMsgText(content:str):
    content = content.lstrip()
    if ORmatch(content[:2].lower(),['点歌','dg','歌曲']):
        content = content[2:].rstrip()
        first = findFirstNot(content,' ')
        if first>=0:
            return content[first:]
    else:
        return ""

# print(checkMsgText('     歌曲 最美的期待'))