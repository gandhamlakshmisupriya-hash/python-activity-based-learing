
# Campus Event Financial Planning

print("=== Campus Event Financial Planning ===")

venue = float(input("Enter venue cost: Rs. "))
equipment = float(input("Enter equipment cost: Rs. "))
catering = float(input("Enter catering cost per participant: Rs. "))
transport = float(input("Enter transport cost: Rs. "))
certificate = float(input("Enter certificate cost per participant: Rs. "))

participants = int(input("Enter expected participants: "))
fee = float(input("Enter registration fee per participant: Rs. "))
sponsorship = float(input("Enter sponsorship amount: Rs. "))

if (venue < 0 or equipment < 0 or catering < 0
        or transport < 0 or certificate < 0
        or participants < 0 or fee < 0 or sponsorship < 0):
    print("Invalid input values.")

else:
    # Calculate total expenses
    fixed_cost = venue + equipment + transport
    variable_cost = (catering + certificate) * participants
    total_cost = fixed_cost + variable_cost

    # Calculate income
    participant_income = fee * participants
    total_income = participant_income + sponsorship

    # Calculate financial result
    balance = total_income - total_cost

    # Sponsorship shortfall
    required_sponsorship = max(0, total_cost - participant_income)
    shortfall = max(0, required_sponsorship - sponsorship)

    # Minimum registrations needed to break even
    contribution = fee - catering - certificate

    print("\n=== Event Financial Report ===")
    print("Fixed Costs: Rs.", round(fixed_cost, 2))
    print("Variable Costs: Rs.", round(variable_cost, 2))
    print("Total Expenses: Rs.", round(total_cost, 2))
    print("Participant Contributions: Rs.",
          round(participant_income, 2))
    print("Sponsorship Received: Rs.", round(sponsorship, 2))
    print("Sponsorship Shortfall: Rs.", round(shortfall, 2))

    if balance >= 0:
        print("Status: Event is financially feasible.")
        print("Surplus: Rs.", round(balance, 2))
    else:
        print("Status: Event is running at a loss.")
        print("Deficit: Rs.", round(abs(balance), 2))

    if contribution > 0:
        remaining = max(0, fixed_cost - sponsorship)
        minimum = int(remaining // contribution)

        if remaining % contribution != 0:
            minimum += 1

        print("Minimum registrations to break even:", minimum)
    else:
        print("Break-even is not possible at this registration fee.")
