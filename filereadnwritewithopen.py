with open("example2.txt", "w") as file:
    file.write("Hello, this is Method 2!\n")

with open("example2.txt", "r") as file:
    content = file.read()
    print("File Content:", content)
