with open("pointer.txt", "w") as f:
    f.write("Hello World\n")
    f.write("Python File Handling\n")

with open("pointer.txt", "r") as f:
    print("File opened...")

    print("Position:", f.tell())

    data = f.read(5)
    print("Read data:", data)

    print("Position after reading 5 chars:", f.tell())

    f.seek(0)
    print("Position after seek(0):", f.tell())

    print("Full content:\n", f.read())
