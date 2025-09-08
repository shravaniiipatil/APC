import os
print(os.listdir())          
print(os.listdir("C:/Users")) 
os.mkdir("new_folder")        
os.makedirs("a/b/c") 
os.rmdir("new_folder")         
os.removedirs("a/b/c")       
os.chdir("a/b/c")
print(os.getcwd())
