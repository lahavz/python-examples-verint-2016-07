"""
Receive key DB and key and if invalid return its value
"""

import sys
import re


keyfile = "C:\Users\lzeno\OneDrive\Code\Python Scripts\ToCode Course\Tasks\Regex\db01.txt"
key = 'number'


with open(keyfile, "r") as s:
    for line in s:
        m = re.search(r'(\w+)\s*=\s*(\w+)',line)
        if m is not None:
            if m.group(1) == key:
                print m.group(2)

