# kammla=8
# fina=6
# tony=7
#
# adding=kammla+fina+tony
#
# print("Avg is "+str(adding/3))

def adding():
    n=int(input("Enter number of nurses"))
    names=0

    for i in range(n):
        names+=int(input("Enter hours"))
        print(names)
    avg=names/n
    print("Avg is ",avg)

adding()