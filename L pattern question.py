# for loop
# for row in range(7):
#     for col in range(6):
#         if col==0 or row==6 and col>=0:
#             print("*",end=" ")
#         else:
#             print(end=" ")
#     print()
    


# while loop
row=0
while row<=6:
    col=0
    while col<=5:
        if col==0 or row==6 and col>=0:
            print("*",end=" ")
        else:
            print(end=" ")
        col=col+1
    print()
    row=row+1