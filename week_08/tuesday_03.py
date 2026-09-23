count = int(input("How many numbers do you want to enter? "))
numbers = []
for i in range(count):
    number = int(input(f"Put number {i+1} "))
    numbers.append(number)
even_count = 0
for number in numbers:
    if number % 2 == 0:
        print(f"{number} is even ")
        even_count += 1
else:
    print(f"{number} is odd ")
print(f"Total numbers {len(numbers)}") 
print(f"Even numbers {even_count} ")
        
