with open("notes.txt", "w") as f:
    f.write("Line 1: Learning Python\n")
    f.write("Line 2: Practicing File Handling\n")
    f.write("Line 3: Using read, readline, readlines, write\n")

with open("notes.txt", "r") as f:
    content = f.read()
    print("Reading with read():\n", content)

with open("notes.txt", "r") as f:
    print("\nReading with readline():")
    print(f.readline().strip()) 
    print(f.readline().strip()) 

with open("notes.txt", "r") as f:
    lines = f.readlines()
    print("\nReading with readlines():")
    print(lines)
