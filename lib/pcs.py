# coding: utf8

"""
网盘相关操作:
1. 列举目录文件
2. 生成下载链接
"""

import os
import pycurl
import json
import urllib
from StringIO import StringIO

from share import const
from util.sign_decode import parse_sign2, decode_sign


def list_dir(dir_name):
    """
    列举网盘目录内容
    :param dir_name: 目录
    :return:
    """
    result = list()
    curl = pycurl.Curl()
    curl.setopt(pycurl.USERAGENT, const.USER_AGENT)
    curl.setopt(pycurl.REFERER, const.PAN_REFER_URL)

    buffers = StringIO()
    request_dict = {
        'channel': 'chunlei',
        'clienttype': 0,
        'showempty': 0,
        'web': 1,
        'order': 'time',
        'desc': 1,
        'page': 1,
        'num': 100,
        'dir': dir_name,
        'bdstoken': 'e0e895bb3ef7b0cb70899ee66b74e809'
    }
    target_url = const.PAN_API_URL + 'list?' + urllib.urlencode(request_dict)
    curl.setopt(pycurl.URL, target_url)
    curl.setopt(pycurl.WRITEDATA, buffers)
    curl.setopt(pycurl.COOKIEFILE, "cookie.txt")
    curl.perform()
    body = buffers.getvalue()
    print body
    buffers.close()
    curl.close()
    data = json.loads(body)
    if data['errno'] == 0:
        for a_list in data['list']:
            dlink = get_download_link(a_list['fs_id'])
            if dlink:
                result.append(dlink)

    return result


def get_download_link(fs_id):
    """
    获取下载链接
    :param fs_id:
    :return:
    """
    curl = pycurl.Curl()
    curl.setopt(pycurl.USERAGENT, const.USER_AGENT)
    curl.setopt(pycurl.REFERER, const.PAN_REFER_URL)

    """
    download_ajax_url = 'https://pan.baidu.com/api/download?sign=cVV6FS6PvqcE75Y43cyh%2FHTbuD2sLcrbOld7O8lgs0IdAHEJqluyZw%3D%3D&
    timestamp=1473685224&fidlist=%5B117518735349252%5D&type=dlink&channel=chunlei&web=1&app_id=250528&
    bdstoken=e0e895bb3ef7b0cb70899ee66b74e809&logid=MTQ3MzY4NTIyODI1MjAuMTI0ODQ1MTgyMzAxMTU1MTY=&clienttype=0'
    """
    buffers = StringIO()
    request_dict = {
        'channel': 'chunlei',
        'timestamp': '1473685224',
        'fidlist': [fs_id],
        'type': 'dlink',
        'web': 1,
        'clienttype': 0,
        'bdstoken': 'e0e895bb3ef7b0cb70899ee66b74e809',
        'sign': decode_sign(parse_sign2('d76e889b6aafd3087ac3bd56f4d4053a', '3545d271c5d07ba27355d39da0c62a4ee06d2d25'))
    }
    target_url = const.PAN_API_URL + 'download?' + urllib.urlencode(request_dict)
    curl.setopt(pycurl.URL, target_url)
    curl.setopt(pycurl.WRITEDATA, buffers)
    curl.setopt(pycurl.COOKIEFILE, "cookie.txt")
    curl.perform()
    body = buffers.getvalue()
    buffers.close()
    curl.close()
    data = eval(body)
    if data['errno']:
        return None

    return data['dlink'][0]['dlink']


def save_to_file(d_links, file_name):
    """
    将图片链接存入文件
    :param d_links: 图片真实下载链接
    :param :file_name: 文件名
    :return
    """
    try:
        if not d_links:
            return
        base_dir = 'out/'
        if not os.path.exists(base_dir):
            os.mkdir(base_dir)
        file_object = open(base_dir + file_name, 'a')

        for item in d_links:
            file_object.write(item)
            file_object.write('\n')
        file_object.close()
    except IOError:
        print('file not exist!')
        exit()


if __name__ == '__main__':
    dlinks = list_dir('/Death Note 1080P')
    save_to_file(dlinks, 'Death Note 1080P.txt')
