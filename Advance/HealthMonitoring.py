def check_alert(bp, sugar, heart):
    if bp > 140 or sugar > 180 or heart > 110:
        return "⚠ ALERT: Inform caregiver!"
    else:
        return "Vitals are normal."

patients = []

n = int(input("How many patients? "))

for i in range(n):
    print("\nPatient", i+1)
    name = input("Name: ")
    bp = int(input("Blood Pressure: "))
    sugar = int(input("Sugar Level: "))
    heart = int(input("Heart Rate: "))
    medicine = input("Medication time: ")

    alert = check_alert(bp, sugar, heart)

    patients.append([name, bp, sugar, heart, medicine, alert])

print("\n--- Health Report ---")
for p in patients:
    print("\nName:", p[0])
    print("BP:", p[1], "| Sugar:", p[2], "| Heart Rate:", p[3])
    print("Medicine time:", p[4])
    print("Status:", p[5])
