# from collections import Counter
#
# lst=['arun','alex','sar','alex','daya','arun','daya']
#
# countert=Counter(lst)
#
# def most_frequent(lst):
#     count = {}
#     max_count = 0
#     max_item = None
#
#     for i in lst:
#         if i not in count:
#
#             count[i] = 1
#
#         else:
#             count[i] += 1
#
#         if count[i] > max_count:
#             max_count = count[i]
#
#             max_item = i
#
#     return max_item
#
#
# print(most_frequent([3, 3, 1, 3, 1, 1, 1, 3, 3, 3, 5, 3, 1, 1, 1, 1, 1]))

# def most_frequent(lst):
#     count={}
#     max_item=None
#     max_count=0
#
#     for i in lst:
#         if i not in count:
#             count[i]=1
#         else:
#             count[i]+=1
#
#         if count[i]>max_count:
#             max_count=count[i]
#             max_item=i
#
#     return max_item
#
# print(most_frequent([1,2,2,1,2]))

def printStringDuplicate(names):
    x=names.split()
    size=len(x)
    repeated=[]
    for i in range(size):
        print(i,"i")
        k=i+1
        print(k,"k")
        print(repeated)
        for j in range(k,size):

            if x[i]==x[j] and x[i] not in repeated:
                print(x[i],x[j],"x[i]==x[j]")

                repeated.append(x[i])
                print(repeated)

names="saurabh saurabh singham manoj manoj"
printStringDuplicate(names)



















