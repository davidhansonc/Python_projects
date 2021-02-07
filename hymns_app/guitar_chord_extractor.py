# -*- coding: utf-8 -*-
# @Author: davidhansonc
# @Date:   2021-01-29 09:15:02
# @Last Modified by:   davidhansonc
# @Last Modified time: 2021-01-29 11:49:08
import pdfminer.high_level as pdf
import pdfreader
from pdfreader import PDFDocument, SimplePDFViewer
import re

fd = open('e0813_g.pdf', "rb")
# doc = PDFDocument(fd)
viewer = SimplePDFViewer(fd)


hymn_title = "I come before Thy throne of grace"
section_name = 'Study of the Word — Feeding on the Word'

text = pdf.extract_text('e0813_g.pdf')
# print(text)
text_list = text.split('\n')
# print(text_list)

# regex = re.compile('^[a-zA-Z]+$')
music_filter = re.compile('^[^a-zA-Z]*\(cid:\d\)[^a-zA-Z]*$')
verse_two = re.compile('^2\..*$')
condensed = []
other_stuff = []
filter2 = re.compile('[a-zA-Z]+\d*')
for item in text_list:
    if verse_two.match(item):
        break 
    if filter2.match(item) and item != hymn_title and item != section_name:
        condensed.append(item)
    if item == '-':
        print(item)

print(condensed)
# print(other_stuff)