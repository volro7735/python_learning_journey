count = int(input("How many guests do you want to add? "))
guests = []
for i in range(count):
    guest = input(f"Add guest {i+1}: ").lower()
    guests.append(guest)
for guest in guests:
    if guest == "vip":
        print(f"VIP guest: {guest} ")
    else:
        print(f"Regular guest: {guest} ")
print(f"Total guests: {len(guests)} ")
