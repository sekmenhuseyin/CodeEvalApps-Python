import sys
#get lines
f = open(sys.argv[1], 'r')
for line in f:
    line=line.replace("\n","")
    words=line.split(",")
    words[1]=words[1].strip()
    sonuc=words[0]
    for x in range(0,len(words[1])):
        sonuc=sonuc.replace(words[1][x],"")
    print(sonuc)
f.close()