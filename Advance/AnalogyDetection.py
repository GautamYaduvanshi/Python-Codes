def mean(values):
    return sum(values) / len(values)

def std_dev(values, m):
    s = 0
    for v in values:
        s += (v - m) ** 2
    return (s / len(values)) ** 0.5

n = int(input("How many transactions? "))

transactions = []
for i in range(n):
    amt = float(input("Enter amount of transaction " + str(i + 1) + ": "))
    transactions.append(amt)

m = mean(transactions)
sd = std_dev(transactions, m)

upper_limit = m + 2 * sd
lower_limit = m - 2 * sd

print("\nAverage amount:", m)
print("Standard deviation:", sd)
print("Normal range: ", lower_limit, "to", upper_limit)

print("\nAnomalous transactions:")
for t in transactions:
    if t < lower_limit or t > upper_limit:
        print(t)
