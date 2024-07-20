n=int(input("enter the number"))
sum=0
i=1
c=0
while i<n:
    if n%i==0:
        print(i,end=" ")
        sum=sum+i
        c=c+1
    i=i+1
if sum==n:
    print("Perfect number")
    print(c)
else:
    print("Not Perfect number")
