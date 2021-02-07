# -*- coding: utf-8 -*-
# @Author: davidhansonc
# @Date:   2021-01-29 09:15:02
# @Last Modified by:   davidhansonc
# @Last Modified time: 2021-01-29 11:49:08
import pdfminer.high_level as pdf
import re

hymn_title = "I come before Thy throne of grace"
section_name = 'Study of the Word — Feeding on the Word'

text = pdf.extract_text('e0813_g.pdf')
print(text)
text_list = text.split('\n')
# print(text_list)

# regex = re.compile('^[a-zA-Z]+$')
music_filter = re.compile('^[^a-zA-Z]*\(cid:\d\)[^a-zA-Z]*$')
verse_two = re.compile('^2\..*$')
condensed = []
for item in text_list:
    if verse_two.match(item):
        break 
    elif item.strip() != hymn_title and item.strip() != section_name \
            and not music_filter.match(item.strip()):
        item = item.strip()
        condensed.append(item.strip(r'(.*\(cid:\d\))'))

print(condensed)