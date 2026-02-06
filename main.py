y=[34,24,45,98,23,89,47,24]
m=0
while m<len(y):
    print(y[m])
    m+=1 #prevents an infinite loop

L=[23,24,25,26,27,28,29,30,31,32,33,34,35]
for x in L[:8:2]:
    print(x,end="") #output is 23,25,27 and 29.