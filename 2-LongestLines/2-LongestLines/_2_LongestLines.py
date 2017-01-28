import sys

lines=[]
counter=0
lineNo=0
tmp=""
#get lines
f = open(sys.argv[1], 'r')
for line in f:
    if counter==0:
        counter=int(line)
    else:
        lines.append(line.replace('\n', ''))
        lineNo+=1
f.close()
#order lines
for x in range(0,lineNo):
    for y in range(x,lineNo):
        if len(lines[x])<len(lines[y]):
            tmp=lines[y]
            lines[y]=lines[x]
            lines[x]=tmp
#show only to counter
for x in range(0,counter):
    print(lines[x])
