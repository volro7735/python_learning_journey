count = int(input("How many answers do you want to enter? "))
answers = []
for i in range(count):
    answer = input(f"Put answers {i+1} ").lower()
    answers.append(answer)
yes_count = 0
no_count = 0
for answer in answers:
    if answer =="yes":
        print("Yes")
        yes_count += 1
    elif answer == "no":
        print("No")
        no_count += 1
    else:
        print(f"Unknown answer {answer} ")
print(f"Total answers {len(answers)} ")
print(f"Yes {yes_count} ")
print(F"No {no_count} ")
