"""
Looks for anagrams and print the couples
"""
from collections import Counter

src = "C:\Users\lzeno\OneDrive\Code\Python Scripts\ToCode Course\Tasks\Data Structures\Anagram.txt"

lines = open(src,"r").readlines()
counters =[]

for i in range(len(lines)):
    lines[i] = lines[i].replace('\n','')

for i in range(len(lines)):
    line = Counter(lines[i])
    for j in range(i+1,len(lines)):
        if (line == Counter(lines[j])) and not line in counters:
            print "%s : %s" % (lines[i], lines[j])
            counters.append(Counter(lines[i]))

