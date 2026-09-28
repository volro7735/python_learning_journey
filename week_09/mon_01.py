count = int(input("How many words do you want to enter? "))
words = []
for i in range(count):
    word = input(f"Put words {i+1} ").lower()
    words.append(word)
a_count = 0
for word in words:
    if "a" in word:
        print(f"{word} contains 'a' ")
        a_count += 1
    else:
        print(f"{word} does not contein 'a'. ")
print(f"Words with 'a' {a_count}. ")
