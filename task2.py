
# Progressive Electricity Billing System

fixed_charge = 50
surcharge_rate = 5       # 5% surcharge
rebate_rate = 10         # 10% rebate
monthly_bills = []

n = int(input("Enter number of months: "))

for month in range(1, n + 1):
    print("\nMonth", month)
    units = int(input("Enter electricity units consumed: "))

    # Calculate progressive slab charges
    if units <= 100:
        energy_charge = units * 2
    elif units <= 200:
        energy_charge = 100 * 2 + (units - 100) * 3
    elif units <= 300:
        energy_charge = 100 * 2 + 100 * 3 + (units - 200) * 5
    else:
        energy_charge = (
            100 * 2 + 100 * 3 + 100 * 5
            + (units - 300) * 7
        )

    subtotal = energy_charge + fixed_charge
    surcharge = subtotal * surcharge_rate / 100

    # Rebate for low consumption
    if units <= 100:
        rebate = subtotal * rebate_rate / 100
    else:
        rebate = 0

    bill = subtotal + surcharge - rebate
    monthly_bills.append(bill)

    print("Energy Charge: Rs.", round(energy_charge, 2))
    print("Fixed Charge: Rs.", fixed_charge)
    print("Surcharge: Rs.", round(surcharge, 2))
    print("Rebate: Rs.", round(rebate, 2))
    print("Total Bill: Rs.", round(bill, 2))

# Compare monthly bills
print("\n--- Monthly Bill Comparison ---")

for i in range(n):
    print("Month", i + 1, ": Rs.", round(monthly_bills[i], 2))

    if i > 0:
        increase = monthly_bills[i] - monthly_bills[i - 1]

        if monthly_bills[i - 1] > 0:
            percentage = increase / monthly_bills[i - 1] * 100
        else:
            percentage = 0

        print("Change: Rs.", round(increase, 2))
        print("Percentage Change:", round(percentage, 2), "%")

        if percentage >= 30:
            print("Warning: Unusual increase in bill!")
