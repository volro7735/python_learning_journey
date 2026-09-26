age = int(input("How old are you?" ))
if age < 18:
    print("You are too young. ")
else:
    ticket = input("Do you have a ticket? ").lower()
    if ticket == "yes":
        print("You can enter. ")
    else:
        print("You need a ticket. ")
