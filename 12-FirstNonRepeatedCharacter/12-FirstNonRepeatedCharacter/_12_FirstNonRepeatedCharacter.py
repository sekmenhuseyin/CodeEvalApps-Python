import sys
#get lines
f = open(sys.argv[1], 'r')
for line in f:
    line=line.replace("\n","")
    for x in range(0,len(line)):
        counter=0
        for y in range(0,len(line)):
            if line[x]==line[y]:
                counter+=1
        if counter==1:
            print(line[x])
            break
f.close()