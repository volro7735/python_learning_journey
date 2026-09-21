count = int(input("How many numbers do you want to enter? "))
numbers = []
for i in range(count):
    number = int(input(f"Put number {i+1}: "))
    numbers.append(number)
for number in numbers:
    if number > 10:
        print(f"{number} is greater than 10 ")
    elif number < 10:
        print(f"{number} is less than 10 ")
    else:
        print(f"{number} is exactly 10 ")
print(f"Total numbers: {len(numbers)} ")
