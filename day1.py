import sys

data = '''R1, L3, R5, R5, R5, L4, R5, R1, R2, L1, L1, R5, R1, L3, L5, L2, R4,
L1, R4, R5, L3, R5, L1, R3, L5, R1, L2, R1, L5, L1, R1, R4, R1, L1,
 L3, R3, R5, L3, R4, L4, R5, L5, L1, L2, R4, R3, R3, L185, R3, R4, L5, L4, R48,
 R1, R2, L1, R1, L4, L4, R77, R5, L2, R192, R2, R5, L4, L5, L3, R2, L4, R1, L5,
 R5, R4, R1, R2, L3, R4, R4, L2, L4, L3, R5, R4, L2, L1, L3, R1, R5, R5, R2, L5,
 L2, L3, L4, R2, R1, L4, L1, R1, R5, R3, R3, R4, L1, L4, R1, L2, R3, L3, L2, L1,
 L2, L2, L1, L2, R3, R1, L4, R1, L1, L4, R1, L2, L5, R3, L5, L2, L2, L3, R1, L4,
 R1, R1, R2, L1, L4, L4, R2, R2, R2, R2, R5, R1, L1, L4, L5, R2, R4, L3, L5, R2,
 R3, L4, L1, R2, R3, R5, L2, L3, R3, R1, R3'''
data = data.replace(" ", "").replace("\n","").split(sep=',')

inic = []
inic.append([0,0])

def addToData(dir,val):

    if(dir == 0):
        for i in range(val):
            inic.append(list(inic[-1]))
            inic[-1][1]+=1
    elif(dir == 1):
        for i in range(val):
            inic.append(list(inic[-1]))
            inic[-1][0]+=1
    elif(dir == 2):
        for i in range(val):
            inic.append(list(inic[-1]))
            inic[-1][1]-=1
    elif(dir == 3):
        for i in range(val):
            inic.append(list(inic[-1]))
            inic[-1][0]-=1
    else:
        print("Deu merda")
        sys.exit(1)
    #print(inic[-1])
    #print(inic[-2])
    #print(dir)


dir = 0
for info in data:
    if info.startswith("R"):
        dir=(dir+1)%4
    else:
        dir=(dir-1+4)%4
    val = int(info[1:])
    addToData(dir, val)

dist=abs(inic[-1][0])+abs(inic[-1][1])
for coord in range(len(inic)):
    if inic[coord] in inic[:coord]:
        print(inic[coord])
        print(abs(inic[coord][0])+abs(inic[coord][1]))
        break
print(inic)
print(dist)
