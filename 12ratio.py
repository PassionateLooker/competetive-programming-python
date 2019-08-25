# red=5000000
# white=8000
#
# ratio1=1
# ratio2=red/white
#
# print(ratio1,":",ratio2)
def g(white,red):
    return white if(red==0) else g(red,white%red)

red=5000000
white=8000

factor=g(white,red)

whiteratio=int(white/factor)
redratio=int(red/factor)

print(whiteratio,redratio)
