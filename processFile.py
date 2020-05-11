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
for line in open(r'C:\Users\cmcc\Desktop\dj_pa\out.txt', 'rt', encoding="utf-8").readlines():
    line = line.strip()
    if line == []:
        continue
    line = re2.findall(line)
    if len(line) > 1:
        print(line)
    # Used for check  search urls
    # tempURL = re2.findall(line)
    # if tempURL == []:
    #     continue
    # for i in range(len(tempURL)):
    #     if "12371" in str(tempURL[i]).split("."):
    #         if tempURL[i].endswith(tuple(ext)):
    #             print(tempURL[i])
