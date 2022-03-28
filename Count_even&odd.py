odd=0
even=0
i=0
while i<=15:
    if i%2==0:
        even=even+1
    else:
        odd=odd+1
    i=i+1
print(even,"even number")
print(odd,"odd number")