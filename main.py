# coding: utf8

import os
# 切换工作目录到项目根目录
project = os.path.split(os.path.realpath(__file__))[0]
os.chdir(project)

from lib import pcs


if __name__ == '__main__':
    # 测试用例
    if __name__ == '__main__':
        dlinks = pcs.list_dir('/Death Note 1080P')
        pcs.save_to_file(dlinks, 'Death Note 1080P.txt')
