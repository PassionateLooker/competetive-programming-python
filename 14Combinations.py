import itertools
a=["a","b","c"]
line=itertools.permutations(a)
empty=[]
for i in line:
    empty.append(i)

print(empty,len(empty))

def printcombination(sArray):
    if len(sArray)==0:
        return []
    if len(sArray)==1:
        return [sArray]
    l=[]
    for i in range(len(sArray)):
        m=sArray[i]
        print(m,i)
        remlist=sArray[:i]+sArray[i+1:]
        print(remlist)
        for p in printcombination(remlist):
            print("==",[m],p)
            l.append([m]+p)
    return l

student=["a","b","sa"]

for i in printcombination(student):
    print(i)