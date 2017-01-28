import sys
#get lines
f = open(sys.argv[1], 'r')
for line in f:
    sonuc=""
    line=line.replace("\n","")
    if line.find("30")>-1 or line.find("52")>-1:
        sonuc="30"
    elif line.find("8")>-1 or line.find("3")>-1:
        sonuc="8"
    else:
        sonuc="20"
    print(sonuc)
f.close()