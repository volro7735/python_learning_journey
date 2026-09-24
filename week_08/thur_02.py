count = int(input("How many numbers do you want to enter? "))
numbers = []
for i in range(count):
    number = int(input(f"Put number {i+1} "))
    numbers.append(number)
positive = []
negative = []
for number in numbers:
        if number > 0:
            positive.append(number)
        if number < 0:
            negative.append(number)
print(f"Positive {positive} ")
print(f"Negative {negative} ")
