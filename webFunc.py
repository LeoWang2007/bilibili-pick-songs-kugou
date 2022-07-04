import requests

def downloadFile(uri,f=''):
    '''
    下载互联网文件
    :param uri: URL
    :param f: 文件存储位置 不填写直接返回文件
    :return: 是否成功? T:F
    '''
    r = requests.get(uri)
    if not f:
        return r.content
    try:
        with open(f, "wb") as code:
            code.write(r.content)
        return True
    except:
        return False