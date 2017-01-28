import sys
#get lines
f = open(sys.argv[1], 'r')
for line in f:
    line=line.replace("\n","")
    words=line.split(" ")
    number=int(words[len(words)-1])
    if number<=len(words):
        print(words[len(words)-number-1])
f.close()