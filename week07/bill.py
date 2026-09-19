bill = int(input("How much is the bill? "))
has_card = input("Do you have a discount card? ").lower()
if bill >= 100 and has_card == "yes":
    print("You get discount 10%. ")
elif bill >= 100:
    print("You get discount 5% ")
else:
    print("No discount ")
