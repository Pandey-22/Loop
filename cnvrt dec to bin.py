# convert decimal to binary

# i=int(input("enter the number"))
# sum=0
# while i>0:
#     a=i%2
#     sum=sum*10+a
#     i=i//2
# print(sum)




binary=input("Enter a binary number:-")
dec=0
p=0
binary=binary[::-1]
for bit in binary:
    if bit=="1":
        dec+=2**p
    p+=1
print("Decimal Number:-",dec)