count = int(input("How many products do you want to enter? "))
products = []
for i in range(count):
    product = input(f"Put product {i+1} ").lower()
    products.append(product)
basic_count = 0
other_count = 0
for product in products:
    if product == "milk" or product == "bread":
        print(f"Basic product {product} ")
        basic_count += 1
    else:
        print(f"Other product {product} ")
        other_count += 1
print(f"Total products {len(products)} ")
print(f"Basic products {basic_count} ")
print(f"Other products {other_count} ")
