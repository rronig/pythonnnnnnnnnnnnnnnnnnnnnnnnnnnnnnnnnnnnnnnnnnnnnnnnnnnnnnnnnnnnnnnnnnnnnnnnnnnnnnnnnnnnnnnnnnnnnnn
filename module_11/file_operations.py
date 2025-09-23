from tarfile import ReadError
import os
#file_path="example.txt"
#file=open(file_path,"r")
#content=file.read()
#file.close()
file_path="example.txt"
with open(file_path, "r") as file:
    content=file.read()
    print(content)

#r=read
#w=write
#a=append
#b=binary
#x=exclusive creation
with open(file_path, "r") as file:
    content=file.read()
    line=file.readline()
    lines=file.readlines()
    print(line)
    print(lines)
    print(content)
with open(file_path, "w") as file:
    file.write("Welcome to Kosovo")
lines=['sddsafdfsdfasdfsdfaasdfasdfweafsfdeveghbywesrx\n', 'sddsafdfsdfasdfsdfaasdfasdfweafsfdeveghbywesrx\n']
with open(file_path, "w") as file:
    file.writelines(lines)
with open(file_path, "r") as file:
    file.seek(0)
    data=file.read()
    print(data)
if os.path.exists(file_path):
    print("File exists")
with open(file_path, "a") as file:
    file.write("new data appended")
data=b'binary data'
with open("example.bin", "wb") as file:
    file.write(data)
with open("example.bin", "rb") as file:
    data=file.read()