# -*- coding: UTF-8 -*-
#!/usr/bin/env python
import json
import random
import socket

try:
    import urllib2 as request
    from urllib import quote
except:
    from urllib import request
    from urllib.parse import quote
from tk import calc_tk

true_socket = socket.socket


def make_bound_socket(source_ip):
    def bound_socket(*a, **k):
        sock = true_socket(*a, **k)
        sock.bind((source_ip, 0))
        return sock
    return bound_socket

# socket.socket = make_bound_socket("223.252.193.21")

class Translator:
    tran_table = [(',,,,', ',null,null,null,'), (',,,', ',null,null,'),
                  (',,', ',null,'), ('[,', '[null,'), (',]', ',null]')]

    def __init__(self, to_lang, from_lang='auto'):
        self.from_lang = from_lang
        self.to_lang = to_lang

    def translate(self, source):
        s = self._get_json(source)
        for pattern, res in self.tran_table:
            s = s.replace(pattern, res)
        j = json.loads(s)
        return ''.join(sen[0] for sen in j[0])

    def _get_json(self, source):
        escaped_source = quote(source, '')
        req = request.Request(
                url=("http://translate.google.com/translate_a/single?"
                     "client=t&ie=UTF-8&oe=UTF-8&dt=t&sl=%s&tl=%s&q=%s&tk=%s"
                     ) % (self.from_lang, self.to_lang, escaped_source, calc_tk(source)),
                headers={'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5)\
                 Gecko/20091102 Firefox/3.5.5 (.NET CLR 3.5.30729)'})

        # 绑定ip
        # ip_add = all_ips[random.randint(0, len(all_ips)-1)]
        # socket.socket = make_bound_socket(ip_add)

        r = request.urlopen(req)

        return r.read().decode('utf-8')

if __name__ == "__main__":
    import argparse
    import sys
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('texts', metavar='text', nargs='+',
                        help='a string to translate'
                             '(use "" when it\'s a sentence)')
    parser.add_argument('-t', '--to', dest='to_lang', type=str, default='zh',
                        help='To language (e.g. zh, zh-TW, en, ja, ko).'
                             ' Default is zh.')
    parser.add_argument('-f', '--from', dest='from_lang',
                        type=str, default='auto',
                        help='From language (e.g. zh, zh-TW, en, ja, ko).'
                             ' Default is auto.')
    args = parser.parse_args()
    translator = Translator(from_lang=args.from_lang, to_lang=args.to_lang)
    for text in args.texts:
        translation = translator.translate(text)
        sys.stdout.write(translation)


