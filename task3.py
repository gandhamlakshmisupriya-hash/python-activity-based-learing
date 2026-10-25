
# Hospital Billing and Patient Classification

print("=== Hospital Billing System ===")

name = input("Enter patient name: ")
age = int(input("Enter patient age: "))

consultation = float(input("Enter consultation charges: Rs. "))
diagnostic = float(input("Enter diagnostic charges: Rs. "))
treatment = float(input("Enter treatment charges: Rs. "))

# Validate billing constraints
if (age <= 0 or consultation < 0 or
        diagnostic < 0 or treatment < 0):
    print("Invalid patient details or charges.")

else:
    total = consultation + diagnostic + treatment

    # Conditional concession policy
    if age >= 60:
        concession_rate = 20
    elif total >= 5000:
        concession_rate = 10
    else:
        concession_rate = 0

    concession = total * concession_rate / 100
    final_bill = total - concession

    # Sample payment classification policy
    if final_bill <= 1000:
        category = "Low Payment"
    elif final_bill <= 5000:
        category = "Medium Payment"
    else:
        category = "High Payment"

    # Display bill
    print("\n=== Patient Bill ===")
    print("Patient Name:", name)
    print("Age:", age)
    print("Consultation Charges: Rs.", consultation)
    print("Diagnostic Charges: Rs.", diagnostic)
    print("Treatment Charges: Rs.", treatment)
    print("Total Charges: Rs.", round(total, 2))
    print("Concession:", concession_rate, "%")
    print("Concession Amount: Rs.", round(concession, 2))
    print("Final Bill: Rs.", round(final_bill, 2))
    print("Patient Classification:", category)
