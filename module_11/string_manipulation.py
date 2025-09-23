with open("example.txt", "r") as file:
    for line in file:
        cleaned_line = line.strip()
        print(cleaned_line)
with open("example.txt", "r") as file:
    for line in file:
        words = line.strip().split()
        print(words)
name="Alice"
age=25
with open("output.txt", "w") as file:
    file.write("Name: "+name+"\nAge: "+str(age)+"\n")
with open("example.txt", "r") as infile, open("output.txt", "w") as outfile:
    for line in infile:
        cleaned_line = line.strip()
        modified_line = cleaned_line.replace("Line 1", "line X")
        outfile.write(modified_line+"\n")