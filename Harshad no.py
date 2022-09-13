num=int(input("enter the number"))
copy=num
sum=0
while num:
    sum+=num%10
    num//=10
if copy%sum==0:
    print(copy,"is Harshad Number")
else:
    print(copy,"is not Harshad Number")
