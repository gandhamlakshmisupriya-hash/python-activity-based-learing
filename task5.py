
# Multi-Plan Telecommunications Cost Optimization

budget = float(input("Enter your budget (Rs.): "))
required_data = float(input("Enter required data (GB): "))
required_calls = int(input("Enter required call minutes: "))
required_validity = int(input("Enter required validity (days): "))

plans = [
    {"name": "Plan A", "price": 199, "data": 2,
     "calls": 300, "validity": 28, "extra_rate": 20},
    {"name": "Plan B", "price": 299, "data": 3,
     "calls": 600, "validity": 56, "extra_rate": 15},
    {"name": "Plan C", "price": 399, "data": 5,
     "calls": 900, "validity": 84, "extra_rate": 10}
]

eligible_plans = []

for plan in plans:
    extra_data = max(0, required_data - plan["data"])
    extra_calls = max(0, required_calls - plan["calls"])

    # Excess usage charges
    excess_charge = extra_data * plan["extra_rate"]
    excess_charge += extra_calls * 0.50

    total_cost = plan["price"] + excess_charge

    print("\n", plan["name"])
    print("Base Price: Rs.", plan["price"])
    print("Excess Charges: Rs.", round(excess_charge, 2))
    print("Total Cost: Rs.", round(total_cost, 2))

    # Check usage, validity and budget
    if (plan["data"] >= required_data
            and plan["calls"] >= required_calls
            and plan["validity"] >= required_validity
            and total_cost <= budget):
        eligible_plans.append((total_cost, plan["name"]))

# Find the most economical eligible plan
print("\n--- Best Plan ---")

if eligible_plans:
    eligible_plans.sort()

    cost, name = eligible_plans[0]

    print("Most Economical Plan:", name)
    print("Total Cost: Rs.", round(cost, 2))
else:
    print("No plan satisfies all requirements.")
