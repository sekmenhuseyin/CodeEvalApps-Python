import sys
#get lines
f = open(sys.argv[1], 'r')
for line in f:
    sonuc=0
    line=line.replace("\n","")
    line=bin(int(line))
    for x in range(0,len(line)):
        if line[x]=="1":
            sonuc+=1
    print(sonuc)
f.close()