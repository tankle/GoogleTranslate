import re
import sys
import ctypes
try:
    import urllib2 as request
except:
    from urllib import request


def get_d1():
    req = request.Request(url='http://translate.google.com/', headers={'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5)\
                 Gecko/20091102 Firefox/3.5.5 (.NET CLR 3.5.30729)'})
    t = request.urlopen(req).read().decode('utf8')
    a, b, h = re.search(r"TKK=eval\(\'\(\(function\(\){var a\\x3d(\-?\d+);var b\\x3d(\-?\d+);return (\d+)", t).groups()
    return int(h), ctypes.c_int32(int(a) + int(b)).value
b, d1 = get_d1()


def RL(a, b):
    for c in range(0, len(b)-2, 3):
        d = b[c+2]
        d = ord(d) - 87 if d >= 'a' else int(d)
        xa = ctypes.c_uint32(a).value
        d = xa >> d if b[c+1] == '+' else xa << d
        a = a + d & 4294967295 if b[c] == '+' else a ^ d
    return ctypes.c_int32(a).value


def calc_tk(a):
    if sys.version_info >= (3,):
        d = a.encode('utf-8')
    else:
        d = map(ord, a)
    a = b
    for di in d:
        a = RL(a + di, "+-a^+6")
    a = RL(a, "+-3^+b+-f")
    a = ctypes.c_int32(a ^ d1).value
    a = a if a >= 0 else ((a & 2147483647) + 2147483648)
    a %= pow(10, 6)
    return '%d.%d' % (a, a ^ b)

if __name__ == '__main__':
    text = ' '.join(sys.argv[1:])
    print(calc_tk(text))
