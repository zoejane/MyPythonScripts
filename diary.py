#! /usr/bin/env python3

import sys
diary=open('diary.txt','a')

if len(sys.argv) >1:
    content = ' '.join(sys.argv[1:])
    if len(str(diary)==0):
        diary.write(content)
    else:
        diary.write("\n" + content)
    
else:
    content = diary.read()
    print(content)

diary.close()
