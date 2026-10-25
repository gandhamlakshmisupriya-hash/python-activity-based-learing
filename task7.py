
# Retail Billing System

products = {
    "1": {"name": "Shirt", "price": 800, "tax": 5},
    "2": {"name": "Shoes", "price": 1500, "tax": 12},
    "3": {"name": "Book", "price": 300, "tax": 0}
}

total = 0
max_discount = 500

n = int(input("Enter number of products: "))

print("\n--- Product List ---")
for key, p in products.items():
    print(key, p["name"], "- Rs.", p["price"],
          "Tax:", str(p["tax"]) + "%")

print("\n--- Itemized Invoice ---")

for i in range(n):
    choice = input("\nEnter product number: ")

    if choice not in products:
        print("Invalid product!")
        continue

    quantity = int(input("Enter quantity: "))

    if quantity <= 0:
        print("Invalid quantity!")
        continue

    p = products[choice]
    amount = p["price"] * quantity

    # Category-specific tax
    tax = amount * p["tax"] / 100

    # Product-wise discount
    discount = amount * 0.10 if quantity >= 3 else 0

    print("\nProduct:", p["name"])
    print("Quantity:", quantity)
    print("Price: Rs.", p["price"])
    print("Amount: Rs.", round(amount, 2))
    print("Discount: Rs.", round(discount, 2))
    print("Tax: Rs.", round(tax, 2))

    total += amount - discount + tax

# Threshold discount
if total >= 5000:
    threshold_discount = total * 0.05
else:
    threshold_discount = 0

# Maximum concession limit
threshold_discount = min(threshold_discount, max_discount)

final_bill = total - threshold_discount

print("\n========== FINAL INVOICE ==========")
print("Subtotal after item discounts and tax: Rs.",
      round(total, 2))
print("Threshold Discount: Rs.",
      round(threshold_discount, 2))
print("Maximum Concession: Rs.", max_discount)
print("-----------------------------------")
print("Final Amount: Rs.", round(final_bill, 2))
print("===================================")
