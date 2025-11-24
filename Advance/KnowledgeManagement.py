knowledge = {}

n = int(input("How many topics to add? "))

for i in range(n):
    topic = input("\nEnter topic name: ")
    info = input("Enter information: ")

    knowledge[topic] = info

print("\n--- Knowledge System ---")
key = input("Enter topic to search: ")

if key in knowledge:
    print("\nInformation on", key, ":\n", knowledge[key])
else:
    print("Topic not found.")
