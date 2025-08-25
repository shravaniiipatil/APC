with open("demo.txt", "w") as f:
    f.write("This is written using 'w' mode.\n")
    f.write("Old content (if any) is erased.\n")

with open("demo_bin.txt", "wb") as f:
    f.write(b"This is written using 'wb' mode.\n")

with open("demo.txt", "a") as f:
    f.write("This line is added using 'a' mode.\n")

with open("demo2.txt", "w+") as f:
    f.write("This is written using 'w+' mode.\n")
    f.seek(0)   # Move cursor to start for reading
    print("Reading from 'w+' mode file:\n", f.read())
