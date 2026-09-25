count = int(input("How many numbers do you want to enter? "))
numbers = []
for i in range(count):
    number = int(input(f"Put numbers {i+1} "))
    numbers.append(number)
search = int(input("What number do you want to find? "))
matches = 0
for number in numbers:
    if number == search:
        matches += 1
print(f"{search} appears {matches} times. ")
