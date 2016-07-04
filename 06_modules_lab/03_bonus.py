import sys
import os
import argparse

parser = argparse.ArgumentParser(description='Delete files higher than')
parser.add_argument("Path", help="directory path")
parser.add_argument("File_size", help="delete files bigger than size (in Bytes)")

args = parser.parse_args()



for root, dirs, files in os.walk(sys.argv[1]):
#for root, dirs, files in os.walk("C:\Users\lzeno\OneDrive\Code\Python Scripts\ToCode Course\Tasks\Models"):
    for name in files:
        if os.path.getsize(os.path.join(root,name)) >= int(sys.argv[2]):
            print os.path.join(root,name) + " is bigger than " + sys.argv[2] + "Bytes Delete? (Y/N)"
            answer = raw_input()
            while True:
                if answer == 'Y' or answer == 'y':
                    os.remove(os.path.join(root,name))
                    print os.path.join(root,name) + " Deleted"
                    break
                else:
                    if answer == 'N' or answer == 'n':
                        break
                    else:
                        print "Try Again"
                        answer = raw_input()
                        
                

