age = int(input("How old are you? "))
day = input("What day is it? ").lower()
if age < 16 or day == "wednesday":
    print("Ticket price: 5 ")
else:
    print("Ticket price: 10 ")
