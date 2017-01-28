import sys
#get lines
f = open(sys.argv[1], 'r')
for line in f:
    sonuc=""
    line=line.replace("\n","")
    words=line.split(" ")
    for word in words:
        sonuc=word +" "+ sonuc
    print(sonuc)
f.close()