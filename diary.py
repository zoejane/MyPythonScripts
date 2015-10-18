import sys
diary=open('diary.txt','a')

if len(sys.argv) >1:
    content = ' '.join(sys.argv[1:])
    diary.write("\n" + content)
    
else:
    diary=open('diary.txt')
    content = diary.read()
    print(content)

diary.close()
