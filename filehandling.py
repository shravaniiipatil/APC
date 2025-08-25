with open("abc.txt", "w") as f:
    f.write("This is ABC file.\n")
    f.write("It has some content.\n")

with open("abc.txt", "r") as f1, open("pqr.txt", "w") as f2:
    data = f1.read()
    f2.write(data)

with open("pqr.txt", "r") as f1, open("xyz.txt", "a") as f2:
    data = f1.read()
    f2.write(data)
with open("xyz.txt", "r") as f:
    f.seek(0)

    data10 = f.read(10)
    print("First 10 bytes using read():", data10)
    print("Current position after 10 bytes (tell):", f.tell())

    f.seek(0)

    line1 = f.readline().strip()
    line2 = f.readline().strip()
    print("\nFirst two lines using readline():")
    print(line1)
    print(line2)

    print("Current position after 2 lines (tell):", f.tell())
