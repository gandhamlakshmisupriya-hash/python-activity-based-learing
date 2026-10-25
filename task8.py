
# Manufacturing Cost and Profitability Analysis

print("=== Manufacturing Cost Analysis ===")

product = input("Enter product name: ")
quantity = int(input("Enter quantity produced: "))

material_cost = float(input("Enter material cost per unit: Rs. "))
labour_cost = float(input("Enter labour cost per unit: Rs. "))
machine_cost = float(input("Enter total machine cost: Rs. "))
wastage_rate = float(input("Enter wastage percentage: "))
selling_price = float(input("Enter selling price per unit: Rs. "))
profit_target = float(input("Enter target profit percentage: "))

if (quantity <= 0 or material_cost < 0 or labour_cost < 0
        or machine_cost < 0 or not 0 <= wastage_rate <= 100
        or selling_price < 0 or profit_target < 0):
    print("Invalid input values.")

else:
    # Calculate total material cost
    material_total = material_cost * quantity

    # Calculate wastage cost
    wastage_cost = material_total * wastage_rate / 100

    # Calculate total labour cost
    labour_total = labour_cost * quantity

    # Calculate total production cost
    total_cost = (material_total + wastage_cost
                  + labour_total + machine_cost)

    # Calculate revenue and profit
    revenue = selling_price * quantity
    profit = revenue - total_cost

    # Calculate profit percentage
    if total_cost > 0:
        profit_percent = profit / total_cost * 100
    else:
        profit_percent = 0

    # Check profit target
    print("\n=== Production Report ===")
    print("Product Name:", product)
    print("Quantity Produced:", quantity)
    print("Material Cost: Rs.", round(material_total, 2))
    print("Wastage Cost: Rs.", round(wastage_cost, 2))
    print("Labour Cost: Rs.", round(labour_total, 2))
    print("Machine Cost: Rs.", round(machine_cost, 2))
    print("Total Production Cost: Rs.", round(total_cost, 2))
    print("Total Revenue: Rs.", round(revenue, 2))
    print("Total Profit: Rs.", round(profit, 2))
    print("Profit Percentage:", round(profit_percent, 2), "%")

    if profit_percent >= profit_target:
        print("Result: Target profit achieved!")
    else:
        print("Result: Target profit not achieved.")
