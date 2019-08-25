# def stair(num):
#     for i in range(1, num+1):
#         k = i + 1 if i % 2 != 0 else i
#
#         for g in range(k, num):
#             if g >= k:
#                 print(end=" ")
#
#         for j in range(0, k):
#             if j == k - 1:
#                 print("*")
#             else:
#                 print("*", end=" ")
#
#
# stair(10)

def pattern(num):
    for i in range(1,num+1):
        k=i+1 if i%2!=0 else i
        for g in range(k,num):
            if g>=k:
                print(end=" ")
        for j in range(0,k):
            if j==k-1:
                print("*")
            else:
                print("*",end=" ")

pattern(10)













