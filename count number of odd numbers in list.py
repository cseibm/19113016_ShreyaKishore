a=int(input("enter the no. of elements in the list:"))
count = 0
nolist=[]
for i in range(a):
    nolist.append(int(input("enter the element:")))
for j in nolist:
    if ((j% 2)==1):
        count =count+1
print(count)
