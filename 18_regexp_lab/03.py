"""
Receive csv DB replace values 1 and 2
"""

import sys
import re


dbfile = "C:\Users\lzeno\OneDrive\Code\Python Scripts\ToCode Course\Tasks\Regex\input.csv"

with open(dbfile, "r") as s:
    for line in s:
        print re.sub(r'(\w+)\s*,\s*(\w+)', lambda m: m.group(2) + ',' + m.group(1), line),
