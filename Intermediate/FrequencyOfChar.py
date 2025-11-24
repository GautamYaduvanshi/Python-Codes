f = open("myfile.txt", "r")
text = f.read()
f.close()

freq = {}

for char in text:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

print("Character Frequency:")
for k, v in freq.items():
    print(k, ":", v)
