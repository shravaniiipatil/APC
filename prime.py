n=int(input("Enter value of n: "))
i=2
is_Prime = True
while i<n:
    if n % i == 0:
        is_Prime = False
        break
    i+=1
if n < 2:
    print("Not a prime number")
elif is_Prime:
    print("Prime Number")
else:
    print("Not a prime number")    

