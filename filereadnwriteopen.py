file = open("example.txt", "w")   
file.write("Hello, this is Method 1!\n")
file.close()  

file = open("example.txt", "r")  
content = file.read()
print("File Content:", content)
file.close()
