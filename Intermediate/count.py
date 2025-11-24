f = open("myfile.txt", "r")
data = f.read()
f.close()

characters = len(data)
words = len(data.split())
lines = len(data.split("\n"))

print("Characters:", characters)
print("Words:", words)
print("Lines:", lines)
