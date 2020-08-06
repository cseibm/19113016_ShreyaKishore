a=int(input("enter the no of elements in the list:"))
sum=0
nolist=[]
for i in range (a):
    nolist.append(int(input("enter the element:")))
    if ((i% 2)==1):
        sum=sum+nolist[i]
print(sum)
