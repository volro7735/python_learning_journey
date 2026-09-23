count = int(input("How many words do you want to add?" ))
words = []
for i in range(count):
    word = input(f"Add word {i+1} ").lower()
    words.append(word)
for word in words:
    if len(word) > 5:
        print(f"Long word {word} ")
    else:
        print(f"Short word {word} ")
print(f"Total words {len(words)} ")
