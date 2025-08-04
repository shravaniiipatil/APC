n = int(input("How many numbers? "))
i = 1

num = int(input("Enter number 1: "))
largest = num

while i < n:
    num = int(input(f"Enter number {i+1}: "))
    if num > largest:
        largest = num
    i = i + 1

print("Largest number is:", largest)
