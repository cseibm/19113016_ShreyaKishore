a=input()
b=input()
i=1
while(int(a)>=i and int(b)>=1):
    if(int(a)%i==0 and int(b)%i==0):
        GCD=i
    i=i+1
n=int(a)/int(GCD)
m=int(b)/int(GCD)
print("ratio is",n,":",m)
