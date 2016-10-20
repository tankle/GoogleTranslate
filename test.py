# -*- coding: utf-8 -*-
#
# @author hztancong
#
from translate import Translator

translator = Translator(from_lang="auto", to_lang="zh")
text = "現在こちらの商品情報は種類別に登録されております。ご投稿に際してはお手元の商品をご確認いただき、それぞれの商品にご投稿ください。 ご協力お願いいたします。(＠ｃｏｓｍｅ編集部)"
translation = translator.translate(text)
print(translation)

text = "Hello world"
translation = translator.translate(text)
print(translation)