#Program which gets two text files and append the first one to the second.

import sys

(src, dst) = sys.argv[1:]

with open(src, "r") as fin:
    with open(dst, "a") as fout:
        fout.write('\n')
        for line in fin:
            fout.write(line)
            

            
    
