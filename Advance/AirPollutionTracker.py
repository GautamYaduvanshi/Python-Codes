regions = []

n = int(input("How many regions? "))

for i in range(n):
    print("\nRegion", i + 1)
    name = input("Region name: ")
    pm25 = float(input("PM2.5 value: "))
    pm10 = float(input("PM10 value: "))
    co2 = float(input("CO2 value: "))

    # simple overall index (average of three)
    index = (pm25 + pm10 + co2) / 3.0

    regions.append([name, pm25, pm10, co2, index])

print("\n--- Pollution Data ---")
for r in regions:
    print("Region:", r[0], "| PM2.5:", r[1], "| PM10:", r[2], "| CO2:", r[3], "| Index: %.2f" % r[4])

# find region with highest index
highest = regions[0]
for r in regions[1:]:
    if r[4] > highest[4]:
        highest = r

print("\nRegion with highest pollution index:", highest[0], "with index %.2f" % highest[4])
