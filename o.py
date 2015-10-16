#! /usr/bin/env python3

import webbrowser,sys

url = 'http://docs.python.org/'

# MacOS
chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

# Windows
# chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'

# Linux
# chrome_path = '/usr/bin/google-chrome %s'


if len(sys.argv) ==2:
    #['open-web.py',      'udemy'] -> 'udemy'
    address = sys.argv[1]
    if address == 'udemy':
        url = 'https://www.udemy.com/automate/learn/'
    elif address == 'gb':
        url= 'https://zoejane.gitbooks.io/zoe-py-tutorial/content/'
    elif address == 'gh':
        url ='https://github.com/zoejane'
    elif address =='edit':
        url ='https://www.gitbook.com/book/zoejane/zoe-py-tutorial/edit'
    elif address  == 'en':
        url ='https://app.yinxiang.com/Home.action'


webbrowser.get(chrome_path).open(url)

