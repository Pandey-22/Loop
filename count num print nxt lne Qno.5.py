# while loop 
# n=int(input("enter a number"))
# i=1
# while i<=n:
#     j=1
#     while j<=i:
#         print(j,end=" ")
#         j=j+1
#     print()
#     i=i+1



# for loop 
# n=int(input("enter the number"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print() 



n=int(input("enter the number:-"))
c=0
while (n>0):
    n=n//10
    c+=1
print(c)