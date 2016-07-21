"""
Defining toCamelCase and fromCamelCase functions
"""

import re

def toCamelCase(text):
    CamelCase = text
    if re.search(r'(\w+)_(\w+)', text):
        CamelCase = re.sub(r'_[a-zA-Z]', lambda m: m.group(0).upper(), text)
        CamelCase = re.sub(r'_', '', CamelCase)
    print CamelCase

def fromCamelCase(text):
    text = re.sub(r'[a-z][A-Z]', lambda m: m.group(0)[0].lower() + '_' + m.group(0)[1].lower(), text)

    print text
    

toCamelCase('lahav')
toCamelCase('lahav_zeno')
toCamelCase('lahav_Zeno')
toCamelCase('_lahav_Zeno')
toCamelCase('lahav_4eno')
toCamelCase('no_more_shall_we_part')

print '________________________'
fromCamelCase('lahavZeno')
fromCamelCase('lahav_Zeno')
fromCamelCase('noMoreShallWePart')
