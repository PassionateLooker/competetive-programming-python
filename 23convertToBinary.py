

# def decToBin(n):
#     binVal=''
#     while n!=0:
#         binVal+=str(n%2)
#         print("binval",binVal)
#         n=n//2
#         print("n",n)
#     return binVal[::-1]
#
# n=int(input("Enter number"))
# b=decToBin(n)
# print("Binary is",b)

def decToBin(n):
    binVal=''
    while n!=0:
        binVal+=str(n%2)
        n=n//2
    return binVal[::-1]

print(decToBin(11))