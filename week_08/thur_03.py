count = int(input("How many words do you want to enter? "))
words = []
for i in range(count):
    word = input(f"Put word {i+1} ").lower()
    words.append(word)
with_a = []
without_a = []
for word in words:
    if "a" in word:
        with_a.append(word)
    else:
        without_a.append(word)
print(f"Words with 'a' {with_a} ")
print(f"Words without 'a' {without_a} ")
