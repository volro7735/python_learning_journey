count = int(input("How many numbers do you want to enter?" ))
numbers = []
for i in range(count):
    number = int(input(f"Put number {i+1} "))
    numbers.append(number)
pos_count = 0
neg_count = 0
zero_count = 0
for number in numbers:
    if number > 0:
        print(f"{number} is positive ")
        pos_count += 1
    elif number < 0:
        print(f"{number} is negative ")
        neg_count += 1
    else:
        print(f"{number} is zero ")
        zero_count += 1
print(f"Total numbers {len(numbers)} ")
print(f"Positive {pos_count} ")
print(f"Negative {neg_count} ")
print(f"Zero {zero_count} ")

