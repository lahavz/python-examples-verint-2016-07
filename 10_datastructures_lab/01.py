"""
Receive hosnames and print IPs based on external hosts file
"""

import sys

hostnames = set(sys.argv[1:])

hostsfile = "C:\Users\lzeno\OneDrive\Code\Python Scripts\ToCode Course\Tasks\Data Structures\hosts.txt"

hosts={}

with open(hostsfile, "r") as s:
    for line in s:
        hosts.setdefault(line.split("=")[0] , line.split("=")[1])

for host in hostnames:
    print " %s %s " % (host, hosts.get(host))
