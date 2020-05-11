import re
import os
import sys

# This re2 used for extract data and chinese chars.
re2 = re.compile(r'[\d{4}\u4e00-\u9fa5\u3002\uff1b\uff0c\uff1a\u201c\u201d\uff08\uff09\u3001\uff1f\u300a\u300b\d{1,2}\u4e00-\u9fa5\u3002\uff1b\uff0c\uff1a\u201c\u201d\uff08\uff09\u3001\uff1f\u300a\u300b{1}\d{1,2}\u4e00-\u9fa5\u3002\uff1b\uff0c\uff1a\u201c\u201d\uff08\uff09\u3001\uff1f\u300a\u300b{1}]+')
# This re3 used for extract urls in a page.
re3 = re.compile(
    r'http[s]?://(?:(?!http[s]?://)[a-zA-Z]|[0-9]|[$\-_@.&+/]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')

# Process file for information
ext = ['.html', '.shtml', '/']

a2c_dict = {"0": "零", "1": "一", "2": "贰", "3": "三", "4": "四",
            "5": "五", "6": "六", "7": "七", "8": "八", "9": "九"}


def arb2chinese(line):
    outLine = ""
    for ch in line:
        if ch in a2c_dict.keys():
            outLine += a2c_dict.get(ch)
        else:
            outLine += ch
    return outLine


punctuation = '！,，；：？“、”。《》%（）.〔〕'


def removePunctuation(text):
    text = re.sub(r'[{}]+'.format(punctuation), '', text)
    return text.strip().lower()


with open(r'C:\Users\cmcc\Desktop\dj_pa\out.txt', 'rt', encoding="utf-8") as f:
    lines = f.read()
    line = lines.strip()
    temStr = re2.findall(lines)
    for i in temStr:
        if len(i) > 20:
            no_sym = removePunctuation(i)
            target = arb2chinese(no_sym)
            print(target)
