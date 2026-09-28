count = int(input("How many numbers do you want to enter? "))
numbers = []
for i in range(count):
    number = int(input(f"Put numbers {i+1} "))
    numbers.append(number)
numbers.sort()
print(f"Smallest {numbers[0]} ")
print(f"Middle {numbers[count //2]} ")
print(f"Largest {numbers[-1]} ") 
