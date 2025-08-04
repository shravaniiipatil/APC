import math
n = int(input("Enter a number: "))
# Initialize sum
result = 0

# Calculate the series sum
for i in range(0, n+ 1):
    result += math.square(x)/math.factorial(i)
print(f"\nSum of the series 1 + 1/1! + 1/2! + ... + 1/{n}! is: {result}")
