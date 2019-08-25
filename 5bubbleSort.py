record=[66,57,44,24,1,5]
def sort(n):
    for j in range(len(n)-1,0,-1):
        for i in range(j):
            if n[i]>n[i+1]:

                n[i],n[i+1]=n[i+1],n[i]
    print(n[0])


sort(record)
