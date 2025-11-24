f = open("myfile.txt", "r")
lines = f.readlines()
f.close()

print("Lines in reverse order:")

for line in reversed(lines):
    print(line.strip())
