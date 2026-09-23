count = int(input("How many products do you want add? "))
products = []
for i in range(count):
    product = input(f"Add product {i+1} ").lower()
    products.append(product)
for product in products:
    if product == "milk" or product == "bread":
        print(f"Basic product {product} ")
    else:
        print(f"Other product {product} ")
print(f"Total products {len(products)} ")
