count = int(input("How many numbers do you want to enter? "))
numbers = []
for i in range(count):
    number = int(input(f"Put number {i+1} "))
    numbers.append(number)
even = []
odd = []
for number in numbers:
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)
print(f"Even {even} ")
print(f"Odd {odd} ")
