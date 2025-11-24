def letter_value(ch):
    ch = ch.upper()
    if 'A' <= ch <= 'Z':
        return ord(ch) - ord('A') + 1
    return 0

def reduce_number(num):
    # keep 11 and 22 as master numbers
    while num > 9 and num != 11 and num != 22:
        s = 0
        for d in str(num):
            s += int(d)
        num = s
    return num

def personality(num):
    meanings = {
        1: "Leader, independent",
        2: "Cooperative, sensitive",
        3: "Creative, expressive",
        4: "Practical, hard working",
        5: "Adventurous, freedom loving",
        6: "Caring, responsible",
        7: "Thinker, spiritual",
        8: "Power, success",
        9: "Kind, humanitarian",
        11: "Intuitive, inspirational",
        22: "Master builder, visionary"
    }
    return meanings.get(num, "No meaning found")

report = []

n = int(input("How many names do you want to process? "))

for i in range(n):
    name = input("\nEnter name: ")
    total = 0
    for ch in name:
        total += letter_value(ch)

    num = reduce_number(total)
    mean = personality(num)

    report.append([name, total, num, mean])

print("\n--- Numerology Report ---")
for r in report:
    print("Name:", r[0])
    print("Total:", r[1], "| Name Number:", r[2])
    print("Personality:", r[3])
    print("-----------------------------")
