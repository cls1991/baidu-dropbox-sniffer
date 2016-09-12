# coding: utf8

"""
example :
sign1: f5cc6220c998f4bf092f8a2439aacc62c99fd6ef
sign3: d76e889b6aafd3087ac3bd56f4d4053a

sign: 期望结果: JFUtQ3yPu6YE48swjJqiqHPRv27wf8GLaF55bJhisRUbCX4L/AnlNA==
      加密结果: JFUtQ3yPu6YE48swjJqiqHPRv27wf8GLaF55bJhisRUbCX4L/AnlNA==
"""
from util.sign_decode import parse_sign2, decode_sign


if __name__ == '__main__':
    sign1 = 'cd5959a7d56fa9076c080cc26f722a72010fc6e4'
    sign3 = 'd76e889b6aafd3087ac3bd56f4d4053a'
    print decode_sign(parse_sign2(sign3, sign1))
