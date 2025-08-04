n = int(input("How many numbers? "))
i = 1

num = int(input("Enter number 1: "))
smallest = num

while i < n:
    num = int(input(f"Enter number {i+1}: "))
    if num < smallest:
        smallest = num
    i = i + 1

print("Smallest number is:", smallest)
