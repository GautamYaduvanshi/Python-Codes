def calc_bmi(weight, height):
    return weight / (height * height)

def get_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

people = []
summary = {"Underweight": 0, "Normal": 0, "Overweight": 0, "Obese": 0}

n = int(input("How many people? "))

for i in range(n):
    print("\nPerson", i + 1)
    name = input("Name: ")
    age = int(input("Age: "))
    weight = float(input("Weight (kg): "))
    height = float(input("Height (m): "))

    bmi = calc_bmi(weight, height)
    cat = get_category(bmi)

    people.append([name, age, weight, height, bmi, cat])
    summary[cat] += 1

print("\n--- BMI Report ---")
for p in people:
    print("Name:", p[0], "| Age:", p[1], "| BMI: %.2f" % p[4], "| Category:", p[5])

print("\n--- Summary ---")
for k, v in summary.items():
    print(k, ":", v)
