a=[1,2,3,4,5,6,7,8,9,10]
b=int(input())
c=[a[i:i+b] for i in range(0,len(a),b)]  
print(c) 
