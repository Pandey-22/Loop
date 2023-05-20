# n=int(input("enter the number"))
# i=1
# c=0
# while i<=n:
#     if (i/2==i//2):
#         c=c+1
#         print("Even=",i)
#     else:
#         c1=c+1
#         print("Odd=",i)
#     i=i+1
# print("Tota Even Number=",c)
# print("Total Odd Number=",c1)



# n=int(input("enter the number"))
# r=n
# while r>0:
#     c=1
#     while c<=r:
#         print(c,end=" ")
#         c=c+1
#     print()
#     r=r-1



n=int(input("enter the number of rows"))
k=int(input("enter the number")) 
i=0
while i<=n:
    p=k
    j=0
    while j<=i:
        print(" ",end=" ")
        j=j+1
    while j<=n:
        print(p,end=" ")
        j=j+1
        p=p-1
    k=k-1
    print()
    i=i+1