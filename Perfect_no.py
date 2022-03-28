        ##for##
# def perfect_number(n):
#     sum=0
#     for x in range(1, n):
#         if n%x==0:
#             sum+=x
#     return sum==n
# print(perfect_number(6))

        ##while##

num=int(input("enter number"))
i=1
sum=0
while(i<num):
    if(num%i==0):
        sum=sum+i
    i=i+1
if(sum==num):
    print("% d is a Perfect Number" % num)
else:
    print("% d is not the Pecfect Number" % num)