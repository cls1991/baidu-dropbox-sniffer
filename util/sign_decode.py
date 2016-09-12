# coding: utf8

"""
加密sign
分两步进行:
1. function u(sign3, sign1) => sign2
2. function base64decode(sign2) => sign
"""


def parse_sign2(sign1, sign3):
    """
    sign1 + sign3 => sign2
    :param sign1:
    :param sign3:
    :return:
    """
    a = list()
    p = list()
    o = ''
    v = len(sign1)
    for q in xrange(0, 256):
        a.append(ord(sign1[q % v:q % v + 1][0]))
        p.append(q)
    u = 0
    for q in xrange(0, 256):
        u = (u + p[q] + a[q]) % 256
        p[q], p[u] = p[u], p[q]
    i = u = 0
    for q in xrange(0, len(sign3)):
        i = (i + 1) % 256
        u = (u + p[i]) % 256
        p[i], p[u] = p[u], p[i]
        k = p[((p[i] + p[u]) % 256)]
        o += chr(ord(sign3[q]) ^ k)

    return o


def decode_sign(sign2):
    """
    sign2 => sign
    :param sign2:
    :return:
    """
    o = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    r = ''
    a = 0
    e = len(sign2)
    while e > a:
        n = 255 & ord(sign2[a])
        a += 1
        if a == e:
            r += o[n >> 2]
            r += o[(3 & n) << 4]
            r += '=='
            break
        i = ord(sign2[a])
        a += 1
        if a == e:
            r += o[n >> 2]
            r += o[(3 & n) << 4 | (240 & i) >> 4]
            r += o[(15 & i) << 2]
            r += '='
            break
        s = ord(sign2[a])
        a += 1
        r += o[n >> 2]
        r += o[(3 & n) << 4 | (240 & i) >> 4]
        r += o[(15 & i) << 2 | (192 & s) >> 6]
        r += o[63 & s]

    return r
