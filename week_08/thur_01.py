count = int(input("How many numbers do you want to enter? "))
numbers = []
for i in range(count):
    number = int(input(f"Put number {i+1} "))
    numbers.append(number)
total = 0
for number in numbers:
    total += number
average = total / count
print(f"Total {total} ")
print(f"Average {average} ")
