#Program which gets three text files
#Merge the content of the first one and the second into the third file.

import sys
from itertools import izip_longest

(src1, src2, dst) = sys.argv[1:]

with open(dst, 'w') as res, open(src1) as f1, open(src2) as f2:
    for line1, line2 in izip_longest(f1, f2, fillvalue=""):
        res.write(line1.rstrip() + '\n')
        res.write(line2.rstrip() + '\n')

        
            
    
