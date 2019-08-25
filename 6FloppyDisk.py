# def floppy():
#
#
#     free=int(input("Input free space"))
#     used=int(input("Input used space"))
#     delete=int(input("Input the number of space you want to remove"))
#     used+=delete
#
#
#
#     print("New free space in the floppy is: ",used)
#
# floppy()

f=int(input("Enter free disk space"))
u=int(input("Enter used disk space"))
o=int(input("Enter old file space"))
n=int(input("Enter new file space"))

totalDiskSize=f+u
newDiskSpace=u-o
newDiskSpace+=n
currentFreeSpace=totalDiskSize-newDiskSpace

print("Free space available is ",currentFreeSpace," bytes")