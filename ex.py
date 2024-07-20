# 1st Q
# a=int(input("enter the  num"))
# i=1
# n=0
# while i<=a:
#     n=n+i
#     i=i+1
# print(n)


# 2nd Q
cumulative_sum=0
count=0
even_number=2
while cumulative_sum<=1000:
    cumulative_sum += even_number  
    count+=1
    even_number+=2 
print("Final sum:",cumulative_sum)
print("Number of even numbers added:",count)    




# 3rd Q
# i=1
# while i<100:
#     if i%7==0:
#         print(i)
#     i=i+1



# 4th Q
# n=int(input("enter the numbet"))
# i=1
# c=0
# while i<=n:
#     if i%2==0 and i%7==0:
#         print(i)
#     i=i+1



# 5th Q
# n=int(input("enter a number"))
# i=1
# s=0
# while i<=9:
#     if i%3==0:
#         s=s+i**2
#     i=i+1
# print(s)



# 6th Q
# n=int(input("enter a number"))
# i=1
# s=0
# while i<=n:
#     s=s+1/i
#     i=i+1
# print(s)


# 7th Q
# n=int(input("enter the number"))
# i=1
# s=0
# p=3
# q=5
# while i<=n:
#     if i%p==0 and i%q!=0:
#         s=s+i
#     i=i+1
# print(s)



# 8th Q
# a=int(input("enter the 1st number"))
# b=int(input("enter the 2nd number"))
# p=a*b
# while b>0:
#     r=a%b
#     a=b
#     b=r
# hcf=a
# lcm=p//hcf
# print(hcf,lcm)



# 9th Q
# n=int(input("enter number the sum of digits"))
# sum=0
# while n>0:    
#     sum=sum+n%10    
#     n=n//10    
# print("sum of digit=",sum)


# 10th Q
# n=int(input("enter the number"))
# r=0
# while n>0:
#     r=(r*10)+(n%10)
#     n=n//10
# print("Reverse Number=",r)


# 11th Q
# n=int(input("enter the number"))
# i=1
# while i<=n:
#     if n%i==0:
#         print(i,end=" ")
#     i=i+1



# 12th Q
# n=int(input("enter the number"))
# sum=0
# i=1
# while i<n:
#     if n%i==0:
#         sum=sum+i
#     i=i+1
# if sum==n:
#     print(i," is perfect number")
# else:
#     print(i,"is not perfect number")



# 13th Q
# n=int(input("enter the number"))
# i=1
# while i<=n:
#     j=2
#     while j<=i+1:
#         if i%j==0:
#             if i==j:
#                 print("Prime Number=",i)
#             break
#         j=j+1
#     i=i+1



# 14th Q



# 15th Q




# 16th Q




# 17th Q
# n=int(input("enter the number"))
# fact=1
# s=0
# i=1
# while i<=n:
#     fact*=i
#     s=s+fact
#     i=i+1
# print("Sum of the first",n,"terms of the factorial series is",s)



# 18th Q



# 19th Q




# 20 Q
# n=int(input("enter the number"))
# i=1
# while i<=n:
#     b=1
#     while b<=n-i:
#         print(" ",end=" ")
#         b=b+1
#     j=1
#     while j<=i:
#         print("*",end=" ")
#         j=j+1
#     print()        
#     i=i+1   
    


