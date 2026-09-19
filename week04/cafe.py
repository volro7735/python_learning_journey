bill = float(input("How much is the bill. £ "))
tip_percent = float(input("What tip percentage do you leave? "))
tip_amount = bill * tip_percent / 100
total = bill + tip_amount
print(f"Bill: £{bill} ")
print(f"Tip: {tip_percent}% ")
print(f"Tip amount: £{tip_amount:.2f} ")
print(f"Total: £{total:.2f} ")
