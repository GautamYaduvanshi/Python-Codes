import sys

try:
    if len(sys.argv) < 2:
        print("Please provide file name as command line argument")
        exit()

    user_file = sys.argv[1]

    f1 = open(user_file, "r")
    text = f1.read().lower()
    f1.close()

    f2 = open("words.txt", "r")
    correct_words = f2.read().lower().split()
    f2.close()

    words = text.split()

    print("Misspelled words are:")

    for word in words:
        word = word.strip(".,!?")

        if word not in correct_words:
            print(word)

except:
    print("Error: Unable to open file")
