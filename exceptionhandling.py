try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    result = a / b  
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Please enter valid numbers only.")
else:
    print("Result:", result)  
finally:
    print("Program execution completed!")

