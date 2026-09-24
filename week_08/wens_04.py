count = int(input("How many numbers do you want to enter? "))
numbers = []
for i in range(count):
    number = int(input(f"Put number {i+1} "))
    numbers.append(number)
max_number = numbers [0]
for number in numbers:
    if number > max_number:
        max_number = number
print(f"Max number {max_number} ")
