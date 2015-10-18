#! /usr/bin/env python3

import sys


if len(sys.argv) >1:
    diary=open('diary.txt','a')
    diary.write("\n" + content)
    
else:

    content = diary.read()
    print(content)

diary.close()
