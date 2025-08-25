with open("demo.txt", "w") as f:
    f.write("Hello World\n")
    f.write("Python File Handling\n")
    f.write("Reading in different modes\n")

with open("demo.txt", "r") as f:
    print(f.read())

with open("demo.txt", "rb") as f:
    print(f.read())

with open("demo.txt", "r") as f:
    print(f.readline().strip())
    print(f.readline().strip())

with open("demo.txt", "r") as f:
    print(f.readlines())

with open("demo.txt", "r+") as f:
    content = f.read()
    print("Before writing:\n", content)
    f.write("\nAdded new line in r+ mode!")
