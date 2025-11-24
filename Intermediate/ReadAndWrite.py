# Writing to a file
f = open("myfile.txt", "w")
f.write("Hello, this is a file handling program.\n")
f.write("Written using Python.")
f.close()

# Reading from the file
f = open("myfile.txt", "r")
content = f.read()
print(content)
f.close()
