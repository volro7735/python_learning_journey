count = int(input("How many names do you want to enter? "))
names = []
for i in range(count):
    name = input(f"Add names {i+1} ").lower()
    names.append(name)
a_count = 0
for name in names:
    if "a" in name:
        print(f"{name} contains 'a' ")
        a_count += 1
    else:
        print(f"{name} does not contain 'a' ")
print(f"Total names {len(names)}")
print(f"Names with 'a' {a_count} ")
