def check_water(ph, turbidity, temp, tds):
    if ph < 6.5 or ph > 8.5 or turbidity > 5 or tds > 500:
        return "⚠ Water Contaminated"
    else:
        return "✅ Water Safe"

regions = []

n = int(input("Number of areas: "))

for i in range(n):
    print("\nArea", i+1)
    name = input("Area name: ")
    ph = float(input("pH: "))
    turbidity = float(input("Turbidity: "))
    temp = float(input("Temperature: "))
    tds = float(input("TDS: "))

    status = check_water(ph, turbidity, temp, tds)

    regions.append([name, ph, turbidity, temp, tds, status])

print("\n--- Water Test Report ---")
for r in regions:
    print("\nArea:", r[0])
    print("pH:", r[1], "| Turbidity:", r[2], "| Temp:", r[3], "| TDS:", r[4])
    print("Status:", r[5])
