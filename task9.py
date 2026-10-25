
# Multi-Currency Travel Budget Analysis

budget = float(input("Enter travel budget in INR: "))
fee_rate = float(input("Enter conversion fee percentage: "))
n = int(input("Enter number of expense categories: "))

exchange_rates = {
    "INR": 1.0,
    "USD": 85.0,
    "EUR": 95.0,
    "GBP": 110.0
}

expenses = {}
total_spending = 0

for i in range(n):
    print("\nExpense", i + 1)

    category = input("Enter category (Hotel/Food/Travel/Shopping): ")
    amount = float(input("Enter expense amount: "))
    currency = input("Enter currency (INR/USD/EUR/GBP): ").upper()

    if amount < 0 or currency not in exchange_rates:
        print("Invalid amount or currency. Try again.")
        continue

    # Convert to INR
    converted = amount * exchange_rates[currency]

    # Calculate conversion fee
    fee = converted * fee_rate / 100
    final_amount = converted + fee

    expenses[category] = expenses.get(category, 0) + final_amount
    total_spending += final_amount

    print("Converted Amount: Rs.", round(converted, 2))
    print("Conversion Fee: Rs.", round(fee, 2))
    print("Total Expense: Rs.", round(final_amount, 2))

# Display budget analysis
print("\n--- Travel Budget Report ---")

for category, amount in expenses.items():
    print(category, ": Rs.", round(amount, 2))

print("Total Spending: Rs.", round(total_spending, 2))
print("Travel Budget: Rs.", round(budget, 2))

if total_spending > budget:
    print("Status: Budget Exceeded")
    print("Excess Amount: Rs.", round(total_spending - budget, 2))
else:
    print("Status: Within Budget")
    print("Remaining Budget: Rs.", round(budget - total_spending, 2))

# Find largest expense category
if expenses:
    largest = max(expenses, key=expenses.get)
    print("Largest Expense Category:", largest)
    print("Amount: Rs.", round(expenses[largest], 2))
else:
    print("No valid expenses recorded.")
