n=int(input("Enter value of n: "))
fact=1
i=1
while i<=n:
    fact*=i
    i+=1
print(n,"factorial =",fact)