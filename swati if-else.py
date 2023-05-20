days=int(input("enter the number"))
if days<=5:
    print(days*2)
elif days>=6 and days<=10:
    print((days-5)*3+5*2)
elif days>=11 and days<=15:
    print((days-10)*4+5*3+5*2)
else:
    print((days-15)*5+5*4+5*3+5*2)