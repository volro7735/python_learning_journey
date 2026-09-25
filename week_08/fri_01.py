count = int(input("How many numbers do you want to enter? "))
numbers = []
for i in range(count):
    number = int(input(f"Put numbers {i+1} "))
    numbers.append(number)
search = int(input("What number do you want to find? "))
if search in numbers:
    print(f"{search} is in the list. ")
else:
    print(f"{search} is not in the list. ")
