count = int(input("How many users do you want to add? "))
users = []
for i in range(count):
    user = input(f"Put user: {i+1}: ").lower()
    users.append(user)
for user in users:
    if user == "admin":
        print("Hello, boss! ")
    else:
        print(f"Hello, {user}! ")
print(f"Total users: {len(users)} ")
