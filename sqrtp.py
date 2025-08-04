import math

num = int(input("Enter a number: "))

# Calculate square root
sqrt_num = math.isqrt(num)  # integer square root

# Check if num is a perfect square
if sqrt_num * sqrt_num == num:
    # Now check if sqrt_num is prime
    if sqrt_num <= 1:
        print(f"The square root {sqrt_num} is not prime.")
    else:
        is_prime = True
        for i in range(2, int(sqrt_num ** 0.5) + 1):
            if sqrt_num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(f"The square root {sqrt_num} is prime.")
        else:
            print(f"The square root {sqrt_num} is not prime.")
else:
    print(f"{num} is not a perfect square, so its square root is not an integer.")
