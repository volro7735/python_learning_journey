count = int(input("How many words do you want to enter? "))
words = []
for i in range(count):
    word = input(f"Put word {i+1} ").lower()
    words.append(word)
longest_word = ""
for word in words:
    if len(word) > len(longest_word):
        longest_word = word
print(f"Longest word {longest_word} ")
print(f"length {len(longest_word)} ")
